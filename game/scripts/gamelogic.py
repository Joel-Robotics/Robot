#!/usr/bin/env python

# !/usr/bin/env python
import rospy
from std_msgs.msg import int

def where_is_ball(ball_coordinates):
    ball_coordinates =
    if ball_coordinates

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)


def listener():

    rospy.init_node('gamelogic', anonymous=True)

    rospy.Subscriber("ball_center_coordinates", int, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()
    return()


if __name__ == '__main__':
    listener()