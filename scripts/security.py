"""Conservative credential marker detection; not a replacement for privacy review."""
import re

PATTERNS = [
    r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----',
    r'\bgh[pousr]_[A-Za-z0-9]{30,}\b',
    r'\bgithub_pat_[A-Za-z0-9_]{40,}\b',
    r'\bsk-(?:proj-)?[A-Za-z0-9_-]{32,}\b',
    r'\bAKIA[A-Z0-9]{16}\b',
    r'https?://[^\s<>"\']+[?&](?:X-Amz-Signature|X-Goog-Signature|access_token)=[^\s<>"\']+',
]


def contains_credential(text):
    return any(re.search(pattern,text) for pattern in PATTERNS)
