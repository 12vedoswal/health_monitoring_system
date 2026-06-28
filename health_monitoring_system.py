import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import random

class HealthMonitor(Node):
    def __init__(self):
        super().__init__("health_monitor")
        self.publisher_ = self.create_publisher(String, "health_monitor", 10)
        self.time_ = self.create_timer(1.0, self.check_health)

    def check_health(self):
        msg = String()
        cpu = random.randint(1,100)
        temp = random.randint(50,100)

        if cpu > 80 or temp >70 :
            msg.data = F"warming | CPU={cpu}% TEMP={temp}C"
        else:
            msg.data = f"NORMAL | CPU={cpu}% TEMP={temp}C"

        self.publisher_.publish(msg)
        self.get_logger().info(msg.data)



def main(args=None):
    rclpy.init(args=args)
    node = HealthMonitor()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__" :
    main()
