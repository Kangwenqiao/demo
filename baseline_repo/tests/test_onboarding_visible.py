from src.api.onboarding_api import OnboardingAPI
from src.repositories.user_repo import InMemoryUserRepo
from src.services.onboarding_service import OnboardingService


def build_api(existing_usernames: set[str] | None = None) -> tuple[OnboardingAPI, InMemoryUserRepo]:
    repo = InMemoryUserRepo(set() if existing_usernames is None else set(existing_usernames))
    service = OnboardingService(repo)
    return OnboardingAPI(service), repo


def test_registers_plain_username() -> None:
    api, repo = build_api()

    response = api.register({"username": "alice_01"})

    assert response == {"status": "ok", "username": "alice_01"}
    assert repo.list_usernames() == ["alice_01"]


def test_replaces_hyphenated_username_with_underscore() -> None:
    api, repo = build_api()

    response = api.register({"username": " Alice-Smith "})

    assert response == {"status": "ok", "username": "alice_smith"}
    assert repo.list_usernames() == ["alice_smith"]
