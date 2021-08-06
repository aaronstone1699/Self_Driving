# Self_Driving

## dataset
For the first phase of this study.ie. in the semantic segmentation stage we have used the Mapillary Vistas Dataset, a novel, large scale street-level image dataset containing 25,000 high resolution images annotated into 66 object categories with additional, instance-specific labels for 37 classes. Annotation is performed in a dense and fine-grained style by using polygons for delineating individual objects. The dataset is 5× larger than the total amount of fine annotations for Cityscapes and contains images from all around the world, captured at various conditions regarding weather, season and daytime. 

For the traffic sign detection stage we have used the TSDD dataset which includes 10000 traffic scene images containing many kinds of signs. The images are collected under different time,weather conditions,lighting conditions as well as moving blurring.

For the final training we have used a custom dataset created on a specifically created scenario with the model car driven manually on 2 separate tracks and the 2 minute videos of each track from the camera mounted on the model car,resulting in 24000 images along with additional data like ir sensor data and steering angles.

## Proposed Method
Our method works by a cooperative operation between an arduino which acts as a drive unit and a raspberry pi which acts as the brain.The arduino is connected to an h-bridge which controls 2 geared dc motors and 1 servo motor, the arduino is further connected to 3 ir sensors which measure the distance between the objects on 3 sides.The arduino sends data to the raspberry pi through usb bus and receives serial instruction from the pi after he raw dat has been processed and a prediction has been made.




