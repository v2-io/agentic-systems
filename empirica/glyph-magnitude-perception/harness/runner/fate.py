"""Fated randomness (vivarium convention; DESIGN-scale-up addenda, Joseph 2026-08-25).

Every stochastic choice derives its seed from a hash of the root object it concerns:
    seed = H(protocol_version || purpose_tag || canonical(root_object))
Purpose tags give domain separation; the protocol version inside the hash makes
re-fating an explicit, versioned act. Canonicalization: JSON with sorted keys,
NFC-normalized strings, no whitespace; glyphs are additionally serialized as
explicit codepoint lists where they are the object (see canon()).
"""
import hashlib, json, random, unicodedata

def _nfc(o):
    if isinstance(o, str):
        return unicodedata.normalize("NFC", o)
    if isinstance(o, list):
        return [_nfc(x) for x in o]
    if isinstance(o, tuple):
        return [_nfc(x) for x in o]
    if isinstance(o, dict):
        return {_nfc(k): _nfc(v) for k, v in o.items()}
    return o

def canon(obj) -> str:
    return json.dumps(_nfc(obj), sort_keys=True, ensure_ascii=True, separators=(",", ":"))

def digest(obj) -> str:
    return hashlib.sha256(canon(obj).encode()).hexdigest()

def seed(protocol_version: str, purpose: str, obj) -> int:
    h = hashlib.sha256(f"{protocol_version}||{purpose}||{canon(obj)}".encode()).hexdigest()
    return int(h[:16], 16)

def rng(protocol_version: str, purpose: str, obj) -> random.Random:
    return random.Random(seed(protocol_version, purpose, obj))

def cps(s: str):
    return [f"U+{ord(c):04X}" for c in s]
