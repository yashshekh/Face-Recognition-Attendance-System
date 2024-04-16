from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from datetime import datetime
import mysql.connector
import cv2
import time
import os
import threading
import csv
import numpy as np

class FaceRecognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="Face Recognition", font=("times new roman", 35, "bold"), bg="white", fg="black")
        title_lbl.place(x=0, y=0, width=1530, height=45)
        
        # Load and display image
        # First image
        img_top = Image.open(r"C:\Users\yashshekh\Downloads\face.jpeg")
        img_top = img_top.resize((650, 700), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=650, height=700)
        
        # Second Image
        img_bottom = Image.open(r"C:\Users\yashshekh\Downloads\recognizer.jpeg")
        img_bottom = img_bottom.resize((950, 700), Image.LANCZOS)
        self.photoimg_bottom= ImageTk.PhotoImage(img_bottom)
        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=650, y=55, width=950, height=700)

        # button
        b1_1 = Button(f_lbl, command=self.face_recog, text="Face Recognition", cursor="hand2", font=("times new roman", 15, "bold"), bg="dark green", fg="white")
        b1_1.place(x=365, y=620, width=200, height=40)
      #=================attendance==============
        self.attendance_file = "Attendance.csv"
        self.create_attendance_file()
        self.recognized_ids = set()

    def create_attendance_file(self):
        if not os.path.exists(self.attendance_file):
            with open(self.attendance_file, "w", newline="\n") as f:
                f.write("ID, Roll Number, Name, Department, Time, Date, Status\n")

    def mark_attendance(self,i,r,n,d):
        with open("Attendance.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry= line.split((",")) 
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now=datetime.now() 
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")   
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present{i}")  

    def start_face_recog(self):
        self.thread = threading.Thread(target=self.face_recog)
        self.thread.start()

    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            features = classifier.detectMultiScale(
                gray_image, scaleFactor=1.2, minNeighbors=5)

            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y+h, x:x+w])
                confidence = int((100*(1-predict/300)))

                coord = []

                conn = mysql.connector.connect(host='localhost', user='root', password='1234', database='systemattendance')
                my_cursor = conn.cursor()

                my_cursor.execute("select Name from student where Student_id="+str(id))
                n = my_cursor.fetchone()

                n = str(n)
                print(n)
                # n="+".join(n)

                my_cursor.execute("select RollNo from student where Student_id="+str(id))
                r=my_cursor.fetchone()
                r = str(r)
                # r = "+".join(r)

                
                my_cursor.execute("select Department from student where Student_id="+str(id))
                d=my_cursor.fetchone()
                d = str(d)
                # d = "+".join(d)

                my_cursor.execute("select Student_id from student where Student_id="+str(id))
                i=my_cursor.fetchone()
                i = str(i)
                # i = "+".join(i)
                
                # new code for accuracy calculation
                # img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                # result = id.predict(img)

                if predict < 500:
                # if result[1] < 500:
                    confidence=int((100*(1-predict/300)))
                    # str2 = str(confidence)
                    # confidence = int(100 * (1 - (result[1])/300))
                    # display_string = str(confidence)+'% confidence it is user'
                # cv2.putText(img,display_string(250, 250), cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),3)
                    cv2.putText(img,f"Accuracy:{confidence}%",(x, y-100), cv2.FONT_HERSHEY_COMPLEX,0.8,(0,255,0),3)
                
                if confidence > 80:
                    cv2.putText(img, f"Id:{i}", (x, y-75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Roll:{r}", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Name:{n}", (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Department:{d}", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    self.mark_attendance(i,r,n,d)
            
                else:
                    cv2.rectangle(img,(x, y), (x+w, y+h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y-5),cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                coord = [x, y, w, y]

            return coord

        def recognize(img, clf, faceCascade):
           coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
           return img
        
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer.create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            # Adjust scaleFactor and minNeighbors values for better face detection
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to Face Recognition",img)

            if cv2.waitKey(1)== 13:
                break
        video_cap.release()
        cv2.destroyAllWindows()
        
if __name__ == "__main__":
    root = Tk()
    obj = FaceRecognition(root)
    root.mainloop()
