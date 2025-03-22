from collections import defaultdict

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        # dfs function to traverse the graph and return the number
        # of nodes (vertex_count) and number of edges (edge_count) in the component.
        def dfs(vertex: int) -> (int, int):
            visited[vertex] = True
            vertex_count, edge_count = 1, len(graph[vertex])  # Initialize counts with current node counts
            for neighbor in graph[vertex]:
                if not visited[neighbor]:
                    additional_vertices, additional_edges = dfs(neighbor)
                    vertex_count += additional_vertices
                    edge_count += additional_edges
            return vertex_count, edge_count

        # build the graph from the edges list
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
          
        visited = [False] * n  # keep track of visited nodes
        complete_components_count = 0  # counter for complete components
      
        # check each node; if it's not visited, perform dfs from that node
        for i in range(n):
            if not visited[i]:
                vertex_count, edge_count = dfs(i)
                # In a complete graph AKA clique, the number of edges is vertex_count * (vertex_count - 1) / 2
                # We multiply by 2 to compare with the undirected edge count (each edge counted twice)
                if vertex_count * (vertex_count - 1) == edge_count:
                    complete_components_count += 1
                  
        return complete_components_count