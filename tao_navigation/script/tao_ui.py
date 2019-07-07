#!/usr/bin/env python

import sys
from PyQt4 import uic, QtGui
import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from std_msgs.msg import Float32MultiArray

class MyWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        uic.loadUi('/home/tarzoozoo/ttao_ws/src/tao_navigation/script/Tao.ui', self)
    
        self.office_btn.clicked.connect(self.office_path)
        self.lab1_btn.clicked.connect(self.lab1_path)
        self.lab3_btn.clicked.connect(self.lab3_path)
        # ROS
        rospy.init_node('movebase_client')
        rospy.Subscriber("chatter", Float32MultiArray, self.get_IR)
        self.state_IR = 0

    # Check IR's state
    # state = 1 ==> non-detected
    # state = 0 ==> detected
    def get_IR(self, data):
        self.state_IR = data.data[2]
        check = Float32MultiArray(data = [self.state_IR])
        check_pub = rospy.Publisher('getState', Float32MultiArray, queue_size=20)
        check_pub.publish(check)
    
    def office_path(self):
        state = self.state_IR
        if(state == 1):
            rospy.logerr("Please insert your documents and choose again")

        elif(state == 0):
            print("Office")
            # self.client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
            # self.client.wait_for_server()
            # goal = MoveBaseGoal()
            # goal.target_pose.header.frame_id = "map"
            # goal.target_pose.header.stamp = rospy.Time.now()
            # goal.target_pose.pose.position.x = 1.0
            # goal.target_pose.pose.orientation.w = 1.0

            # self.client.send_goal(goal)
            # wait = self.client.wait_for_result()
            # if not wait:
            #     rospy.logerr("Action server not available!")
            #     rospy.signal_shutdown("Action server not available!")
            # else:
            #     return self.client.get_result()

            # Reget state
            while(True):
                state = self.state_IR
                if(state == 1):
                    break
            self.home()
            

    def lab1_path(self):
        state = self.state_IR
        if(state == 1):
            rospy.logerr("Please insert your documents and choose again")
        elif(state == 0):    
            print("Lab1")

            while(True):
                state = self.state_IR
                if(state == 1):
                    break
            self.home()

    def lab3_path(self):
        state = self.state_IR
        if(state == 1):
            rospy.logerr("Please insert your documents and choose again")
        elif(state == 0):    
            print("Lab3)

            while(True):
                state = self.state_IR
                if(state == 1):
                    break
            self.home()

    def home(self):
        print("home")
        rospy.sleep(3)


if __name__ == '__main__':
    # try:
    app = QtGui.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
    
    

        

    # except rospy.ROSException as e:
    #     print(e)