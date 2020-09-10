# TurtleBot-LineFollower

## Introduction
This project utilizes ROS to exhibit a basic line following robot in a simulated Gazebo environment. Line
following is a simple and highly useful application for a robot as all it requires is a robot with a camera and
pre-defined line, this can be utilized to make complex significant level models utilizing various robots and
numerous ways. This can be executed in ventures and shop floors for material dealing with and distribution or in
industrial factories. These robots can be made to follow these paths in periodic intervals autonomously and
subsequently automate the function of the entire material handling system in a highly proficient way.


## Procedure 
This project consist of 3 main aspects which can be defined as followS
1) simulation environment
2) robot modeling
3) robot programing

### 1) robot modeling
TurtleBot is a low-cost, personal robot kit with open-source software. With TurtleBot, we’ll be
able to build a robot that can drive around any environment. Figure 1
![image](https://user-images.githubusercontent.com/45981942/92712727-be1ae680-f362-11ea-86cd-cbeba63bd5f6.png)
The main sensor of the TutelBot is the 3D camera. The 3D camera is one of the most versatile
robot sensors. One output of a 3D camera is a 2D camera image, which means that various object
recognition algorithms can be used. Many machine vision libraries are available for ROS. One of the
most widely used and versatile is OpenCV

![image](https://user-images.githubusercontent.com/45981942/92712819-ddb20f00-f362-11ea-933a-8191c3e5e62b.png)


### 2) simulation environment
Robot simulation is an essential tool in every roboticist's toolbox. A well-designed simulator makes it
possible to rapidly test algorithms, design robots, perform regression testing, and train AI system using
realistic scenarios. Gazebo offers the ability to accurately and efficiently simulate populations of robots
in complex indoor and outdoor environments. At your fingertips is a robust physics engine, high-quality
graphics, and convenient programmatic and graphical interfaces. Best of all, Gazebo is free with a
vibrant community.

In this project we used TurtleBot simulated in Gazebo by creating a Gazebo world containing some
walls and a blue path for our TurtleBot to follow, as it shown in figure 3
In this world we also add some light to create shadows to try it on the 3D camera to simulate the effects
done on the colors

![image](https://user-images.githubusercontent.com/45981942/92712976-12be6180-f363-11ea-8cfe-52dea63a215d.png)
                               *Gazebo map*

### 3) Robot programing

In order to program this robot, we used Python programing language and we connected it with ROS by using
nodes, or robot contain two main nodes
1. Vision node
2. Motion node
According to the receiving image from the 3D camera our Vision node send a heading message to the Motion
node, Motion node convert this message into velocity messages and send it to the motors
All of this can be summarized by the following flowchart

![image](https://user-images.githubusercontent.com/45981942/92713291-7ba5d980-f363-11ea-93db-e6d7dd7e1a01.png)

## Results
After building and testing the model in the simulated environment the following results are obtained, the robot
can navigate autonomously through the custom-built maze.
The output from the TurtleBot camera can be seen below. The image processing is performed from the images
obtained from this camera

![image](https://user-images.githubusercontent.com/45981942/92713439-a6902d80-f363-11ea-962f-756d7df46c6d.png)

The messages send to the motor can be seen below, the movement procedure is preformed from the message
obtain from the Vision node.

![image](https://user-images.githubusercontent.com/45981942/92713601-d8a18f80-f363-11ea-87dd-36f646382fab.png)

*message from movement node*

![image](https://user-images.githubusercontent.com/45981942/92713658-ec4cf600-f363-11ea-8be4-ca9ec67b50be.png)

*robot movement*

## To build
To build the project run the following steps in a terminal

1- *Creating a catkin workspace*
```
mkdir catkin_ws
cd catkin_ws
mkdir src
catkin_make
```
2- *Cloning the repository and building*
```
cd ~/catkin_ws/src
git clone https://github.com/Alhassan-Khalil/TurtleBot-LineFollower.git
cd ..
catkin_make
```
## TO RUN
```
cd ~/catkin_ws/src/TurtleBot-LineFollower/src
python ./Launch.py
```

