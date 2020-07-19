# Face-Recognition-Flask-App

The Facial Regognition Flask App to identify gender from images and videos using Machine Learning model to classify the images, between Male and Female. The project uses SVM, Numpy,
Pandas , Matplotlib , PIL , CV2 , Sci-kit Learn. 

The dependecies can be downloaded as follows-
To install flask

>pip install Flask

To Install all other dependencies

> pip install scikit-learn, numpy, pandas, opencv-python

## Main.py is the main runner file which has all the url rules and flask app initialization with all the url rules
## Views.py returns all the templates to the main.py to be displayed by creating a server.
## Util.py contains the pipeline program which starts with loading the image -> scaling the image -> Grayscaling the image -> Cropping the face -> turning the cropped image into Eigan images
-> Putting the eigan images into Machine learning model -> Predicting the images -> Showing the Output as the square around the face with the probablity of confidence.
