import pytest

from src.api.onboarding_api import OnboardingAPI
from src.repositories.user_repo import InMemoryUserRepo
from src.services.onboarding_service import OnboardingService, UsernameTakenError


def build_api(existing_usernames: set[str] | None = None) -> tuple[OnboardingAPI, InMemoryUserRepo]:
    repo = InMemoryUserRepo(set() if existing_usernames is None else set(existing_usernames))
    service = OnboardingService(repo)
    return OnboardingAPI(service), repo


def test_spaces_and_hyphens_collapse_to_single_underscore() -> None:
    api, _ = build_api()

    response = api.register({"username": "  Team --- Lead  "})

    assert response == {"status": "ok", "username": "team_lead"}


def test_reserved_prefix_rejected_after_normalization() -> None:
    api, _ = build_api()

    with pytest.raises(ValueError, match="username is reserved"):
        api.register({"username": " Admin-Team "})

def test_duplicate_after_normalization() -> None:
    api, _ = build_api({"team_lead"})

    with pytest.raises(UsernameTakenError):
        api.register({"username": " Team---Lead "})


def test_invalid_characters_rejected() -> None:
    api, _ = build_api()

    with pytest.raises(ValueError, match="lowercase letters, numbers, and underscores"):
        api.register({"username": "bad$name"})


def test_length_checked_after_normalization() -> None:
    api, _ = build_api()

    with pytest.raises(ValueError, match="between 3 and 20 characters"):
        api.register({"username": " --AB-- "})
