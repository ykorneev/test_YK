import requests
import json

def test_add_pet():
    BASE_URL = "https://petstore.swagger.io/v2/pet"

    new_pet = {
        "id": 9867543,
        "name": "Vitya",
        "status": "available"
    }


    response = requests.post(
        BASE_URL,
        headers={"Content-Type": "application/json"},
        data=json.dumps(new_pet)
    )

    assert response.status_code == 200, f"Expected status 200, got {response.status_code}"

    response_data = response.json()
    assert response_data["id"] == new_pet["id"], f"Expected id {new_pet['id']}, got {response_data['id']}"
    assert response_data["name"] == new_pet["name"], f"Expected name {new_pet['name']}, got {response_data['name']}"
    assert response_data["status"] == new_pet["status"], f"Expected status {new_pet['status']}, got {response_data['status']}"

