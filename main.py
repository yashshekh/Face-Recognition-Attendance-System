from tkinter import Button, Label, Tk, Toplevel
from typing import Any
from PIL import Image
from PIL import ImageTk
import os
import threading
import tkinter
from time import strftime
from student import Student
from train import Train
from face_recognition import FaceRecognition
from attendance import Attendance
from help import Help
from chatbot import ChatBot

class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        

        # First heading
        title_lbl = Label(self.root,text="Face Recognition Attendance System", font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)
        

        #button student
        img5 = Image.open(r"C:\Users\yashshekh\Downloads\student.jpeg")
        img5 = img5.resize((220, 220), Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(image=self.photoimg5,command=self.student_details, cursor="hand2")
        b1.place(x=200, y=100, width=220, height=220)

        b1_1 = Button(text="Student Details",command=self.student_details, cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200, y=300, width=220, height=40)

          #===================time==============
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000, time)
            
        lbl = Label(title_lbl, font = ('times new roman' , 14, 'bold'),background= 'white' , foreground = 'blue')
        lbl.place(x=0,y=0,width=110,height=50)
        time()


        #Detect face button
        img6 = Image.open(r"C:\Users\yashshekh\Downloads\facedetector.jpg")
        img6 = img6.resize((220, 220), Image.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1 = Button(image=self.photoimg6, cursor="hand2",command=self.face_data)
        b1.place(x=500, y=100, width=220, height=220)

        b1_1 = Button(text="Face Detector",command=self.face_data,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500, y=300, width=220, height=40)


        #Attendance button
        img7 = Image.open(r"C:\Users\yashshekh\Downloads\attendance.jpeg")
        img7 = img7.resize((220, 220), Image.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1 = Button(image=self.photoimg7, cursor="hand2",command=self.attendance_data)
        b1.place(x=800, y=100, width=220, height=220)

        b1_1 = Button(text="Attendance", cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=800, y=300, width=220, height=40)


        #Help button
        img8 = Image.open(r"C:\Users\yashshekh\Downloads\support.jpg")
        img8 = img8.resize((220, 220), Image.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1 = Button(image=self.photoimg8, cursor="hand2",command=self.help_data)
        b1.place(x=1100, y=100, width=220, height=220)

        b1_1 = Button(text="Support", cursor="hand2",command=self.help_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1100, y=300, width=220, height=40)

       
        #Train face button
        img9 = Image.open(r"C:\Users\yashshekh\Downloads\train.jpg")
        img9 = img9.resize((220, 220), Image.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1 = Button(image=self.photoimg9, cursor="hand2",command=self.train_data)
        b1.place(x=200, y=450, width=220, height=220)

        b1_1 = Button(text="Train Data", cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200, y=650, width=220, height=40)
        

        #Photos face button
        img10 = Image.open(r"C:\Users\yashshekh\Downloads\photos.jpg")
        img10 = img10.resize((220, 220), Image.LANCZOS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b1 = Button(image=self.photoimg10, cursor="hand2",command=self.open_img)
        b1.place(x=500, y=450, width=220, height=220)

        b1_1 = Button(text="Photos", cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500, y=650, width=220, height=40)
        

        #Chatbot button
        img11 = Image.open(r"C:\Users\yashshekh\Downloads\friendly-chatbot.jpeg")
        img11 = img11.resize((220, 220), Image.LANCZOS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b1 = Button(image=self.photoimg11, cursor="hand2",command=self.chatbot)
        b1.place(x=800, y=450, width=220, height=220)

        b1_1 = Button(text="Friendly Chatbot", cursor="hand2",command=self.chatbot,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=800, y=650, width=220, height=40)

        
        #Exit button
        img12 = Image.open(r"C:\Users\yashshekh\Downloads\exit.png")
        img12 = img12.resize((220, 220), Image.LANCZOS)
        self.photoimg12 = ImageTk.PhotoImage(img12)

        b1 = Button(image=self.photoimg12, cursor="hand2",command=self.IExit)
        b1.place(x=1100, y=450, width=220, height=220)

        b1_1 = Button(text="Exit", cursor="hand2",command=self.IExit,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1100, y=650, width=220, height=40)

        def open_img(self):
            os.startfile("data")
        
    def IExit(self):
        self.IExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure you want to exit?",parent=self.root)
        if self.IExit >0:
            self.root.destroy()
        else:
            return

    def open_img(self):
        os.startfile("data")
       
       #===========function button===========
       
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=FaceRecognition(self.new_window)

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)

    def chatbot(self):
        self.new_window=Toplevel(self.root)
        self.app=ChatBot(self.new_window)



if __name__ == "__main__":
    root1 = Tk()
    obj1 = Face_Recognition_System(root1)
    root1.mainloop()

