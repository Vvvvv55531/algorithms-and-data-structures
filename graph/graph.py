from collections import deque
from matrix import Matrix
from typing import Union
import pickle


class Graph:
    def __init__(self) -> None:
        self._matrix: Matrix = Matrix()
        self._vertex_list: list[str] = ["Vertexes:"]
        self._edges_list: list[list[str]] = []

    def add_vertex(self, vertex: str) -> None:
        if self._matrix.title_check(vertex):
            raise ValueError("Vertex already exists")

        self._matrix.add_title(vertex)
        self._vertex_list.append(vertex)

    def add_edge(self, vertex1: str, vertex2: str, weight: int) -> None:
        if weight < 1:
            raise TypeError("Incorrect weight")

        elif vertex1 == vertex2:
            raise TypeError("Incorrect vertexes")

        elif self._current_weight(vertex1, vertex2) != 0:
            raise TypeError("Edge already exists")

        elif self._matrix.title_check(vertex1) and self._matrix.title_check(vertex2):
            self._matrix.add_value(vertex1, vertex2, weight)
            vertexes: list[str] = [vertex1, vertex2]
            self._edges_list.append(vertexes)
            vertexes: list[str] = [vertex2, vertex1]
            self._edges_list.append(vertexes)
        else:
            raise ValueError("Vertex doesn't exist")

    def _current_state(self) -> list[list[Union[str, int]]]:
        if self._matrix.length_check():
            raise AttributeError("Graph is empty")

        return self._matrix.get_matrix()

    def _current_vertexes(self) -> list[str]:
        return self._vertex_list

    def _current_weight(self, vertex1: str, vertex2: str) -> str:
        if self._matrix.length_check():
            raise AttributeError("Graph is empty")

        elif self._matrix.title_check(vertex1) and self._matrix.title_check(vertex2):
            i: int = self._vertex_list.index(vertex1)
            j: int = self._vertex_list.index(vertex2)
            return self._matrix[i][j]
        else:
            raise ValueError("Vertex doesn't exist")

    def _current_edges(self) -> None:
        for vertexes in self._edges_list:
            for i in range(1):
                weight: str = self._current_weight(vertexes[i - 1], vertexes[i])
                print(f"(Vertex1: {vertexes[i - 1]}, "
                      f"Vertex2: {vertexes[i]}, "
                      f"Weight: {weight})")

    def print_graph(self) -> None:
        if self._matrix.length_check():
            raise AttributeError("Graph is empty")

        print("Current matrix:")
        self._matrix.print()

        print("\nCurrent vertexes:")
        print(self._current_vertexes())

        print("\nCurrent edges:")
        self._current_edges()
        print()

    def clean_graph(self) -> None:
        if self._matrix.length_check():
            raise AttributeError("Graph is empty")

        self._matrix.clean()
        self._vertex_list: list[str] = ["Vertexes:"]
        self._edges_list: list[list[str]] = []

    def bsf(self, start: str) -> None:
        visited: set = set()
        queue: deque = deque([start])

        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                print(vertex)
                visited.add(vertex)
                for edge in range(len(self._edges_list)):
                    if vertex == self._edges_list[edge][0]:
                        neighbor = self._edges_list[edge][1]
                        if neighbor not in visited:
                            queue.append(neighbor)

    def save(self) -> None:
        self._matrix.save()
        save_graph_1: list[str] = self._vertex_list
        save_graph_2: list[list[str]] = self._edges_list

        with open("graph_save_1.pkl", "wb") as file1:
            pickle.dump(save_graph_1, file1)

        with open("graph_save_2.pkl", "wb") as file2:
            pickle.dump(save_graph_2, file2)

    def load(self) -> None:
        self.clean_graph()
        self._matrix.load()

        with open("graph_save_1.pkl", "rb") as file1:
            load_graph_1: list[str] = pickle.load(file1)

        with open("graph_save_2.pkl", "rb") as file2:
            load_graph_2: list[list[str]] = pickle.load(file2)

        self._vertex_list = load_graph_1
        self._edges_list = load_graph_2

    """def bellman_ford(self, start: str, end: str) -> None:
            edges: list[list[str]] = self._edges_list

            for edge in range(len(edges)):
                edges[edge].append(self._current_weight(edges[edge][0], edges[edge][1]))

            del edges[1::2]
            print(edges)

            next_edge: list = []
            shadow_start: str = start
            while start != end or shadow_start != end:
                for edge in range(len(edges)):
                    if start == edges[edge][0] or start == edges[edge][1]:
                        next_edge.append(edges[edge])

                        while len(next_edge) != 1:
                            for cost in range(1, len(next_edge)):
                                if next_edge[cost][2] > next_edge[cost - 1][2]:
                                    del next_edge[cost]
                                else:
                                    del next_edge[cost - 1]
                        start = next_edge[0][1]
                        shadow_start = next_edge[0][0]
            print(shadow_start, start)"""
