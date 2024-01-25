import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time


class Move_turtle(Node):
    def __init__(self):
        super().__init__('move_turtle') #type: ignore
        self.create_timer(0.1, self.pub_callback)
        self.create_timer(1/30, self.update_callback)
        self.pub = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)
        self.msg = Twist()
        self.ptime = time.time()

    def pub_callback(self):
        self.pub.publish(self.msg)

    def update_callback(self):
        # create your idea
        # self.msg.angular.z = 2.0
        # self.msg.linear.x += 0.01
        # if self.msg.linear.x > 10:
        #     self.msg.linear.x = 0.0
        if time.time() - self.ptime < 1:
            self.msg.linear.x = 3.0
            self.msg.angular.z = 0.0
        elif time.time() - self.ptime < 1.5:
            self.msg.linear.x = 0.0
            self.msg.angular.z = 2.0
        else:
            self.ptime = time.time()
