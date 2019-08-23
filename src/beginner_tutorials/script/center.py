#!/usr/bin/env python
import rospy
import sys
from darknet_ros_msgs.msg import BoundingBoxes



def gettaginfo(data):
    for i in data.bounding_boxes:
        if i.Class =="person":
            a=(i.xmin+i.xmax)/2    
            b=(i.ymin+i.ymax)/2
            print(a)
            print(b)
            print(" ")
    
 
        
      
def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("/darknet_ros/bounding_boxes",BoundingBoxes, gettaginfo)
    #print('4')

    rospy.spin()

if __name__ == '__main__':
    #print('3')
    listener()
    #print('2')