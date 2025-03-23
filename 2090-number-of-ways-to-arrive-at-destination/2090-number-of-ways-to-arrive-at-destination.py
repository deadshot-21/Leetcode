from math import inf
from typing import List

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        # Constants for infinity and modulus
        INF = inf
        MOD = 10 ** 9 + 7
      
        # Initialize the graph with infinite weights
        graph = [[INF] * n for _ in range(n)]
      
        # Populate graph with road travel times
        for u, v, time in roads:
            graph[u][v] = time
            graph[v][u] = time
      
        # Set the distance to the starting node 0 to 0
        graph[0][0] = 0
      
        # Initialize distance and ways arrays with infinite distance and zero ways
        distance = [INF] * n
        ways = [0] * n
      
        # Start with the distance to node 0 to be 0 and the number of ways to 1
        distance[0] = 0
        ways[0] = 1
      
        # Initialize visited array to track visited nodes
        visited = [False] * n
      
        # Perform Dijkstra's algorithm to find shortest paths
        for _ in range(n):
            # Find the unvisited node with the smallest distance
            current_node = -1
            for i in range(n):
                if not visited[i] and (current_node == -1 or distance[i] < distance[current_node]):
                    current_node = i
          
            # Mark this node as visited
            visited[current_node] = True
          
            # Update the distances and ways for neighboring nodes
            for neighbor in range(n):
                if neighbor == current_node:
                    continue
                new_distance = distance[current_node] + graph[current_node][neighbor]
              
                # If a shorter path is found, update the distance and ways
                if distance[neighbor] > new_distance:
                    distance[neighbor] = new_distance
                    ways[neighbor] = ways[current_node]
                # If another shortest path is found, increment the ways
                elif distance[neighbor] == new_distance:
                    ways[neighbor] += ways[current_node]
      
        # Return the number of shortest ways to the last node modulo MOD
        return ways[n - 1] % MOD