# Computer-Vision-Python-GUI-Project
This is a computer vision project using the OpenCV library integrated with GUI using the PyQt5 library. This project consists of a supermarket analyzer used to analyze supermarket activity and hand gesture recognition using the MediaPipe library. Besides that, this project is also integrated with Firebase as the online database for the user.

## Login Page

The login page is designed using the Qt Designer app, which consists of buttons to help users use the application easily. Besides that, I also added a signup page that will direct new users to create an account on the application. Both the signup and login pages are integrated with Firebase as the online database. Using Firebase, the administrator could easily monitor the application activity since it is also provided with a graph to make it easily visualized.

![Computer Vision Python GUI Project](https://github.com/wiryanatasunardi/Computer-Vision-Python-GUI-Project/blob/main/Documentation/login.jpg)
![Computer Vision Python GUI Project](https://github.com/wiryanatasunardi/Computer-Vision-Python-GUI-Project/blob/main/Documentation/signup.jpg)

## Home Page
The main page or the home page is themed modern GUI where there are so many features inside such as a profile section, notification, sign out, the application detail, and the main features such as supermarket analyzer that is used to track supermarket-activity based on body detection and hand gesture recognition that is used to translate hand gesture to establish a complete sentence.

![Computer Vision Python GUI Project](https://github.com/wiryanatasunardi/Computer-Vision-Python-GUI-Project/blob/main/Documentation/home_profile.jpg)
![Computer Vision Python GUI Project](https://github.com/wiryanatasunardi/Computer-Vision-Python-GUI-Project/blob/main/Documentation/home.jpg)

## Supermarket Analyzer
Supermarket Analyzer analyzes supermarket activity based on body detection using the Mediapipe library. Using computer vision to analyze supermarket activity, it can receive various inputs such as the amount of activity in a certain period and the average duration the action occurs in a specific aisle in a supermarket. After the analyzer's window has been closed, the GUI will generate the activity's statistic graph using the Matplotlib library.

![Computer Vision Python GUI Project](https://github.com/wiryanatasunardi/Computer-Vision-Python-GUI-Project/blob/main/Documentation/supermarket.jpg)
![Computer Vision Python GUI Project](https://github.com/wiryanatasunardi/Computer-Vision-Python-GUI-Project/blob/main/Documentation/supermarket%20graph.jpg)

## Hand Gesture Recognition
Hand Gesture Recognition is my computer vision project using the Mediapipe library that can analyze and recognize hand gestures based on the user hand landmark model. The ability to perceive the shape and motion of hands can be a vital component in improving the user experience across various technological domains and platforms. MediaPipe Hands is a high-fidelity hand and finger tracking solution. It employs machine learning (ML) to infer 21 3D landmarks of a hand from just a single frame. Integrating the Hand Gesture Recognition project with Python GUI will make the task easier to use since the Hand Gesture Recognition needs to train the model before the model can be used for recognizing hand gestures. The hand gestures model that has been prepared will be saved in the user's local drive in a pickle file and can be opened whenever the user wants to use the recognition feature.

![Computer Vision Python GUI Project](https://github.com/wiryanatasunardi/Computer-Vision-Python-GUI-Project/blob/main/Documentation/hand_train.jpg)
![Computer Vision Python GUI Project](https://github.com/wiryanatasunardi/Computer-Vision-Python-GUI-Project/blob/main/Documentation/hand_recog.jpg)

## Acknowledgement
- [Mediapipe for Hand Detection and Pose Estimation](https://www.youtube.com/watch?v=xHK-wv2JG18&list=PLGs0VKk2DiYyXlbJVaE8y1qr24YldYNDm&index=32)
- [Mediapipe Hands](https://google.github.io/mediapipe/solutions/hands.html)
- [Mediapipe Library](https://google.github.io/mediapipe/)

## Authors
-  LinkedIn  - [Wiryanata Sunardi](https://www.linkedin.com/in/wiryanata/)
-  Instagram - [wiryanatasunardi](https://www.instagram.com/wiryanatasunardi/)
