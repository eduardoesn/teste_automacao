import pytest

from api_tests.services.petstore_api import PetstoreApi
from api_tests.utils.data_generator import user_payload


@pytest.fixture
def api():
    return PetstoreApi()


def test_create_get_update_and_delete_user(api):
    user = user_payload()

    create_response = api.create_user(user)
    assert create_response.status_code == 200
    assert create_response.json()["message"] == str(user["id"])

    get_response = api.get_user(user["username"])
    assert get_response.status_code == 200
    assert get_response.json()["username"] == user["username"]
    assert get_response.json()["email"] == user["email"]

    updated_user = {**user, "firstName": "Quality", "phone": "11888888888"}
    update_response = api.update_user(user["username"], updated_user)
    assert update_response.status_code == 200

    updated_response = api.get_user(user["username"])
    assert updated_response.status_code == 200
    assert updated_response.json()["firstName"] == "Quality"
    assert updated_response.json()["phone"] == "11888888888"

    delete_response = api.delete_user(user["username"])
    assert delete_response.status_code == 200

    not_found_response = api.get_user(user["username"])
    assert not_found_response.status_code == 404
