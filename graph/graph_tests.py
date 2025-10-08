import unittest
from graph import Graph


class TestGraph(unittest.TestCase):

    def test_add_vertex(self):
        graph: Graph = Graph()
        graph.add_vertex("v1")
        graph.add_vertex("v2")
        expected_str: list[str] = ["Vertexes:", "v1", "v2"]
        self.assertEqual(graph._current_vertexes(), expected_str)

    def test_add_edge(self):
        graph: Graph = Graph()
        graph.add_vertex("v1")
        graph.add_vertex("v2")
        graph.add_edge("v1", "v2", 1234)
        expected_value: int = 1234
        self.assertEqual(graph._current_weight("v1", "v2"), expected_value)

    def test_current_vertexes(self):
        graph: Graph = Graph()
        graph.add_vertex("v3")
        expected_str: list[str] = ["Vertexes:", "v3"]
        self.assertEqual(graph._current_vertexes(), expected_str)

    def test_current_weight(self):
        graph: Graph = Graph()
        self.assertRaises(AttributeError, graph._current_weight, "v1", "v2")
        graph: Graph = Graph()
        graph.add_vertex("v1")
        graph.add_vertex("v3")
        graph.add_edge("v1", "v3", 123)
        expected_value: int = 123
        self.assertEqual(graph._current_weight("v1", "v3"), expected_value)

    def test_clean(self):
        graph: Graph = Graph()
        graph.add_vertex("v1")
        graph.add_vertex("v2")
        graph.add_edge("v1", "v2", 1234)
        graph.clean_graph()
        expected_str: list[str] = ["Vertexes:"]
        self.assertEqual(graph._current_vertexes(), expected_str)
        self.assertRaises(AttributeError, graph.add_edge, "v1", "v2", 1234)
