from collections import deque

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        target_state = (1 << n) - 1  # All nodes visited state

        queue = deque([(i, 1 << i) for i in range(n)])  # Initialize the queue with starting nodes and their states
        visited = set([(i, 1 << i) for i in range(n)])  # Keep track of visited nodes and their states

        steps = 0  # Initialize the number of steps

        while queue:
            size = len(queue)
            for i in range(size):
                node, state = queue.popleft()

                if state == target_state:
                    return steps  # If all nodes are visited, return the number of steps

                for neighbor in graph[node]:
                    new_state = state | (1 << neighbor)  # Update the state to include the neighbor
                    if (neighbor, new_state) not in visited:
                        queue.append((neighbor, new_state))
                        visited.add((neighbor, new_state))

            steps += 1  # Increment the number of steps

        return -1  # If all nodes cannot be visited, return -1

# Example usage:
solution = Solution()
graph1 = [[1,2,3],[0],[0],[0]]
print(solution.shortestPathLength(graph1))  # Output: 4

graph2 = [[1],[0,2,4],[1,3,4],[2],[1,2]]
print(solution.shortestPathLength(graph2))  # Output: 4
