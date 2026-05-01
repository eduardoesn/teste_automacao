from datetime import datetime, timezone
from uuid import uuid4


def unique_id() -> int:
    return int(datetime.now(timezone.utc).timestamp() * 1000)


def unique_text(prefix: str) -> str:
    return f"{prefix}-{uuid4().hex[:8]}"


def user_payload() -> dict:
    username = unique_text("qa-user")
    return {
        "id": unique_id(),
        "username": username,
        "firstName": "QA",
        "lastName": "Automation",
        "email": f"{username}@example.com",
        "password": "Password123",
        "phone": "11999999999",
        "userStatus": 1,
    }


def pet_payload(status: str = "available") -> dict:
    return {
        "id": unique_id(),
        "category": {"id": 1, "name": "dogs"},
        "name": unique_text("pet"),
        "photoUrls": ["https://example.com/pet.jpg"],
        "tags": [{"id": 1, "name": "automation"}],
        "status": status,
    }


def order_payload(pet_id: int) -> dict:
    return {
        "id": unique_id(),
        "petId": pet_id,
        "quantity": 1,
        "shipDate": datetime.now(timezone.utc).isoformat(),
        "status": "placed",
        "complete": True,
    }
