from src.domain.user_rules import validate_username
from src.repositories.user_repo import InMemoryUserRepo


class UsernameTakenError(ValueError):
    pass


class OnboardingService:
    def __init__(self, user_repo: InMemoryUserRepo) -> None:
        self.user_repo = user_repo

    def register(self, username: str) -> str:
        candidate = username.strip()
        if self.user_repo.exists(candidate):
            raise UsernameTakenError("username already exists")
        validated_username = validate_username(candidate)
        self.user_repo.add(validated_username)
        return validated_username
