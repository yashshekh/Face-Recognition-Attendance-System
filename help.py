from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import webbrowser

class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")

        
        title_lbl=Label(self.root,text="SUPPORT",font=("time new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_top=Image.open(r"C:\Users\yashshekh\Downloads\support.jpg")
        img_top=img_top.resize((1530,720),Image.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=720)
       
        # Create a clickable email label
        dev_label = Label(f_lbl, text="Email: hkun89828@gmail.com", font=("time new roman", 20, "bold"), bg="white", fg="blue", cursor="hand2")
        dev_label.place(x=60, y=270)

        # Bind the label to a function that opens the default email application
        dev_label.bind("<Button-1>", self.open_email)

    def open_email(self, event):
        # Open the default email application with the specified email address
        webbrowser.open("mailto:hkun89828@gmail.com")
        
        
        
        
if __name__ == "__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()