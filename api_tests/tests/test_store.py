import pytest

from api_tests.services.petstore_api import PetstoreApi
from api_tests.utils.data_generator import order_payload, pet_payload


@pytest.fixture
def api():
    return PetstoreApi()


@pytest.fixture
def created_pet(api):
    pet = pet_payload()
    response = api.create_pet(pet)
    assert response.status_code == 200
    yield response.json()
    api.delete_pet(pet["id"])


def test_create_get_and_delete_order(api, created_pet):
    order = order_payload(created_pet["id"])

    create_response = api.create_order(order)
    assert create_response.status_code == 200
    assert create_response.json()["petId"] == created_pet["id"]
    assert create_response.json()["status"] == "placed"

    get_response = api.get_order(order["id"])
    assert get_response.status_code == 200
    assert get_response.json()["id"] == order["id"]
    assert get_response.json()["complete"] is True

    delete_response = api.delete_order(order["id"])
    assert delete_response.status_code == 200

    not_found_response = api.get_order(order["id"])
    assert not_found_response.status_code == 404


def test_get_store_inventory(api):
    response = api.get_inventory()

    assert response.status_code == 200
    inventory = response.json()
    assert isinstance(inventory, dict)
    assert inventory
