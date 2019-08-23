#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
import sys
from std_srvs.srv import Empty
PI = 3.1415926535897

 
def move(speed,distance,isForward):
    # Starts a new node
    rospy.init_node('robot_cleaner', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()
 
    #Receiveing the user's input
    print("Let's move your robot")
    #speed = input("Input your speed:")
    #distance = input("Type your distance:")
    #isForward = input("Foward?: ")#True or False
 
    #speed=3
    #distance=4
    #isForward=1

    #Checking if the movement is forward or backwards
    if(isForward):
        vel_msg.linear.x = abs(speed)
    else:
        vel_msg.linear.x = -abs(speed)
    #Since we are moving just in x-axis
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0
 
    #while not rospy.is_shutdown():
 
        #Setting the current time for distance calculus
    t0 = rospy.Time.now().to_sec()
    current_distance = 0
 
        #Loop to move the turtle in an specified distance
    while(current_distance < distance):
            #Publish the velocity
        velocity_publisher.publish(vel_msg)
            #Takes actual time to velocity calculus
        t1=rospy.Time.now().to_sec()
            #Calculates distancePoseStamped
        current_distance= speed*(t1-t0)
        #After the loop, stops the robot
    vel_msg.linear.x = 0
        #Force the robot to stop
    velocity_publisher.publish(vel_msg)
    print("first move end")

def move1():
    # Starts a new node
    rospy.init_node('robot_cleaner', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()
 
    #Receiveing the user's input
    print("Let's move your robot")
    #speed = input("Input your speed:")
    #distance = input("Type your distance:")
    #isForward = input("Foward?: ")#True or False
 
    speed=3
    distance=8
    isForward=1

    #Checking if the movement is forward or backwards
    if(isForward):
        vel_msg.linear.x = abs(speed)
    else:
        vel_msg.linear.x = -abs(speed)
    #Since we are moving just in x-axis
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0
 
    #while not rospy.is_shutdown():
 
        #Setting the current time for distance calculus
    t0 = rospy.Time.now().to_sec()
    current_distance = 0
 
        #Loop to move the turtle in an specified distance
    while(current_distance < distance):
        #Publish the velocity
        velocity_publisher.publish(vel_msg)
            #Takes actual time to velocity calculus
        t1=rospy.Time.now().to_sec()
            #Calculates distancePoseStamped
        current_distance= speed*(t1-t0)
    #After the loop, stops the robot
    vel_msg.linear.x = 0
    #Force the robot to stop
    velocity_publisher.publish(vel_msg)
        

def rotate(speed,angle,clockwise):
    #Starts a new node
    rospy.init_node('robot_cleaner', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()
 
    # Receiveing the user's input
    print("Let's rotate your robot")
    #speed = input("Input your speed (degrees/sec):")
    #angle = input("Type your distance (degrees):")
    #clockwise = input("Clockwise?: ") #True or false

    #speed=50
    #angle=100
    #clockwise=0
 
    #Converting from angles to radians
    angular_speed = speed*2*PI/360
    relative_angle = angle*2*PI/360
 
    #We wont use linear components
    vel_msg.linear.x=0
    vel_msg.linear.y=0
    vel_msg.linear.z=0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
 
    # Checking if our movement is CW or CCW
    if clockwise:
        vel_msg.angular.z = -abs(angular_speed)
    else:
        vel_msg.angular.z = abs(angular_speed)
    # Setting the current time for distance calculus
    t0 = rospy.Time.now().to_sec()
    current_angle = 0
 
    while(current_angle < relative_angle):
        velocity_publisher.publish(vel_msg)
        t1 = rospy.Time.now().to_sec()
        current_angle = angular_speed*(t1-t0)
 
 
    #Forcing our robot to stop
    vel_msg.angular.z = 0
    velocity_publisher.publish(vel_msg)
    #rospy.spin()
    print("asasas")



def rotate1():
    #Starts a new node
    rospy.init_node('robot_cleaner', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()
 
    # Receiveing the user's input
    print("Let's rotate your robot")
    #speed = input("Input your speed (degrees/sec):")
    #angle = input("Type your distance (degrees):")
    #clockwise = input("Clockwise?: ") #True or false

    speed=50
    angle=190
    clockwise=1
 
    #Converting from angles to radians
    angular_speed = speed*2*PI/360
    relative_angle = angle*2*PI/360
 
    #We wont use linear components
    vel_msg.linear.x=0
    vel_msg.linear.y=0
    vel_msg.linear.z=0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
 
    # Checking if our movement is CW or CCW
    if clockwise:
        vel_msg.angular.z = -abs(angular_speed)
    else:
        vel_msg.angular.z = abs(angular_speed)
    # Setting the current time for distance calculus
    t0 = rospy.Time.now().to_sec()
    current_angle = 0
 
    while(current_angle < relative_angle):
        velocity_publisher.publish(vel_msg)
        t1 = rospy.Time.now().to_sec()
        current_angle = angular_speed*(t1-t0)
 
 
    #Forcing our robot to stop
    vel_msg.angular.z = 0
    velocity_publisher.publish(vel_msg)
    #rospy.spin()
    print("asasas")


if __name__ == '__main__':
    if(sys.argv[1]=="2"):
        print("2")
    else:
        try:
            #Testing our function
            rotate(50,100,0)
            print("finish rotate")
            move(3,4,1)
            print("second")
            rospy.ServiceProxy('clear', Empty)()
            #rotate1()
            #move1()
        except rospy.ROSInterruptException: pass