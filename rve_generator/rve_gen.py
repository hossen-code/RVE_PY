# -*- coding: utf-8 -*-
"""
Creating random micromechanical RVE of composites
author Hossein Ghayoor

"""
from rve_generator.point import Point
from rve_generator.utility import is_colliding, calculate_all_distances, sum_n_closest_point_distance, plot_all_points

if __name__ == "__main__":
    all_points = []
    point_collection = []
    for i in range(2000):
        new_point = Point()
        if not is_colliding(point_collection, new_point):
            point_collection.append(new_point)

    all_distances = calculate_all_distances(point_collection)
    three_closest_dist = sum_n_closest_point_distance(all_distances)

    plot_all_points(point_collection)
