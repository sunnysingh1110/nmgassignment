#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys

def floyd_warshall(graph):
    # Number of vertices in the graph
    V = len(graph)
    
    # Initialize the distance matrix with initial values
    dist = [[float('inf')] * V for _ in range(V)]
    for i in range(V):
        for j in range(V):
            if i == j:
                dist[i][j] = 0
            elif graph[i][j] != 0:
                dist[i][j] = graph[i][j]
    
    # Calculate shortest paths
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][k] != float('inf') and dist[k][j] != float('inf'):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    return dist

# Example usage
if __name__ == "__main__":
    # Example graph represented as an adjacency matrix
    graph = [
        [0, 5, 0, 10],
        [0, 0, 3, 0],
        [0, 0, 0, 1],
        [0, 0, 0, 0]
    ]

    result = floyd_warshall(graph)
    
    # Print the shortest distances between all pairs of vertices
    for row in result:
        print(row)

