class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def find(parent, x):
            if parent[x] == x:
                return x
            parent[x] = find(parent, parent[x])
            return parent[x]

        def union(parent, x, y):
            root_x = find(parent, x)
            root_y = find(parent, y)
            if root_x != root_y:
                parent[root_x] = root_y

        n = len(points)
        edges = []  # List to store edges and their costs

        for i in range(n):
            for j in range(i + 1, n):
                xi, yi = points[i]
                xj, yj = points[j]
                cost = abs(xi - xj) + abs(yi - yj)
                edges.append((i, j, cost))

        # Sort edges by their cost in ascending order
        edges.sort(key=lambda x: x[2])

        parent = list(range(n))
        min_cost = 0
        num_edges = 0

        for edge in edges:
            i, j, cost = edge
            if find(parent, i) != find(parent, j):
                union(parent, i, j)
                min_cost += cost
                num_edges += 1

            # Early exit condition: If we have already added n-1 edges, we can stop
            if num_edges == n - 1:
                break

        return min_cost
