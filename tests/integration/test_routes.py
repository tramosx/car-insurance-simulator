def test_calculate_endpoint(client):
    payload = {
        "car": {
            "make": "Fiat",
            "model": "Uno",
            "year": 2012,
            "value": 30000.0
        },
        "insurance": {
            "deductible_percentage": 0.15,
            "broker_fee": 50.0
        }
    }

    response = client.post("/calculate", json=payload)
    assert response.status_code == 200

    data = response.json()
    assert data["calculated_premium"] > 0
    assert data["policy_limit"] > 0
    assert data["car"]["make"] == "Fiat"
