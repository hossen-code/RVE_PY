
import matplotlib.pyplot as plt
from scipy.spatial import distance
import numpy as np

CIRCLE_RADIUS = 0.5


def two_point_distance(point_1, point_2):
    return distance.euclidean(point_1.coordinates, point_2.coordinates)


def is_colliding(points, new_point):
    radius = CIRCLE_RADIUS
    for point in points:
        if two_point_distance(point, new_point) < 2 * radius:
            return True

    return False


def plot_all_points(points):
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
            dist = two_point_distance(point, other_point)
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
