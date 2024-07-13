class Graph:
    rank = []
    parent = []

    def __init__(self, vertices):
        self.vertices = vertices
        self.rank = [0 for _ in range(vertices)]
        self.parent = [i for i in range(vertices)]
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def find_parent(self, number):
        if self.parent[number] == number:
            return number
        return self.find_parent(self.parent[number])

    def union(self, num1, num2):
        parent1 = self.find_parent(num1)
        parent2 = self.find_parent(num2)

        if self.rank[parent1] < self.rank[parent2]:
            self.parent[parent1] = parent2
        elif self.rank[parent2] < self.rank[parent1]:
            self.parent[parent2] = parent1
        else:
            self.parent[parent1] = parent2
            self.rank[parent2] += 1

    def kruskal(self):
        result = []
        i, e = 0, 0

        self.graph = sorted(self.graph, key=lambda item: item[2])

        while e < self.vertices - 1:
            u, v, w = self.graph[i]
            i += 1
            x = self.find_parent(u)
            y = self.find_parent(v)

            if x != y:
                e += 1
                result.append([u, v, w])
                self.union(x, y)
        return result


class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:

        g = Graph(len(points))

        for i in range(len(points)):
            p1 = points[i]
            for j in range(i + 1, len(points)):
                p2 = points[j]
                distance = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
                g.add_edge(i, j, distance)

        mst = g.kruskal()
        total_cost = sum(edge[2] for edge in mst)

        return total_cost
