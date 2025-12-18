from rag_pdf import query_pdf
from weather import fetch_weather
from is_weather_question import is_weather_question

# --- Node class ---
class Node:
    def __init__(self, name, func, inputs=None, outputs=None):
        self.name = name
        self.func = func
        self.inputs = inputs or []
        self.outputs = outputs or []

# --- Graph class with conditional edges ---
class Graph:
    def __init__(self):
        self.nodes = {}
        self.edges = {}  # node_name -> list of (next_node_name, condition_func)

    def add_node(self, node):
        self.nodes[node.name] = node

    def add_edge(self, from_node, to_node, condition=None):
        if from_node not in self.edges:
            self.edges[from_node] = []
        self.edges[from_node].append((to_node, condition))

    def run(self, inputs):
        current_node_name = list(self.nodes.keys())[0]  # start from first added node
        state = inputs
        visited_nodes = set()

        while current_node_name:
            if current_node_name in visited_nodes:
                break  # prevent infinite loops
            visited_nodes.add(current_node_name)

            node = self.nodes[current_node_name]
            result = node.func(state)
            state.update(result)

            # Determine next node based on conditional edges
            next_node_name = None
            for next_node, condition in self.edges.get(current_node_name, []):
                if condition is None or condition(result):
                    next_node_name = next_node
                    break

            current_node_name = next_node_name

        return state

# --- Node 1: Weather check ---
def classify_weather_node(inputs):
    question = inputs["question"]
    return {"is_weather": is_weather_question(question)}

weather_node = Node(
    name="WeatherClassifier",
    func=classify_weather_node,
    inputs=["question"],
    outputs=["is_weather"]
)

# --- Node 2: PDF RAG ---
def pdf_rag_node(inputs):
    pdf_path = inputs["pdf"]
    question = inputs["question"]
    return {"answer": query_pdf(pdf_path, question)}

pdf_node = Node(
    name="PDFRAG",
    func=pdf_rag_node,
    inputs=["pdf", "question"],
    outputs=["answer"]
)

# --- Node 3: Weather API ---
def weather_api_node(inputs):
    question = inputs["question"]
    city = question.split()[-1]  # naive city extraction
    try:
        data = fetch_weather(city)
        description = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        return {"answer": f"Weather in {city}:\nDescription: {description}\nTemperature: {temp}°C\nHumidity: {humidity}%"}
    except Exception as e:
        return {"answer": f"Weather API error: {str(e)}"}

weather_api = Node(
    name="WeatherAPI",
    func=weather_api_node,
    inputs=["question"],
    outputs=["answer"]
)

# --- Build the graph ---
graph = Graph()
graph.add_node(weather_node)
graph.add_node(pdf_node)
graph.add_node(weather_api)

# Conditional edges
graph.add_edge("WeatherClassifier", "PDFRAG", condition=lambda output: not output["is_weather"])
graph.add_edge("WeatherClassifier", "WeatherAPI", condition=lambda output: output["is_weather"])

# --- Run wrapper ---
def process_input(pdf, question):
    outputs = graph.run({"pdf": pdf.name, "question": question})
    return outputs["answer"]
