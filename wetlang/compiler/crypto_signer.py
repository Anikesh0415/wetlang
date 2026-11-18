"""
WetLang Biosafety Cryptographic Signing & Tamper Verification
=============================================================
Enforces cryptographic provenance for WBC binaries running on physical biological wetware.
Implements HMAC-SHA256 authenticated manifests preventing unauthorized bytecode execution.
"""

import hmac
import hashlib
import struct
from typing import Tuple, Optional, List

from compiler.isa import HEADER_MAGIC, HEADER_SIZE, Capability


SIGNATURE_MAGIC = b"WETSIG01"  # 8 bytes
SIGNATURE_LEN = 32           # HMAC-SHA256 digest length


def sign_bytecode(bytecode: bytes, secret_key: bytes) -> bytes:
    """
    Signs a WBC binary with an HMAC-SHA256 biosafety certificate.
    Sets the CAP_SIGNATURE_VERIFIED capability flag in the header and appends
    the signed manifest trailer.
    """
    if len(bytecode) < HEADER_SIZE or bytecode[:4] != HEADER_MAGIC:
        raise ValueError("Invalid WBC binary: header truncated or magic mismatch")

    # Unpack capabilities at offset 6 (uint16)
    caps = struct.unpack_from("<H", bytecode, 6)[0]
    caps |= Capability.CAP_SIGNATURE_VERIFIED

    # Reconstruct bytecode with updated capabilities
    modified = bytearray(bytecode)
    struct.pack_into("<H", modified, 6, caps)

    # Compute HMAC-SHA256 over entire modified bytecode
    h = hmac.new(secret_key, bytes(modified), hashlib.sha256)
    digest = h.digest()

    # Append trailer: [SIGNATURE_MAGIC (8s)] [DIGEST (32s)]
    trailer = struct.pack("<8s32s", SIGNATURE_MAGIC, digest)
    return bytes(modified) + trailer


def verify_bytecode_signature(signed_bytecode: bytes, secret_key: bytes) -> Tuple[bool, str]:
    """
    Verifies that the signed WBC binary carries a valid cryptographic signature trailer
    and that the bytecode body matches the computed digest.
    Returns (is_valid: bool, reason: str).
    """
    trailer_len = 8 + 32
    if len(signed_bytecode) < HEADER_SIZE + trailer_len:
        return False, "Binary too short to contain cryptographic signature trailer"

    payload = signed_bytecode[:-trailer_len]
    trailer = signed_bytecode[-trailer_len:]

    sig_magic, expected_digest = struct.unpack("<8s32s", trailer)
    if sig_magic != SIGNATURE_MAGIC:
        return False, f"Invalid signature trailer magic: {sig_magic!r}"

    # Verify CAP_SIGNATURE_VERIFIED capability flag
    caps = struct.unpack_from("<H", payload, 6)[0]
    if (caps & Capability.CAP_SIGNATURE_VERIFIED) == 0:
        return False, "Bytecode lacks CAP_SIGNATURE_VERIFIED capability flag"

    # Compute actual HMAC
    h = hmac.new(secret_key, payload, hashlib.sha256)
    actual_digest = h.digest()

    if not hmac.compare_digest(actual_digest, expected_digest):
        return False, "Cryptographic signature mismatch: bytecode tampered or invalid secret key"

    return True, "Valid signature"
