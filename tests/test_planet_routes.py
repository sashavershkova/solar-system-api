def test_get_all_planets_with_no_records(client):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

def test_get_one_planet(client, two_saved_planets):
    # Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "Pluto",
        "description": "A dwarf planet in the Kuiper Belt, formerly classified as the ninth planet. It has a rocky and icy surface with a thin atmosphere of nitrogen, methane, and carbon monoxide.",
        "distance_from_sun_mm_km": 5906,
        "moons": []
    }

def test_get_one_planet_not_found(client):
    # Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert response_body == {"message": "This Planet with id 1 is not found"}

def test_get_all_planets_with_records(client, two_saved_planets):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert len(response_body) == 2
    assert response_body == [
        {
            "id": 1,
            "name": "Pluto",
            "description": "A dwarf planet in the Kuiper Belt, formerly classified as the ninth planet. It has a rocky and icy surface with a thin atmosphere of nitrogen, methane, and carbon monoxide.",
            "distance_from_sun_mm_km": 5906,
            "moons": []
        },
        {
            "id": 2,
            "name": "Saturn",
            "description": "A gas giant, the sixth planet from the Sun. Known for its spectacular ring system, composed mostly of ice particles, rocky debris, and dust.",
            "distance_from_sun_mm_km": 1429,
            "moons": []
        }
    ]

def test_post_a_planet(client):
    # Act
    request_body = {"name": "Kelsey", "description": "beautiful", "distance_from_sun_mm_km": 100}
    response = client.post("/planets", json=request_body)
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert len(response_body) == 5
    assert response_body == {"id": 1, "name": "Kelsey", "description": "beautiful", "distance_from_sun_mm_km": 100, "moons": []}