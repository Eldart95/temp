import setup_path 
import airsim
import funcs
import time

# connect to the AirSim simulator 
client = airsim.CarClient()
client.confirmConnection()
client.enableApiControl(True)
car_controls = airsim.CarControls()
print("OK")




while True: 
    ##### Collecting Data from LIDAR #####
    car_state = client.getCarState()
    print("Speed %d, Gear %d" % (car_state.speed, car_state.gear))
    front_lidarData = client.getLidarData("Emergancy-Brake");
    left_lidarData  = client.getLidarData("Left-Lane_Assist");
    right_lidarData = client.getLidarData("Right-Lane_Assist");
    
    front_dist_3d = funcs.avg_distance(front_lidarData.point_cloud)
    left_dist_3d = funcs.avg_distance(left_lidarData.point_cloud)
    right_dist_3d = funcs.avg_distance(right_lidarData.point_cloud)

    ###### PRINTINGS ######
    print("\nfront avg distance from closest obstacle is %s:" % front_dist_3d)
    print("\nleft avg distance from closest obstacle is %s:" % left_dist_3d)
    print("\nright avg distance from closest obstacle is %s:" %right_dist_3d)
    

    car_controls.throttle = 1.0
    car_controls.steering = 0
    client.setCarControls(car_controls)

    if front_dist_3d-((car_state.speed**2)/20) < 15 :
        funcs.emergancy_brake(client,car_controls)   

    if front_dist_3d > 7 :
        car_controls.steering = 0
        car_controls.brake = 0
        car_controls.manual_gear = 1
        car_controls.throttle = 0.3
        client.setCarControls(car_controls)
        time.sleep(1)   # let car drive a bit

    
    if front_dist_3d < 7 or front_closest_point < 9: 
        client.enableApiControl(True)
        print("Obstacle ahead,Braking\n")
        car_controls.brake = 1
        car_controls.throttle = 0
        client.setCarControls(car_controls)
        time.sleep(1)   # let car drive a bit
        max = left_dist_3d>=right_dist_3d?left_dist_3d:right_dist_3d
        if left_dist_3d > 2.8:
            car_controls.brake = 0
            car_controls.throttle = 0.4
            car_controls.steering = -1
            client.setCarControls(car_controls)
            time.sleep(3)
        if right_dist_3d > 2.8:
            car_controls.brake = 0
            car_controls.throttle = 0.4
            car_controls.steering = 1
            client.setCarControls(car_controls)
            time.sleep(3)
        client.enableApiControl(False)

    if right_dist_3d < 2.3 and left_dist_3d > 2.3 :
        print("Correcting to the left\n")
        car_controls.steering = -0.1
        car_controls.throttle = 0.2
        client.setCarControls(car_controls)
        time.sleep(0.75)   # let car drive a bit
        car_controls.steering = 0.2
        car_controls.throttle = 0.2
        client.setCarControls(car_controls)
        time.sleep(0.5)   # let car drive a bit

    if left_dist_3d < 2.3 and right_dist_3d > 2.3:
        print("Correcting to the right\n")
        car_controls.steering = 0.1
        car_controls.throttle = 0.2
        client.setCarControls(car_controls)
        time.sleep(0.75)   # let car drive a bit
        car_controls.steering = -0.2
        car_controls.throttle = 0.2
        client.setCarControls(car_controls)
        time.sleep(0.5)   # let car drive a bit