from collections import deque
from typing import List

"""
1. https://leetcode.com/problems/course-schedule/description/
2. https://leetcode.com/problems/course-schedule-ii/description/
3. https://leetcode.com/problems/course-schedule-iii/description/
"""


class Solution:
    def canFinish(self, num_courses: int, prerequisites: List[List[int]]) -> bool:
        return self.topo_sort(num_courses, prerequisites)

    def topo_sort(self, num_courses: int, prerequisites: list) -> bool:
        # create graph as adj list
        adj_list = []
        for _ in range(num_courses):
            adj_list.append([])
        # add node to graph
        for edge in prerequisites:
            adj_list[edge[0]].append(edge[1])
        # count indegree
        in_degree = [0] * num_courses
        for node in range(num_courses):
            for nbr in adj_list[node]:
                in_degree[nbr] += 1
        # add nodes in queue who has indegree equal to zero
        queue = deque()
        for index, value in enumerate(in_degree):
            if value == 0:
                queue.append(index)
        # BFS based on indegree of nodes
        toposort = [0] * num_courses
        index = 0
        count = 0
        while queue:
            node = queue.popleft()
            toposort[index] = node
            count += 1
            index += 1
            for nbr in adj_list[node]:
                in_degree[nbr] -= 1
                if in_degree[nbr] == 0:
                    queue.append(nbr)
        return count == num_courses
