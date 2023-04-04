
import open3d as o3d
from generate_pc_data import generate_shape
import copy
import numpy as np


def draw_registration_result(source, target):
    source_temp = copy.deepcopy(source)
    target_temp = copy.deepcopy(target)
    source_temp.paint_uniform_color([1, 0.706, 0])
    target_temp.paint_uniform_color([0, 0.651, 0.929])
    #source_temp.transform(transformation)
    o3d.visualization.draw_geometries([source_temp, target_temp],
                                      zoom=0.4459,
                                      front=[0.9288, -0.2951, -0.2242],
                                      lookat=[1.6784, 2.0612, 1.4451],
                                      up=[-0.3402, -0.9189, -0.1996])


def main(method='generalized_ICP'):
    source = generate_shape(shape='rectangle')
    target = copy.deepcopy(source).translate((500, 500, 500))

    # Compute covariance matrices for source and target point clouds
    source.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.1, max_nn=30))
    o3d.geometry.PointCloud.estimate_covariances(source)
    target.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.1, max_nn=30))
    o3d.geometry.PointCloud.estimate_covariances(target)

    draw_registration_result(source, target)

    #reg_p2p = o3d.pipelines.registration.registration_icp(
    #    pc_1, pc_2, threshold, trans_init,
    #    o3d.pipelines.registration.TransformationEstimationPointToPoint())
    if method=='ICP':
        # Define the parameters for the ICP algorithm
        threshold = 500 # Distance threshold for corresponding points
        trans_init = np.eye(4)  # Initial transformation
        target_T_source = o3d.pipelines.registration.registration_icp(
            source, target, threshold, trans_init,
            o3d.pipelines.registration.TransformationEstimationPointToPoint())
    elif method == 'generalized_ICP':
        target_T_source = o3d.pipelines.registration.registration_icp(
        source, target, max_correspondence_distance=500,
            estimation_method=o3d.pipelines.registration.TransformationEstimationForGeneralizedICP()
        )

    print(target_T_source.transformation)

    transformed_source = source.transform(target_T_source.transformation)
    draw_registration_result(transformed_source, target)

    return


if __name__=='__main__':

    main(method='ICP')