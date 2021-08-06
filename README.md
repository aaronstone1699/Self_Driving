# Self_Driving

## dataset
For the first phase of this study.ie. in the semantic segmentation stage we have used the Mapillary Vistas Dataset, a novel, large scale street-level image dataset containing 25,000 high resolution images annotated into 66 object categories with additional, instance-specific labels for 37 classes. Annotation is performed in a dense and fine-grained style by using polygons for delineating individual objects. The dataset is 5× larger than the total amount of fine annotations for Cityscapes and contains images from all around the world, captured at various conditions regarding weather, season and daytime. 

For the traffic sign detection stage we have used the TSDD dataset which includes 10000 traffic scene images containing many kinds of signs. The images are collected under different time,weather conditions,lighting conditions as well as moving blurring.

For the final training we have used a custom dataset created on a specifically created scenario with the model car driven manually on 2 separate tracks and the 2 minute videos of each track from the camera mounted on the model car,resulting in 24000 images along with additional data like ir sensor data and steering angles.

## Proposed Method
Our method works by a cooperative operation between an arduino which acts as a drive unit and a raspberry pi which acts as the brain.The arduino is connected to an h-bridge which controls 2 geared dc motors and 1 servo motor, the arduino is further connected to 3 ir sensors which measure the distance between the objects on 3 sides.The arduino sends data to the raspberry pi through usb bus and receives serial instruction from the pi after he raw dat has been processed and a prediction has been made.

### Pre Training Phase
For the training of our final model we need the images to be available in a processed form instead of in the raw form.For this step/ we first semantically segment the images into various objects (from 1 of 128) so the images from any scenario could be generalised.Then from the segmented images the traffic sign segment is extracted and sent to a classifier for the classification between various types of traffic signs.

### Data Collection Phase
#### Camera data: 
the camera mounted on top of the car provides a constant feed of 256*256*3 images of the path which is passed to the image segmentation with weights taken from the previous stage and the traffic sign classification model ,this step results in a processed segmented image and the label array with direction.
#### Arduino sensor data : 
the arduino is connected to 3 ir proximity sensors which are mounted on the back,right and left sides of the vehicle and relay the 0/1 information of whether the vehicle is in close proximity with another object.

These sensor and camera datas are processed using the pretrained models (UNet for segmentation and CNN for traffic light classification).This information is arranged in a [length,5] numpy array ,where each element contains [ir_sensor_right,ir_sensor_left,ir_sensor_back,traffic_light,image(segmented)],this data is appended with the direction logged from the user which is one from {f,b,l,r,s}.

### Final Training Phase
The pre-trained models and the collected sensor data is brought together and the vehicle is driven manually across 2 tracks for the training of the deep learning model which can be used to predict the moves in a testing scenario. 

## Hardware Requirement

150 RPM dual shaft geared motor
5000 mAh lithium polymer power bank
5V 0.2A Cooling Fan
Raspberry Pi 4 b
Raspberry pi 4 heatsink
Battery holder case 4x 1.5V AA
IR Proximity Sensor
NiMH 3000mAh battery
Raspberry pi 5MP camera
L293D Motor Shield
16GB MicroSDHC
Arduino Uno
Wheels 2.5’’
Laptop 
BreadBoard
Jumper Cables(m-m,f-m,f-f) 
USB A to USB B cable
LED







