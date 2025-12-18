def is_weather_question(question: str) -> bool:
    """
    Returns True if the question is related to weather based on keywords.
    """
    weather_keywords = {
        "weather",
        "temperature",
        "temp",
        "rain",
        "rainfall",
        "snow",
        "climate",
        "forecast",
        "humidity",
        "wind",
        "windy",
        "storm",
        "sunny",
        "cloudy",
        "clouds",
        "heat",
        "cold",
        "hot",
        "cold",
        "drizzle",
        "thunder",
        "thunderstorm",
        "cyclone",
        "fog",
        "mist"
    }

    question_lower = question.lower()

    return any(keyword in question_lower for keyword in weather_keywords)
