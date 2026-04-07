import re

USERNAME_PATTERN = re.compile(r"^[a-z0-9_ -]+$")
RESERVED_USERNAMES = {"admin", "root", "system"}


def validate_username(username: str) -> str:
    normalized_username = username.strip().lower()
    if len(normalized_username) < 3 or len(normalized_username) > 20:
        raise ValueError("username must be between 3 and 20 characters")
    if not USERNAME_PATTERN.fullmatch(normalized_username):
        raise ValueError("username may only contain letters, numbers, spaces, hyphens, and underscores")
    if normalized_username in RESERVED_USERNAMES:
        raise ValueError("username is reserved")
    return normalized_username
