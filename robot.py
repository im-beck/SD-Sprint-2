def aSection():
    # Set the robot's mode to free movement
    robot_ctrl.set_mode(rm_define.robot_mode_free)
    
    # Set the rotation speed of the chassis to 30 degrees per second
    chassis_ctrl.set_rotate_speed(30)
    
    # Move the robot forward 5 meters
    chassis_ctrl.move_with_distance(0, 5)
    
    # Move the robot forward 0.5 meters
    chassis_ctrl.move_with_distance(0, 0.50)
    
    # Pause execution for 5 seconds
    time.sleep(5)

def bSection():
    # Set the robot's mode to free movement
    robot_ctrl.set_mode(rm_define.robot_mode_free)
    
    # Set the rotation speed of the chassis to 30 degrees per second
    chassis_ctrl.set_rotate_speed(30)

    # Maze Navigation
    chassis_ctrl.move_with_distance(0, 0.3)   # Forward 0.3 meters
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 115)  # Rotate left 115 degrees
    chassis_ctrl.move_with_distance(0, 0.8)   # Forward 0.8 meters
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 110)  # Rotate right 110 degrees
    chassis_ctrl.move_with_distance(0, 0.4)   # Right 0.4 meters
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 60)   # Rotate right 60 degrees
    chassis_ctrl.move_with_distance(0, 1.6)   # Forward 1.6 meters
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 50)   # Rotate left 50 degrees
    chassis_ctrl.move_with_distance(0, 0.5)   # Left 0.5 meters
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 120)  # Rotate left 120 degrees
    chassis_ctrl.move_with_distance(0, 0.546)  # Forward 0.546 meters
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 45)  # Rotate right 45 degrees
    chassis_ctrl.move_with_distance(0, 1.4)   # Forward 1.4 meters
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 75)  # Rotate right 75 degrees
    chassis_ctrl.move_with_distance(0, 0.6)   # Forward 0.6 meters
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 50)  # Rotate right 50 degrees
    chassis_ctrl.move_with_distance(0, 0.9)   # Forward 0.9 meters
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)  # Rotate left 90 degrees
    chassis_ctrl.move_with_distance(0, 0.5)   # Forward 0.5 meters

    # Pause execution for 5 seconds
    time.sleep(5)

def start():
    aSection()
    bSection()

start()
