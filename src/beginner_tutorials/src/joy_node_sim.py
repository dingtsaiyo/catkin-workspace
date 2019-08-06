#!/usr/bin/env python
import rospy
import math

from sensor_msgs.msg import Joy
from std_msgs.msg import Float32


class JoyMapper(object):
    def __init__(self):
        # Publications
        self.pub_motor_right = rospy.Publisher("/right_thrust_cmd",Float32,queue_size=1)
        self.pub_motor_left = rospy.Publisher("/left_thrust_cmd",Float32,queue_size=1)

        # Subscriptions
        self.sub_joy = rospy.Subscriber("joy", Joy, self.cbJoy, queue_size=1)

        #varibles
        self.right = 0
        self.left = 0

        #timer
        self.timer = rospy.Timer(rospy.Duration(0.2),self.cb_publish)
        
    def cb_publish(self,event):
        self.pub_motor_right.publish(self.right)
        self.pub_motor_left.publish(self.left)


    def cbJoy(self, joy_msg):
        self.joy = joy_msg
        '''
        speed = math.sqrt((math.pow(self.joy.axes[1],2)+math.pow(self.joy.axes[3],2))/2)
        print('Axe 1: {}'.format(self.joy.axes[1]))
        print('Axe 3: {}'.format(self.joy.axes[3]))
        phi = math.atan2(self.joy.axes[1],self.joy.axes[3])
        speed = speed*math.sin(phi)
        difference = speed*math.cos(phi)
        
        self.right = max(min(speed + difference , 1),-1)
        self.left = max(min(speed - difference , 1),-1)
        '''
        speed = self.joy.axes[1]
        difference = self.joy.axes[3]
        self.right = speed + difference
        self.left = speed - difference
        print('Right speed: {}'.format(self.right))
        print('Left speed: {}'.format(self.left))


    def processButtons(self, joy_msg):
        # Button A
        if (joy_msg.buttons[0] == 1):
            rospy.loginfo('A1 button')

        # Y button
        elif (joy_msg.buttons[3] == 1):
            rospy.loginfo('Y button')

        # Left back button
        elif (joy_msg.buttons[4] == 1):
            rospy.loginfo('left back button')

        # Right back button
        elif (joy_msg.buttons[5] == 1):
            rospy.loginfo('right back button')

        # Back button
        elif (joy_msg.buttons[6] == 1):
            rospy.loginfo('back button')

        # Start button
        elif (joy_msg.buttons[7] == 1):
            self.autoMode = not self.autoMode
            if self.autoMode:
                rospy.loginfo('going auto')
            else:
                rospy.loginfo('going manual')

    # Power/middle button
        elif (joy_msg.buttons[8] == 1):
            self.emergencyStop = not self.emergencyStop
            if self.emergencyStop:
                rospy.loginfo('emergency stop activate')
                self.right = 0
                self.left = 0
            else:
                rospy.loginfo('emergency stop release')
        # Left joystick button
        elif (joy_msg.buttons[9] == 1):
            rospy.loginfo('left joystick button')

        else:
            some_active = sum(joy_msg.buttons) > 0
            if some_active:
                rospy.loginfo('No binding for joy_msg.buttons = %s' % str(joy_msg.buttons))

    def on_shutdown(self):
        self.right = 0
        self.left = 0
        self.pub_motor_cmd.publish(self.motor_msg)
        rospy.loginfo("shutting down [%s]" %(self.node_name))

if __name__ == "__main__":
    rospy.init_node("joy_mapper",anonymous=False)
    joy_mapper = JoyMapper()
    rospy.on_shutdown(joy_mapper.on_shutdown)
    rospy.spin()

