from flow import graph

def test_graph_routes_to_weather(mocker):
    mocker.patch("flow.fetch_weather", return_value={
        "weather": [{"description": "sunny"}],
        "main": {"temp": 28, "humidity": 50}
    })

    result = graph.run({"question": "weather in Delhi", "pdf": None})
    assert "Weather in" in result["answer"]

def test_graph_routes_to_pdf(mocker):
    mocker.patch("flow.query_pdf", return_value="PDF answer")

    result = graph.run({"question": "Explain chapter 1", "pdf": "dummy.pdf"})
    assert result["answer"] == "PDF answer"
