from tkinter import *
from tkinter import ttk
from tkinter import Tk, Button, Label, messagebox 
from PIL import Image, ImageTk
import cv2
import os
import mysql.connector
import numpy as np

class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # heading
        title_lbl = Label(self.root, text="Train Data Set", font=("times new roman", 35, "bold"), bg="white", fg="black")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Load and display image
        img_top = Image.open(r"C:\Users\yashshekh\Downloads\traindata.jfif")
        img_top = img_top.resize((1530, 325), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1530, height=325)

        # Button to start training
        b1_1 = Button(self.root, text="Train Data", command=self.train_classifier, cursor="hand2", font=("times new roman", 30, "bold"), bg="blue", fg="white")
        b1_1.place(x=0, y=380, width=1530, height=60)

        # Placeholder for bottom image
        img_bottom = Image.open(r"C:\Users\yashshekh\Downloads\traindata1.jpg")
        img_bottom = img_bottom.resize((1530, 325), Image.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=0, y=440, width=1530, height=325)

  
    def train_classifier(self):
        data_dir = ("data")
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        ids = []


        for image_path in path:
            if image_path.endswith('.jpg'):  # Filter only JPG files
                img = Image.open(image_path).convert('L')  # Convert to grayscale image
                imageNp = np.array(img, 'uint8')
                id = int(os.path.split(image_path)[1].split('.')[0].split('_')[-1])  # Extract ID from file name
                faces.append(imageNp)
                ids.append(id)


                cv2.imshow("Training", imageNp)
                if cv2.waitKey(1) & 0xFF == 13:
                    break

        ids = np.array(ids)
  

        # Train Classifier using LBPH algorithm
        clf = cv2.face.LBPHFaceRecognizer.create()
        clf.train(faces, ids)
        clf.save("classifier.xml")
       
        cv2.destroyAllWindows()
        # Display messagebox after training
        messagebox.showinfo("Result", "Training Dataset Completed!!")
       

if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()