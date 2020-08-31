import setup_path 
import airsim
import time

def emergancy_brake(client,car_controls):
    client.enableApiControl(True)
    print("Obstacle ahead,Braking\n")
    car_controls.brake = 1
    car_controls.throttle = 0
    client.setCarControls(car_controls)
    time.sleep(2)   # let car drive a bit

def avg_distance(point_cloud):
    point_3d = 0
    for i in range(0,len(point_cloud)-3,3):
        
        point_x = point_cloud[i]
        point_y = point_cloud[i+1]
        point_z = point_cloud[i+2]

        formula = (point_x**2+point_y**2+point_z**2)**0.5
        #if formula < front_closest_point:
            #front_closest_point = formula
        point_3d += formula

    front_dist_3d = point_3d/(len(point_cloud)/3)
    return front_dist_3d



"""
    ##### Avg point from front Sensor #####
    for i in range(0,len(front_lidarData.point_cloud)-3,3):
        
        point_x = front_lidarData.point_cloud[i]
        point_y = front_lidarData.point_cloud[i+1]
        point_z = front_lidarData.point_cloud[i+2]

        formula = (point_x**2+point_y**2+point_z**2)**0.5
        if formula < front_closest_point:
            front_closest_point = formula
        point_3d += formula

    front_dist_3d = point_3d/(len(front_lidarData.point_cloud)/3)

    ##### Avg point from left Sensor #####
    point_3d = 0
    for i in range(0,len(left_lidarData.point_cloud)-3,3):
        
        point_x = left_lidarData.point_cloud[i]
        point_y = left_lidarData.point_cloud[i+1]
        point_z = left_lidarData.point_cloud[i+2]

        point_3d += (point_x**2+point_y**2+point_z**2)**0.5
    left_dist_3d = point_3d/(len(left_lidarData.point_cloud)/3)

    ##### Avg point from right Sensor #####
    point_3d = 0
    for i in range(0,len(right_lidarData.point_cloud)-3,3):
        
        point_x = right_lidarData.point_cloud[i]
        point_y = right_lidarData.point_cloud[i+1]
        point_z = right_lidarData.point_cloud[i+2]

        point_3d += (point_x**2+point_y**2+point_z**2)**0.5

    right_dist_3d = point_3d/(len(right_lidarData.point_cloud)/3)
"""
