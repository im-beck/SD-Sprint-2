def scanForMarker():


    vision_ctrl.enable_detection(rm_define.vision_detection_marker)
    gimbal_ctrl.recenter()
    gimbal_ctrl.pitch_ctrl(15)
    gimbal_ctrl.yaw_ctrl(rm_define.gimbal_right,90)
    gimbal_ctrl.yaw_ctrl(rm_define.gimbal_left,180)
    gimbal_ctrl.yaw_ctrl(rm_define.gimbal_right,90)

def scanForPerson():


    gimbal_ctrl.recenter()
    vision_ctrl.enable_detection(rm_define.vision_detection_people)
    gimbal_ctrl.pitch_ctrl(15)
    gimbal_ctrl.yaw_ctrl(rm_define.gimbal_right,90)
    gimbal_ctrl.yaw_ctrl(rm_define.gimbal_left,180)
    gimbal_ctrl.yaw_ctrl(rm_define.gimbal_right,90)

def vision_recognized_marker_letter_F(msg):

    vision_ctrl.disable_detection(rm_define.vision_detection_marker)
    vision_ctrl.detect_marker_and_aim(rm_define.vision_detection_marker)
    gun_ctrl.fire_once()
    print("Shots fired")

def vision_recognized_marker_number_one(msg):
    vision_ctrl.disable_detection(rm_define.vision_detection_marker)
    vision_ctrl.detect_marker_and_aim(rm_define.vision_detection_marker)

    gimbal_ctrl.recenter()
    chassis_ctrl.set_rotate_speed(60)
    gimbal_ctrl.set_rotate_speed(60)
    gimbal_ctrl.rotate_with_degree(rm_define.gimbal_left, 360)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 360)
    chassis_ctrl.set_rotate_speed(30)
    gimbal_ctrl.set_rotate_speed(30)
    


def vision_recognized_marker_number_two(msg):
    vision_ctrl.disable_detection(rm_define.vision_detection_marker)
    vision_ctrl.detect_marker_and_aim(rm_define.vision_detection_marker)

    led_ctrl.set_flash(rm_define.armor_all, 5)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 69, 215, 255, rm_define.effect_always_on)
    led_ctrl.set_top_led(rm_define.armor_top_all, 224, 0, 255, rm_define.effect_always_on)

def vision_recognized_marker_number_three(msg):
    vision_ctrl.disable_detection(rm_define.vision_detection_marker)
    vision_ctrl.detect_marker_and_aim(rm_define.vision_detection_marker)

    gimbal_ctrl.recenter()
    chassis_ctrl.set_rotate_speed(180)
    gimbal_ctrl.set_rotate_speed(180)
    led_ctrl.set_flash(rm_define.armor_all, 5)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 69, 215, 255, rm_define.effect_always_on)
    led_ctrl.set_top_led(rm_define.armor_top_all, 224, 0, 255, rm_define.effect_always_on)
    gimbal_ctrl.rotate_with_degree(rm_define.gimbal_left, 360)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 360)
    chassis_ctrl.set_rotate_speed(30)
    gimbal_ctrl.set_rotate_speed(30)




def vision_recognized_people(msg):

    vision_ctrl.disable_detection(rm_define.vision_detection_people)
    vision_ctrl.detect_marker_and_aim(rm_define.vision_detection_people)
    led_ctrl.set_flash(rm_define.armor_all, 10)



def aSection():
    
    
    # Set robot speed
    chassis_ctrl.set_trans_speed(0.7)

    # Set the rotation speed of the chassis to 60 degrees per second
    chassis_ctrl.set_rotate_speed(60)
    
    # Move the robot forward 5 meters
    chassis_ctrl.move_with_distance(0, 5)
    
    # Move the robot forward 0.5 meters
    chassis_ctrl.move_with_distance(0, 0.5)
    
    # Pause execution for 5 seconds
    time.sleep(1)

def bSection():
    # Set the robot's mode to free movement
    robot_ctrl.set_mode(rm_define.robot_mode_free)
    
    # Set the rotation speed of the chassis to 30 degrees per second
    chassis_ctrl.set_rotate_speed(50)

    # Maze Navigation
    chassis_ctrl.move_with_distance(0, 0.3)   # Forward 0.3 meters
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)  # Rotate left 115 degrees
    chassis_ctrl.move_with_distance(0, 0.8)   # Forward 0.8 meters
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)  # Rotate right 110 degrees
    chassis_ctrl.move_with_distance(0, 0.5)   # Right 0.4 meters
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)   # Rotate right 60 degrees
    chassis_ctrl.move_with_distance(0, 1.6)   # Forward 1.6 meters
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)   # Rotate left 50 degrees
    chassis_ctrl.move_with_distance(0, 0.5)   # Left 0.5 meters
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)  # Rotate left 120 degrees
    chassis_ctrl.move_with_distance(0, 0.546)  # Forward 0.546 meters
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 40)  # Rotate right 45 degrees
    chassis_ctrl.move_with_distance(0, 1.5)   # Forward 1.5 meters
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 50)  # Rotate right 75 degrees
    chassis_ctrl.move_with_distance(0, 0.6)   # Forward 0.6 meters
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)  # Rotate right 50 degrees
    chassis_ctrl.move_with_distance(0, 0.8)   # Forward 0.8 meters
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)  # Rotate left 90 degrees
    chassis_ctrl.move_with_distance(0, 0.5)   # Forward 0.5 meters

    # Pause execution for 5 seconds
    time.sleep(5)


def cSection():

    roomOne = 3

    chassis_ctrl.move_with_distance(0,5)
    chassis_ctrl.move_with_distance(0, 1.5)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)
    gimbal_ctrl.recenter()

    if roomOne == 1: # Fire
        chassis_ctrl.move_with_distance(0, 2.2)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)
        gimbal_ctrl.recenter()
        chassis_ctrl.move_with_distance(0, 2.1)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)
        scanForMarker()
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        chassis_ctrl.move_with_distance(0, 2.1)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
        chassis_ctrl.move_with_distance(0, 2.2)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)

    elif roomOne == 2: # Poison
        led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 50, 205, 50, rm_define.effect_breath)
        led_ctrl.set_top_led(rm_define.armor_top_all, 50, 205, 50, rm_define.effect_breath)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
        led_ctrl.turn_off(rm_define.armor_all)

    elif roomOne == 3: # Person
        chassis_ctrl.move_with_distance(0, 2.2)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)
        gimbal_ctrl.recenter()
        chassis_ctrl.move_with_distance(0, 2.1)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)
        scanForPerson()
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        chassis_ctrl.move_with_distance(0, 2.1)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
        chassis_ctrl.move_with_distance(0, 2.2)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 5)
        led_ctrl.turn_off(rm_define.armor_all)
        time.sleep(5)
        chassis_ctrl.move_with_distance(180, 5)
        chassis_ctrl.move_with_distance(180, 5)
        chassis_ctrl.move_with_distance(180, 5)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 180)
        


def dSection():
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.move_with_distance(0, 0.2)
    time.sleep(5)

def eSection():

    roomTwo = 1
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)

    # Determine Room Type
    if roomTwo == 1:  #Fire
        chassis_ctrl.move_with_distance(0,2)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        chassis_ctrl.move_with_distance(0, 1.7)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        chassis_ctrl.move_with_distance(0, 1)
        scanForMarker()
        chassis_ctrl.move_with_distance(180, 1)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        chassis_ctrl.move_with_distance(0, 1.9)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
        chassis_ctrl.move_with_distance(0, 2)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)

    elif roomTwo == 2:  # Poison
        led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 50, 205, 50, rm_define.effect_breath)
        led_ctrl.set_top_led(rm_define.armor_top_all, 50, 205, 50, rm_define.effect_breath)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
        led_ctrl.turn_off(rm_define.armor_all)
    
    elif roomTwo == 3:  # Person
        chassis_ctrl.move_with_distance(0,2)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        chassis_ctrl.move_with_distance(0, 1.7)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        scanForPerson()
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        chassis_ctrl.move_with_distance(0, 1.9)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
        chassis_ctrl.move_with_distance(0, 2)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
        
        # Bring person to point A
        chassis_ctrl.move_with_distance(0,5)
        time.sleep(5)
        chassis_ctrl.move_with_distance(0,5)
        chassis_ctrl.move_with_distance(0,5)
        chassis_ctrl.move_with_distance(0,5)
        chassis_ctrl.move_with_distance(0,5)
        time.sleep(5)
        led_ctrl.turn_off(rm_define.armor_all)
        chassis_ctrl.move_with_distance(180,5)
        chassis_ctrl.move_with_distance(180,5)
        chassis_ctrl.move_with_distance(180,5)
        chassis_ctrl.move_with_distance(180,5)
        time.sleep(5)
        chassis_ctrl.move_with_distance(180,5)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 180)



    
def fSection():
    chassis_ctrl.move_with_distance(0, 4)
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
    scanForMarker()
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
    time.sleep(5)

def gSection():

    roomThreeType = 2 # Poison

    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
    
    if roomThreeType == 2:
        led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 50, 205, 50, rm_define.effect_breath)
        led_ctrl.set_top_led(rm_define.armor_top_all, 50, 205, 50, rm_define.effect_breath)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
        led_ctrl.turn_off(rm_define.armor_all)
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 0.2)
    



def hSection():
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 180)
    time.sleep(5)
    media_ctrl.play_sound(rm_define.media_custom_audio_0)
    chassis_ctrl.set_trans_speed(1)
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.move_with_distance(0, 5)
    time.sleep(5)
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.move_with_distance(0, 4)

def dSectionPartTwo():

    led_ctrl.set_bottom_led(rm_define.armor_all, 255, 0, 0, rm_define.effect_breath)
    led_ctrl.set_top_led(rm_define.armor_all, 255, 0, 0, rm_define.effect_breath)
    j = 0
    time.sleep(5)
    while j < 4:
        chassis_ctrl.move_with_distance(0, 5)
        j += 1
    chassis_ctrl.move_with_distance(0, 0.3)

def start():

    robot_ctrl.set_mode(rm_define.robot_mode_free)
    aSection()
    bSection()
    cSection()
    dSection()
    eSection()
    fSection()
    gSection()
    hSection()
    dSectionPartTwo()


