import open3d as o3d
import numpy as np
import cv2
import matplotlib.pyplot as plt

# Load LiDAR point cloud data
lidar_points = o3d.io.read_point_cloud("lidar_point_cloud.pcd")
lidar_points_array = np.asarray(lidar_points.points)

# Load camera image
camera_image = cv2.imread("camera_image.jpg")

# Calibration parameters (fx, fy, cx, cy)
fx, fy, cx, cy = 1000.0, 1000.0, camera_image.shape[1] / 2, camera_image.shape[0] / 2

# Project LiDAR points onto the image plane
image_points = np.zeros_like(lidar_points_array[:, :2])
for i in range(len(lidar_points_array)):
    X, Y, Z = lidar_points_array[i]
    u = int(fx * (X / Z) + cx)
    v = int(fy * (Y / Z) + cy)
    image_points[i] = [u, v]

# Overlay LiDAR points on the camera image
plt.imshow(cv2.cvtColor(camera_image, cv2.COLOR_BGR2RGB))
plt.scatter(image_points[:, 0], image_points[:, 1], c=lidar_points_array[:, 2], cmap='jet', s=1)
plt.colorbar(label='Depth (Z)')
plt.show()
