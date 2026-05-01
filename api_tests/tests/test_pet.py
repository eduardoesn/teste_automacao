import pytest

from api_tests.services.petstore_api import PetstoreApi
from api_tests.utils.data_generator import pet_payload


@pytest.fixture
def api():
    return PetstoreApi()


def test_create_get_update_and_delete_pet(api):
    pet = pet_payload()

    create_response = api.create_pet(pet)
    assert create_response.status_code == 200
    assert create_response.json()["id"] == pet["id"]
    assert create_response.json()["status"] == "available"

    get_response = api.get_pet(pet["id"])
    assert get_response.status_code == 200
    assert get_response.json()["name"] == pet["name"]

    updated_pet = {**pet, "name": "updated-pet", "status": "sold"}
    update_response = api.update_pet(updated_pet)
    assert update_response.status_code == 200
    assert update_response.json()["status"] == "sold"

    delete_response = api.delete_pet(pet["id"])
    assert delete_response.status_code == 200

    not_found_response = api.get_pet(pet["id"])
    assert not_found_response.status_code == 404


def test_find_pets_by_status(api):
    response = api.find_pets_by_status("available")

    assert response.status_code == 200
    pets = response.json()
    assert isinstance(pets, list)
    assert all(pet["status"] == "available" for pet in pets[:10])
