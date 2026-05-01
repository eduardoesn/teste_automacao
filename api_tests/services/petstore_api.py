import requests


class PetstoreApi:
    def __init__(self, base_url: str = "https://petstore.swagger.io/v2", timeout: int = 20):
        self.base_url = base_url
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update({"Content-Type": "application/json"})

    def create_user(self, payload: dict) -> requests.Response:
        return self.session.post(f"{self.base_url}/user", json=payload, timeout=self.timeout)

    def get_user(self, username: str) -> requests.Response:
        return self.session.get(f"{self.base_url}/user/{username}", timeout=self.timeout)

    def update_user(self, username: str, payload: dict) -> requests.Response:
        return self.session.put(f"{self.base_url}/user/{username}", json=payload, timeout=self.timeout)

    def delete_user(self, username: str) -> requests.Response:
        return self.session.delete(f"{self.base_url}/user/{username}", timeout=self.timeout)

    def create_pet(self, payload: dict) -> requests.Response:
        return self.session.post(f"{self.base_url}/pet", json=payload, timeout=self.timeout)

    def get_pet(self, pet_id: int) -> requests.Response:
        return self.session.get(f"{self.base_url}/pet/{pet_id}", timeout=self.timeout)

    def update_pet(self, payload: dict) -> requests.Response:
        return self.session.put(f"{self.base_url}/pet", json=payload, timeout=self.timeout)

    def delete_pet(self, pet_id: int) -> requests.Response:
        return self.session.delete(f"{self.base_url}/pet/{pet_id}", timeout=self.timeout)

    def find_pets_by_status(self, status: str) -> requests.Response:
        return self.session.get(
            f"{self.base_url}/pet/findByStatus",
            params={"status": status},
            timeout=self.timeout,
        )

    def create_order(self, payload: dict) -> requests.Response:
        return self.session.post(f"{self.base_url}/store/order", json=payload, timeout=self.timeout)

    def get_order(self, order_id: int) -> requests.Response:
        return self.session.get(f"{self.base_url}/store/order/{order_id}", timeout=self.timeout)

    def delete_order(self, order_id: int) -> requests.Response:
        return self.session.delete(f"{self.base_url}/store/order/{order_id}", timeout=self.timeout)

    def get_inventory(self) -> requests.Response:
        return self.session.get(f"{self.base_url}/store/inventory", timeout=self.timeout)
