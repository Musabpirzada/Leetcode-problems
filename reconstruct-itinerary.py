#using of DFS
from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Create a graph represented as a dictionary where keys are departure airports
        # and values are lists of arrival airports in lexical order.
        graph = defaultdict(list)
        for from_airport, to_airport in tickets:
            graph[from_airport].append(to_airport)

        # Sort the destinations for each departure airport in reverse order.
        for key in graph.keys():
            graph[key].sort(reverse=True)

        # Initialize an empty list to store the itinerary.
        itinerary = []

        def dfs(node):
            # Visit all neighbors (arrival airports) of the current node (departure airport).
            while graph[node]:
                neighbor = graph[node].pop()
                dfs(neighbor)
            # Append the current node to the beginning of the itinerary.
            itinerary.append(node)

        # Start the DFS from the "JFK" airport.
        dfs("JFK")

        # Reverse the itinerary to get the correct order.
        return itinerary[::-1]
