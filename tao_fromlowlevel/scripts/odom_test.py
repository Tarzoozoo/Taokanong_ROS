#!/usr/bin/env python

import rospy

from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist

global target
global pub
target = 3.0
pub = rospy.Publisher('cmd_vel', Twist, queue_size = 1)
def listener():
    
    rospy.init_node('target', anonymous=True)
    rospy.Subscriber("odom", Odometry, callback)
    rospy.spin()

def callback(data):
    pos_x = data.pose.pose.position.x
    diff = 0.1 * (target - pos_x)
    print(pos_x, diff)

    rate = rospy.Rate(10)
    twist = Twist()
    twist.linear.x = diff
    twist.linear.y = 0
    twist.linear.z = 0
    twist.angular.x = 0
    twist.angular.y = 0
    twist.angular.z = 0
    pub.publish(twist)
    rate.sleep

if __name__ == '__main__':
    listener()