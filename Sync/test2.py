import open3d as o3d
import matplotlib.pyplot as plt
import os

# Load LiDAR point cloud
lidar_pcd_path = "path_to_lidar.pcd"
lidar_pcd = o3d.io.read_point_cloud(lidar_pcd_path)

# Load camera images
image_folder = "path_to_images_folder"
image_files = sorted([f for f in os.listdir(image_folder) if f.endswith('.jpg')])

# Visualize LiDAR point cloud
o3d.visualization.draw_geometries([lidar_pcd])

# Visualize synchronization
for image_file in image_files:
    image_path = os.path.join(image_folder, image_file)
    image = plt.imread(image_path)

    # Display image and LiDAR point cloud together
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
    ax1.imshow(image)
    o3d.visualization.draw_geometries_with_editing([lidar_pcd], window_name='LiDAR Point Cloud', width=800, height=600, left=800)
    plt.show()
