class DisjointSet:
    rank = []
    parent = []

    def __init__(self, vertices):
        self.vertices = vertices
        self.rank = [0 for _ in range(vertices)]
        self.parent = [0 for _ in range(vertices)]

    def find_parent(self, item):
        if self.parent[item] == item:
            return item
        # Path compression
        self.parent[item] = self.find_parent(self.parent[item])
        return self.parent[item]

    # union by rank
    def union(self, first, second):
        first_parent = self.find_parent(first)
        second_parent = self.find_parent(second)

        if self.rank[first_parent] < self.rank[second_parent]:
            self.parent[first_parent] = second_parent
        elif self.rank[second_parent] < self.rank[first_parent]:
            self.parent[second_parent] = first
        else:
            self.parent[first_parent] = second_parent
            self.rank[second_parent] += 1
