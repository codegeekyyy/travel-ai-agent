# demo code
import hashlib
import numpy as np


def fake_embedding(text: str) -> np.ndarray:
    """
    Temporary embedding function.
    Converts text → deterministic vector.
    (Used only for architecture, not intelligence)
    """
    hash_bytes = hashlib.sha256(text.encode()).digest()
    vector = np.frombuffer(hash_bytes, dtype=np.uint8).astype("float32")
    return vector
