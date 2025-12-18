from is_weather_question import is_weather_question

def test_weather_question_true():
    question = "What is the weather in Chennai?"
    assert is_weather_question(question) is True

def test_weather_question_false():
    question = "What is discussed in chapter 2 of the PDF?"
    assert is_weather_question(question) is False
