# Face Recognition Attendance System

## Overview

The **Face Recognition Attendance System** that uses Local Binary Pattern Histogram (LBPH) and Haar Cascade classifier and take attendance in real-time. This system captures a person's face, identifies them using a pre-trained face recognition model, and logs their attendance into a CSV file with timestamps.

## Features

- Real-time face detection and recognition using the camera/webcam.
- Automatic attendance logging with names and timestamps.
- Pre-trained model for face recognition using `dlib` and `face_recognition` libraries.
- Simple and intuitive graphical user interface (GUI) for ease of use.
- Attendance stored in a CSV file for easy access and further processing.

## Demo
1. Interface (GUI)
 ![main](https://github.com/user-attachments/assets/6b9b0867-cea9-4a5b-89be-a310a3ce5c87)

2. Student Details
 ![image](https://github.com/user-attachments/assets/2e5be1d1-01ba-4c8c-b709-1a65b19f6e62)

3. Training
![image](https://github.com/user-attachments/assets/b0d38fc4-a39a-4364-9059-50253dec405e)

4. Face Recognition
![image](https://github.com/user-attachments/assets/be28aebd-03d2-459f-9aaa-9ec3b1d959ee)

5. Attendance
![image](https://github.com/user-attachments/assets/32dbc3bd-d927-4a3d-82d0-6f7a285ceb4d)

6. Face Recognition Test Case
![image](https://github.com/user-attachments/assets/1d54c3e5-e8ca-4a9f-9328-d105c63d87aa)

## Tech Stack

- **Language**: Python
- **Libraries**:
  - `OpenCV`: For real-time video capturing and processing.
  - `LBPH`: Used to recognize faces.
  - `Haar Cascade`: Used to detect faces in images and video in real-time.
  - `dlib`: For face detection.
  - `face_recognition`: For facial recognition.
  - `Tkinter`: For the GUI interface.
  - `Numpy`: For numerical operations.

## Installation

Follow these steps to set up and run the project on your local machine.

### Prerequisites

Make sure you have Python installed on your system. You can download it from [here](https://www.python.org/downloads/).

### Step-by-Step Setup

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/yashshekh/Face-Recognition-Attendance-System.git

2. Navigate to the project directory:

    ```bash
   cd Face-Recognition-Attendance-System

3. Install the required libraries:

    ```bash
   pip install opencv-python numpy dlib face_recognition

4. Run the application:

    ```bash
   python main.py

5. Optional: Configure Camera Settings
If you are using an external webcam or default camera, you can modify the camera index in the code by changing the parameter in the 'cv2.VideoCapture()' method.

    ```bash
   video_capture = cv2.VideoCapture(0)  # Default camera (0), change for external cameras

## Project Structure

├── known_faces/             # Folder containing images of known faces
├── attendance.csv           # CSV file for logging attendance
├── main.py                  # Main script to run the application
├── requirements.txt         # Required Python libraries
└── README.md                # Project documentation

   
   





