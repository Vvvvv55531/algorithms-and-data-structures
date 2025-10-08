from dataclasses import dataclass
from graph import Graph

if __name__ == "__main__":
    @dataclass
    class Vertex:
        name: str

        def __str__(self) -> str:
            return f"Vertex({self.name})"

        def get_vertex(self) -> str:
            return self.name


    city_list: list[Vertex] = [Vertex("v1"), Vertex("v2"),
                               Vertex("v3"), Vertex("v4"),
                               Vertex("v5"), Vertex("v6"),
                               Vertex("v7"), Vertex("v8"),
                               Vertex("v9"), Vertex("v10"),
                               Vertex("v11"), Vertex("v12"),
                               Vertex("v13")]

    graph: Graph = Graph()

    for it in city_list:
        graph.add_vertex(it.get_vertex())

    graph.add_edge("v1", "v11", 100)
    graph.add_edge("v11", "v12", 399)
    graph.add_edge("v2", "v12", 237)
    graph.add_edge("v7", "v12", 41)
    graph.add_edge("v4", "v5", 20)
    graph.add_edge("v7", "v4", 23)
    graph.add_edge("v7", "v10", 1001)
    graph.add_edge("v10", "v12", 4002)

    graph.print_graph()

    print("BSF_Search:")
    graph.bsf("v1")

    print("\nSave and Load:")
    graph.save()
    graph.load()
    graph.print_graph()

    """print("\nBellman_Ford_Algorithm:")
        graph.bellman_ford("v12", "v10")"""
