# health_monitoring_system
ROS 2 Health Monitoring System
A simple ROS 2 project that simulates a real-time health monitoring system for robotic platforms. The node periodically generates CPU usage and temperature values, evaluates the system's health based on predefined thresholds, and publishes diagnostic messages over a ROS 2 topic.

Features
Real-time health monitoring using ROS 2 timers.
Simulated CPU utilization and temperature data.
Threshold-based warning detection.
Publishes system status on a ROS 2 topic.
Console logging for real-time diagnostics.
Lightweight and modular Python implementation using rclpy.

Technologies Used
ROS 2
Python
rclpy
ROS 2 Topics
Timer Callbacks
Standard ROS Messages (std_msgs/String)

How It Works
A ROS 2 timer triggers the monitoring node every second.
The node generates simulated CPU and temperature values.
If CPU usage exceeds 80% or temperature exceeds 70°C, a warning message is published.
Otherwise, the node publishes a normal system health status.
All health messages are simultaneously logged to the terminal.

Example Output
NORMAL | CPU=42% TEMP=61°C
NORMAL | CPU=67% TEMP=64°C
WARNING | CPU=91% TEMP=74°C
NORMAL | CPU=38% TEMP=58°C

Future Improvements
Integrate with actual system diagnostics using the psutil library.
Publish structured diagnostic messages instead of plain strings.
Add CPU, RAM, disk, battery, and network monitoring.
Visualize health metrics in RViz or a custom dashboard.
Generate alerts via email or mobile notifications for critical conditions.
Support monitoring of multiple robotic subsystems.
