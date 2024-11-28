
import numpy as np

def cluster_points_chatGPT(points, cluster_centers):
    """
    Solution from chatGPT, wrong
    """
    
    # Initialize a dictionary to store points for each cluster
    clusters = {center: [] for center in cluster_centers}

    # Iterate over each point to compute its distance from the cluster centers
    for idx, point in enumerate(points):
        # Initialize the minimum distance and the cluster to be assigned to the point
        min_distance = float('inf')
        closest_center = None
        
        # Compute the distance of the point from each cluster center
        for center, center_coords in cluster_centers.items():
            distance = np.linalg.norm(np.array(center_coords) - np.array(point))  # Euclidean distance
            
            # Update the closest cluster center if the current one is closer
            if distance < min_distance:
                min_distance = distance
                closest_center = center
        
        # Add the point index to the corresponding cluster in the dictionary
        clusters[closest_center].append(idx)
    
    return clusters
