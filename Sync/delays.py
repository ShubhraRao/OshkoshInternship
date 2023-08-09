import os
import re
import time
from datetime import datetime

lidar_dir = 'D:\\0-Shubhra\\CMU\\Internship\\Oshkosh\\Data\\Lidar'
camera_dir = 'D:\\0-Shubhra\\CMU\\Internship\\Oshkosh\\Data\\Camera'


def extract_unix_timestamp_milliseconds_from_filename(filename):
    print(filename)
    timestamp_str = re.search(r'pcd_(\d{17})_(\d+)\.pcd', filename)
    if timestamp_str:
        full_timestamp = timestamp_str.group(1)
        milliseconds = int(timestamp_str.group(2))
        unix_timestamp = int(full_timestamp[:-3])  # Exclude last 3 characters for milliseconds
        return unix_timestamp, milliseconds
    else:
        return None
    
def extract_unix_timestamp_from_filename(filename):
    print(filename)
    print("Hello")
    # print(re.search(r'(\w+)_(\d+)_(\w+)', filename))
    # pattern = r'(.+)_(\d{4})(\d{2})(\d{2})(\d{2})(\d{2})(\d{2})(\d{6})_(.+)$'
    pattern = r'(.+)_(\d{20})_(.+)$'
    # pattern = r'^(.*?)_'
    timestamp_str = re.search(pattern, filename)
    print(timestamp_str)
    prefix = timestamp_str.group(1)
    time = timestamp_str.group(2)
    # month = timestamp_str.group(3)
    # day = timestamp_str.group(4)
    # hour = timestamp_str.group(5)
    # minute = timestamp_str.group(6)
    # second = timestamp_str.group(7)
    # milliseconds = timestamp_str.group(8)
    suffix = timestamp_str.group(3)
    print(f"Prefix: {prefix}")
    print(f"Year: {time}")
    # print(f"Month: {month}")
    # print(f"Day: {day}")
    # print(f"Hour: {hour}")
    # print(f"Minute: {minute}")
    # print(f"Second: {second}")
    # print(f"Milliseconds: {milliseconds}")
    print(f"Suffix: {suffix}")
    
    return time



    # timestamp_str = re.search(r'_(\d+)_', filename).group(1)
    
    # return int(timestamp_str)

# def extract_timestamp_from_filename(filename):
#     timestamp_str = re.search(r'\d{14}', filename).group()
#     return datetime.strptime(timestamp_str, '%Y%m%d%H%M%S')

def sort_filenames(directory):
    filenames = [f for f in os.listdir(directory) if f.endswith('.png') or f.endswith('.pcd')]
    return sorted(filenames)


lidar_filenames = sort_filenames(lidar_dir)
camera_filenames = sort_filenames(camera_dir)

for lidar_filename, camera_filename in zip(lidar_filenames, camera_filenames):
    lidar_unix_timestamp  = extract_unix_timestamp_from_filename(lidar_filename)
    camera_unix_timestamp  = extract_unix_timestamp_from_filename(camera_filename)

    datetime_format = "%Y%m%d%H%M%S%f"
    lidar_datetime = datetime.strptime(lidar_unix_timestamp, datetime_format)
    camera_datetime = datetime.strptime(camera_unix_timestamp, datetime_format)

    # lidar_datetime = datetime.fromtimestamp(lidar_unix_timestamp) + timedelta(milliseconds=lidar_milliseconds)
    # camera_datetime = datetime.fromtimestamp(camera_unix_timestamp) + timedelta(milliseconds=camera_milliseconds)

    print(lidar_datetime)
    print(camera_datetime)

    delay_in_milliseconds = int((camera_datetime - lidar_datetime).total_seconds() * 1000)
    
    print(f"Lidar File: {lidar_filename} | Camera File: {camera_filename} | Delay: {delay_in_milliseconds:.2f} milliseconds")
    
    # time.sleep(delay)
