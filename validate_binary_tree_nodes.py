from collections import defaultdict

class Solution:
    def validateBinaryTreeNodes(self, n, leftChild, rightChild):
        graph = defaultdict(list)
        indegree = [0] * n

        for i in range(n):
            left, right = leftChild[i], rightChild[i]
            if left != -1:
                graph[i].append(left)
                indegree[left] += 1
            if right != -1:
                graph[i].append(right)
                indegree[right] += 1

        root_count = 0
        root = -1
        for i in range(n):
            if indegree[i] == 0:
                root_count += 1
                root = i

        if root_count != 1:
            return False

        visited = set()

        def dfs(node):
            if node in visited:
                return False
            visited.add(node)
            for child in graph[node]:
                if not dfs(child):
                    return False
            return True

        if not dfs(root):
            return False

        return len(visited) == n

# Example usage:
sol = Solution()
print(sol.validateBinaryTreeNodes(4, [3, -1, 1, -1], [-1, -1, 0, -1]))  # Output: True
