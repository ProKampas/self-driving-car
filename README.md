# self-driving-car

This repository is my hands on experience of  Udemy course: The Complete Self-Driving Car Course - Applied Deep Learning
to drive an automated car in Carla Simulator.

Most of the Jupyter Notebooks implemented for the needs of the course were pretty simple, therefore I have only commited
the **Road Symbols Classification** and the **Behavioral Cloning** projects. 

For the **Road Symbols Classification** project you will require this dataset: [german-traffic-signs](https://bitbucket.org/jadslim/german-traffic-signs/src/master/) 

In the **Behavioral Cloning** project there is a folder names videos where there are 2 videos from the autonomous driving results of the car. The model
is subject to overfitting after training for more than 3 epochs. Therefore, the model that is working for both tracks is the one derived after the 
second epoch. 
The software is subject to changes and improvements. The most important ones are:
  * Make the steering more stable
  * Accelerate when driving in a straight line
  * Resolve the problem of overfitting 
  
For the implementation, I mostly used the Google Colab.
