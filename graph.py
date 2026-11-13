# ASSESSMENT 3.4
# GRAPH - BASTATAS
# Name: Ian Alhjo R. Bastatas

from collections import deque


class Graph:
    def __init__(self):
        # Dictionary adjacency list preserves insertion order.
        self.adjacency = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency:
            self.adjacency[vertex] = []

    def add_edge(self, first, second):
        # Undirected edge: connect both directions.
        self.adjacency[first].append(second)
        self.adjacency[second].append(first)

    def bfs(self, start):
        """Breadth-First Search using a queue."""
        if start not in self.adjacency:
            return

        visited = {start}
        queue = deque([start])

        while queue:
            current = queue.popleft()
            print(current, end=" ")

            for neighbor in self.adjacency[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

    def dfs(self, start):
        """Depth-First Search using recursion."""
        if start not in self.adjacency:
            return

        visited = set()
        self._dfs_recursive(start, visited)

    def _dfs_recursive(self, vertex, visited):
        visited.add(vertex)
        print(vertex, end=" ")

        for neighbor in self.adjacency[vertex]:
            if neighbor not in visited:
                self._dfs_recursive(neighbor, visited)


def create_graph():
    """Create an undirected graph from the unique letters B, A, S, T."""
    graph = Graph()

    for vertex in ["B", "A", "S", "T"]:
        graph.add_vertex(vertex)

    graph.add_edge("B", "A")
    graph.add_edge("A", "S")
    graph.add_edge("S", "T")
    graph.add_edge("T", "B")

    return graph


def main():
    graph = create_graph()

    print("GRAPH - BASTATAS")
    print("----------------")

    print("BFS Traversal (start B): ", end="")
    graph.bfs("B")

    print("\nDFS Traversal (start B): ", end="")
    graph.dfs("B")

    print("\nProgram completed!")


if __name__ == "__main__":
    main()
