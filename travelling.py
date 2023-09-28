#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import itertools
import sys

def tsp_dynamic_programming(graph):
    num_cities = len(graph)
    all_cities = set(range(num_cities))
    
    # Initialize the memoization table
    memo = {}
    
    # Function to compute the optimal tour length starting from city `start` and visiting all cities in `to_visit`
    def tsp_helper(start, to_visit):
        if not to_visit:
            return graph[start][0]  # Return to the starting city to complete the tour
        if (start, to_visit) in memo:
            return memo[(start, to_visit)]
        
        min_distance = sys.maxsize
        for city in to_visit:
            remaining_cities = to_visit - {city}
            distance = graph[start][city] + tsp_helper(city, remaining_cities)
            if distance < min_distance:
                min_distance = distance
        
        memo[(start, to_visit)] = min_distance
        return min_distance
    
    # Start the dynamic programming process from city 0
    optimal_tour_length = tsp_helper(0, all_cities - {0})
    
    # Reconstruct the optimal tour
    tour = [0]  # Start from city 0
    current_city = 0
    remaining_cities = all_cities - {0}
    
    while remaining_cities:
        next_city = min(remaining_cities, key=lambda city: graph[current_city][city])
        tour.append(next_city)
        current_city = next_city
        remaining_cities -= {next_city}
    
    tour.append(0)  # Return to the starting city to complete the tour
    
    return optimal_tour_length, tour

# Example usage
if __name__ == "__main__":
    # Example graph represented as an adjacency matrix
    graph = [
        [0, 29, 20, 21],
        [29, 0, 15, 18],
        [20, 15, 0, 22],
        [21, 18, 22, 0]
    ]

    optimal_length, optimal_tour = tsp_dynamic_programming(graph)
    print("Optimal Tour Length:", optimal_length)
    print("Optimal Tour Route:", optimal_tour)

