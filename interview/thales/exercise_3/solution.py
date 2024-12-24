
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


def main():
    # Code that serves as the entry point of the program
    print("Hello, this is the main function!")

    points = np.array([[-11.95,  68.14,  52.96],
        [-44.68,  51.8 , -14.19],
        [  4.35,  77.51,  73.96],
        [-6.98,  33.09,  5.83],
        [ 16.44,  56.2 ,  53.39]])



    cluster_centers = {
        'Center1': [
            68.03,
            -77.24,
            23.5
        ],
        'Center2': [
            66.66,
            -22.67,
            -38.08
        ],
        'Center3': [
            35.01,
            -72.83,
            60.5
        ]
    }  


    centers  = cluster_points_chatGPT(points, cluster_centers)
    print(centers)



if __name__ == "__main__":
    main()



"""
Test 1:

Input : 
points = np.array([[ 18.08,  78.95, -12.73],
    [ 61.02,  34.75, -40.64],
    [-83.86, -27.62, -73.54],
    [ 78.07, -24.72, -54.4 ],
    [-2.01,  -92.49, -77.56],
    [ -25.87,  15.34,  -81.73],
    [ 81.98, -16 ,  89.27],
    [-45.11, -22.49,  44.12],
    [-35.62, -38.43, -73.62],
    [-87.98,  54.16, -94.34]])



cluster_centers = {
    'Center1': [
        68.03,
        -77.24,
        23.5
    ],
    'Center2': [
        66.66,
        -22.67,
        -38.08
    ],
    'Center3': [
        35.01,
        -72.83,
        60.5
    ]
}   

Expected output:
centers = {'Center1': [], 'Center2': [0, 1, 2, 3, 4, 5, 8, 9], 'Center3': [6, 7]}

Test 2:

points = np.array([[-11.95,  68.14,  52.96],
       [-44.68,  51.8 , -14.19],
       [  4.35,  77.51,  73.96],
       [-6.98,  33.09,  5.83],
       [ 16.44,  56.2 ,  53.39]])

cluster_centers = 
{
    'Center1': [
        -63.2,
        32.15,
        -22.58
    ],
    'Center2': [
        83.79,
        48.71,
        6.32
    ]
}

Expected output:
centers = {
    'Center1': [
        0,
        1,
        3
    ],
    'Center2': [
        2,
        4
    ]
}


test 3:

points = np.array([[-71.76, -36.28, -34.98],
       [0.5, 43.86, 51.17],
       [83.63, -91.69, -22.52],
       [32.41, -23.72, -57.4],
       [2.98, -46.07, 35.87],
       [78.47, -71.37, 81.04],
       [13.72, 81.15, -85.99],
       [9.26, -46.27, 37.41],
       [-89.8, -75.55, 33.54],
       [63.69, -76.08, 96.69],
       [-27.08, 11.32, -17.2]])

       
cluster_centers = 
{
    'Center1': [
        -43.97,
        55.37,
        9.15
    ],
    'Center2': [
        75.3,
        -18.25,
        16.04
    ],
    'Center3': [
        -32.18,
        -87.45,
        1.1
    ],
    'Center4': [
        -39.56,
        -13.19,
        -71.81
    ]
}

Expected output:
centers = 
{
    'Center1': [
        1,
        9
    ],
    'Center2': [
        2,
        5,
        8
    ],
    'Center3': [
        4,
        7
    ],
    'Center4': [
        0,
        3,
        6
    ]
}

"""