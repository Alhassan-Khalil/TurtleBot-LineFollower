#!/usr/bin/env python
#dependencies
import roslib
import sys
import rospy
import cv2
import numpy as np
from std_msgs.msg import String
from sensor_msgs.msg import Image
from std_msgs.msg import Int32
from cv_bridge import CvBridge, CvBridgeError
bridge = CvBridge()
#parameters
global bridge,hsv,steering
gain = 20

def color_mask(frame):
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    blur = cv2.GaussianBlur(hsv,(5,5),0)
    lower = np.array([85, 225, 0])
    upper = np.array([179, 255, 255])
    mask = cv2.inRange(blur, lower, upper)
    return mask

def callback(Image):
    try:
      cv_image = bridge.imgmsg_to_cv2(Image, desired_encoding="passthrough")
    except CvBridgeError as e:
     print(e)

# image processing
    image_view = cv_image
    cv_image = cv_image[360:480, 160:480]
    h,w,_ = cv_image.shape
    mask = color_mask(cv_image)
    contours,hierarchy = cv2.findContours(mask.copy(), 1, cv2.CHAIN_APPROX_NONE)
    left_offset = min(range(w/2-gain,w/2))
    right_offset = max(range(w/2,w/2+gain))

    if len(contours) > 0:
        c = max(contours, key=cv2.contourArea)
        M = cv2.moments(c)
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
        position = (cx,cy)
        cv2.line(cv_image,(w/2,h), (cx,cy),(0,0,255),thickness=5,lineType=8)
        cv2.putText(cv_image,"Direction",position,cv2.FONT_HERSHEY_SIMPLEX,1,(209, 80, 0, 255),1)
        cv2.drawContours(cv_image, contours, -1, (0,255,0), 3)

        if cx < left_offset:
            steering = 2
        elif cx > right_offset:
            steering = 3
        else:
            steering = 1

    if len(contours) == 0:
        steering = 0

    #publishing the steering
    pub = rospy.Publisher('vision_node',Int32, queue_size=10)
    msg_sterring = (steering)
    #rospy.loginfo(msg_sterring)
    pub.publish(msg_sterring)

    #show the frame
    cv2.imshow("Camera View", image_view)
    #cv2.imshow("processing Image",cv_image)
    cv2.waitKey(1)


def main(args):
  rospy.init_node('vision_node', anonymous=True)
  image_sub = rospy.Subscriber("/camera/rgb/image_raw",Image,callback)
  try:
    rospy.spin()
  except KeyboardInterrupt:
    print("Shutting down")
  cv2.destroyAllWindows()

if __name__ == '__main__':
    main(sys.argv)
