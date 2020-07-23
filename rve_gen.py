# -*- coding: utf-8 -*-
"""
Creating random micromechanical RVE of composites
author Hossein Ghayoor

"""

import random
import matplotlib.pyplot as plt
from scipy.spatial import distance
import scipy
import numpy as np


WIDTH = 10
HEIGHT = 10
CIRCLE_RADIUS = 0.5


class Point:
    """
    Center points of non-colliding circles
    #TODO: convert all the lists of points to NdArray for algebraic operations
    """
    def __init__(self):
        self.coordinates = np.random.rand(1, 2) * np.array([WIDTH, HEIGHT])
        
    def move(self):
        
        move_val = np.random.rand(1, 2)* np.array([3, 3]) # 3 is the move intensity
        self.coordinates += move_val
    
              

all_points = []

        
def _distance(point_1, point_2):
    
    dist = distance.euclidean(point_1.coordinates, point_2.coordinates)
    
    return dist

def colliding(points, new_point):
    radius = CIRCLE_RADIUS
    for point in points:
        if _distance(point, new_point) < 2*radius:
            return True
        
    return False

        
def show_points(points):
    all_xs, all_ys = [], []
    for point in points:
        all_xs.append(point.coordinates[0][0])
        all_ys.append(point.coordinates[0][1])
        
        
    plt.plot(all_xs, all_ys, "ro")
    plt.show()
    

def calculate_all_distances(points):
    # TODO: list comprehension to optimize the speed here
    all_distances = np.empty((0, len(points)), float)

    for point in points:
        one_point_to_rest = []
        for other_point in points:
            dist = _distance(point, other_point)
            one_point_to_rest.append(dist)

        all_distances = np.append(all_distances, np.array([one_point_to_rest]), axis=0)
            
    return all_distances  
        

def sum_n_closest_point_distance(distance_arrays, n_points: int = 3):
    # based on the result of this we find the secluded points to move them
    # towards their neighbors
    sum_n_close_points = []
    for dist_array in distance_arrays:
        close_point_ind = np.argpartition(dist_array, n_points)
        distance_sum = sum(dist_array[close_point_ind[:n_points]])
        sum_n_close_points.append(distance_sum)
        
    return sum_n_close_points
    

def move_points():
    pass


if __name__ == "__main__":
    point_collection = []
    for i in range(20):
        new_point = Point()
        if not colliding(point_collection, new_point):
            point_collection.append(new_point)

    all_distances = calculate_all_distances(point_collection)
    three_closest_dist = sum_n_closest_point_distance(all_distances)
    
    show_points(point_collection)
