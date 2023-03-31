import numpy as np
import open3d as o3d


def generate_rectangle(width=10, height=5, depth=50, num_points=10000):
    """
    generates point cloud in the shape of rectangle with given width, height and depth

    :param width: (int) width (x) of rectangle
    :param height: (int) height (y) of rectangle
    :param depth: (int) depth (z) of rectangle
    :param num_points: (int) how many points in the point cloud - determines how dense it is
    :return: (ndarray of shape N,3) point cloud representing rectangle
    """

    x = np.random.uniform(low=0, high=width, size=(num_points,))
    y = np.random.uniform(low=0, high=height, size=(num_points,))
    z = np.random.uniform(low=0, high=depth, size=(num_points,))

    point_cloud = np.vstack([x, y, z]).T

    return point_cloud


def generate_sphere(radius=2, num_points=1000):
    """
    generates sphere of given radius

    :param radius: (int) radius of sphere
    :param num_points: (int) how many points in the point cloud - determines how dense it is
    :return: (ndarray of shape N,3) point cloud representing sphere
    """

    phi = np.random.uniform(low=0, high=np.pi, size=(num_points,))
    theta = np.random.uniform(low=0, high=2*np.pi, size=(num_points,))

    x = radius * np.sin(phi) * np.cos(theta)
    y = radius * np.sin(phi) * np.sin(theta)
    z = radius * np.cos(phi)
    point_cloud = np.vstack([x, y, z]).T

    return point_cloud


def generate_ellipse(width=2, height=10, depth=60, num_points=100):
    """
    generates sphere of given radius

    :param width: (int) width (x) of ellipse
    :param height: (int) height (y) of ellipse
    :param depth: (int) depth (z) of ellipse
    :param num_points: (int) how many points in the point cloud - determines how dense it is
    :return: (ndarray of shape N,3) point cloud representing sphere
    """

    phi = np.random.uniform(low=0, high=np.pi, size=(num_points,))
    theta = np.random.uniform(low=0, high=2*np.pi, size=(num_points,))

    x = width * np.outer(np.sin(theta), np.cos(phi))
    y = height * np.outer(np.sin(theta), np.sin(phi))
    z = depth * np.outer(np.cos(theta), np.ones_like(phi))

    point_cloud = np.column_stack((x.flatten(), y.flatten(), z.flatten()))

    return point_cloud


def generate_shape(shape, num_points=10000):

    if shape == 'rectangle':
        width = np.random.randint(low=1, high=10000)
        height = np.random.randint(low=1, high=10000)
        depth = np.random.randint(low=1, high=10000)
        point_cloud = generate_rectangle(width=width, height=height, depth=depth, num_points=num_points)

    elif shape=='cube':
        length = np.random.randint(low=1, high=10000)
        point_cloud = generate_rectangle(width=length, height=length, depth=length, num_points=num_points)
    elif shape == 'sphere':
        radius = np.random.randint(low=1, high=100)
        point_cloud = generate_sphere(radius=radius, num_points=num_points)

        #point_cloud[:,0] *= 2
        #point_cloud[:, 0] *= 5
        #point_cloud[:, 0] *= 3

    elif shape == 'ellipse':
        width = np.random.randint(low=1, high=10000)
        height = np.random.randint(low=1, high=10000)
        depth = np.random.randint(low=1, high=10000)
        point_cloud = generate_ellipse(width=width, height=height, depth=depth)
    else:
        return None

    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(point_cloud)
    o3d.visualization.draw_geometries([pcd])


def main():
    shape = 'sphere'
    generate_shape(shape)


if __name__=='__main__':
    main()