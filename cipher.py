import hashlib

def get_note_id(text: str, salt: str) -> str:
    return hashlib.sha256(
        text.encode("utf-8") + salt.encode("utf-8")
    ).hexdigest()