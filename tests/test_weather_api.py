from weather import fetch_weather

def test_fetch_weather_success(mocker):
    mock_response = {
        "weather": [{"description": "clear sky"}],
        "main": {"temp": 30, "humidity": 60}
    }

    mocker.patch(
        "weather.requests.get",
        return_value=mocker.Mock(
            status_code=200,
            json=lambda: mock_response,
            raise_for_status=lambda: None
        )
    )

    data = fetch_weather("Chennai")
    assert data["main"]["temp"] == 30
    assert data["weather"][0]["description"] == "clear sky"
