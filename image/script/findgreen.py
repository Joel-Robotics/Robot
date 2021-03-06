#!/usr/bin/env python

import numpy as np
import cv2
import rospy
from std_msgs.msg import int


#
def image_node():
    pub = rospy.Publisher('ball_center_coordinates', int)
    rospy.init_node('image_node', anonymous=True)
    rate = rospy.Rate(10)  # 10hz
    while not rospy.is_shutdown():
        ball_center_coordinates =
        rospy.loginfo(hello_str
        pub.publish(ball_center_coordinates)
        rate.sleep()
  #


def ball_center_coordinates()
    while(True):
        cap = cv2.VideoCapture(2)
        # Capture frame-by-frame
        __, frame = cap.read()

        # Our operations on the frame come here
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        lower_green = np.array([36,0,0])
        upper_green = np.array([86,255,255])

        mask = cv2.inRange(hsv, lower_green, upper_green)

        res = cv2.bitwise_and(frame, frame, mask = mask)

        cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
                                cv2.CHAIN_APPROX_SIMPLE)[-2]

        center = None
        lenq = 10 # Maximum number of center points stored in memory

        if len(cnts) > 0:

            #print(len(cnts))

            c = max(cnts, key=cv2.contourArea)
            ((x,y), radius) = cv2.minEnclosingCircle(c)
            M = cv2.moments(c)
            if radius >7:
                center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
                center[0] = int(center)  #simplification of result to int to test a simple ball finder program

                return(center)



        #cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)




        # Display the resulting frame
        cv2.imshow("frame",res)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
        cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    try:
        image_node()
    except rospy.ROSInterruptException:
        pass