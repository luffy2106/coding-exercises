# K means
#
# Write a k-means function that takes data points and a number of centroids K and return the centroids. Data points belong to an n dimensional space (arbitrary n).
#
# Initialization: initialize the K centroids 
# Iterate the two following steps until a certain criterion is met
#    Assignment: Assign each point to the closest centroid
#    Update: update the centroids to be the average of all the points that were assigned to it.

from typing import List
import random
def calculate_centroid(graph : List, k : int, n : int):
    # graph = [(x1,y1,... ), (x2,y2,...) ...]

    list_centroid = []
    
    for x in range(k):
        centroid_x = []
        for i in range(n): 
            min_x_i = min([element[i] for element in graph])
            max_x_i = max([element[i] for element in graph])
            centroid_i = random.uniform(min_x_i, max_x_i)
            centroid_x.append(centroid_i)
        list_centroid.append(centroid_x)


    





    return