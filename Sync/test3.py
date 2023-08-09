import open3d as o3d
import cv2
import numpy as np

lidar_pcd_path = "Data/Lidar/pcd_20230807033729999312_1.pcd"
lidar_pcd = o3d.io.read_point_cloud(lidar_pcd_path)

image_path = "Data/Camera/camera_20230807033729847312_1.png"
image = cv2.imread(image_path)

fx = 1000  # Focal length along X-axis
fy = 1000  # Focal length along Y-axis
cx = image.shape[1] / 2  # Principal point X-coordinate
cy = image.shape[0] / 2  # Principal point Y-coordinate

# Extrinsic transformation matrix (LiDAR to camera)
lidar_to_camera_transform = np.array([[0.866, -0.5, 0.0, 100],
                                     [0.5, 0.866, 0.0, 200],
                                     [0.0, 0.0, 1.0, 50],
                                     [0.0, 0.0, 0.0, 1.0]])

lidar_points = np.asarray(lidar_pcd.points)
lidar_points_transformed = np.dot(lidar_to_camera_transform[:3, :3], lidar_points.T) + lidar_to_camera_transform[:3, 3].reshape(-1, 1)

projected_points = np.dot(np.array([[fx, 0, cx], [0, fy, cy], [0, 0, 1]]), lidar_points_transformed)
projected_points = projected_points[:2] / projected_points[2]  # Normalize by depth

valid_indices = np.logical_and.reduce((projected_points[0] >= 0,
                                       projected_points[0] < image.shape[1],
                                       projected_points[1] >= 0,
                                       projected_points[1] < image.shape[0]))

intersection_points = lidar_points[valid_indices]

intersection_pcd = o3d.geometry.PointCloud()
intersection_pcd.points = o3d.utility.Vector3dVector(intersection_points)
o3d.visualization.draw_geometries([lidar_pcd, intersection_pcd])

print(intersection_points)

for point in intersection_points:
    x, y = int(point[0]), int(point[1])
    cv2.circle(image, (x, y), radius=5, color=(0, 0, 255), thickness=-1)

cv2.imshow("Intersection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
