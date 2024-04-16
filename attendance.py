from tkinter import RIDGE, W, Button, Entry, Frame, Image, Label, LabelFrame, Tk
from tkinter import ttk
from tkinter import *
from PIL import Image
from PIL import ImageTk
from tkinter import messagebox
from tkinter import filedialog
import mysql.connector
import cv2
import csv
import os

mydata=[]
class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #==================variables==================
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()

         # first image
        img=Image.open(r"C:\Users\yashshekh\Downloads\student.jpeg")
        img=img.resize((1530,200),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1530,height=200)


        # heading
        title_lbl = Label(text="Attendance Management System", font=("times new roman", 35, "bold"), bg="white", fg="black")
        title_lbl.place(x=0, y=0, width=1530, height=45)

          
        self.create_left_frame()
        self.create_right_frame()

    
    def create_left_frame(self):
        # Left label frame
        left_frame = LabelFrame(self.root, borderwidth=2, bg="white", relief="ridge",
                                text="Student Attendance Details", font=("times new roman", 12, "bold"))
        left_frame.place(x=10, y=210, width=730, height=580)

        # Attendance frame
        attendance_frame = LabelFrame(left_frame, bd=2, bg="white", relief=RIDGE,
                                    text="Attendance Information", font=("times new roman", 12, "bold"))
        attendance_frame.place(x=5, y=50, width=710, height=400)

        # Attendance ID
        attendanceID_label = Label(attendance_frame, text="AttendanceId:", font=("times new roman", 15, "bold"), bg="white")
        attendanceID_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        attendanceID_entry = ttk.Entry(attendance_frame, width=30,textvariable=self.var_atten_id, font=("times new roman", 12, "bold"))
        attendanceID_entry.grid(row=0, column=1, padx=10, pady=10)

        # Student Roll
        rollLabel=Label(attendance_frame,text=" Roll:",font=("comicsansns 11 bold"),bg="white")
        rollLabel.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        rollLabel_entry=ttk.Entry(attendance_frame,width=30,textvariable=self.var_atten_roll,font=("comicsansns 11 bold"))
        rollLabel_entry.grid(row=1, column=1, padx=10, pady=10)

        # Name
        nameLabel = Label(attendance_frame, text="Name:", font=("times new roman", 15, "bold"), bg="white")
        nameLabel.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        nameLabel_entry = ttk.Entry(attendance_frame, width=30,textvariable=self.var_atten_name, font=("times new roman", 12, "bold"))
        nameLabel_entry.grid(row=2, column=1, padx=10, pady=10)

        # Department
        depLabel = Label(attendance_frame, text="Department:", font=("times new roman", 15, "bold"), bg="white")
        depLabel.grid(row=3, column=0, padx=10, pady=10, sticky="w")

        depLabel_entry = ttk.Entry(attendance_frame, width=30,textvariable=self.var_atten_dep, font=("times new roman", 12, "bold"))
        depLabel_entry.grid(row=3, column=1, padx=10, pady=10)

        # Time
        timLabel = Label(attendance_frame, text="Time:", font=("times new roman", 15, "bold"), bg="white")
        timLabel.grid(row=4, column=0, padx=10, pady=10, sticky="w")

        timLabel_entry = ttk.Entry(attendance_frame, width=30,textvariable=self.var_atten_time, font=("times new roman", 12, "bold"))
        timLabel_entry.grid(row=4, column=1, padx=10, pady=10)

        # Date
        dateLabel = Label(attendance_frame, text="Date:", font=("times new roman", 15, "bold"), bg="white")
        dateLabel.grid(row=5, column=0, padx=10, pady=10, sticky="w")

        dateLabel_entry = ttk.Entry(attendance_frame, width=30,textvariable=self.var_atten_date, font=("times new roman", 12, "bold"))
        dateLabel_entry.grid(row=5, column=1, padx=10, pady=10)

        # Attendance Status
        attendance_label = Label(attendance_frame, text="Attendance Status:", font=("times new roman", 15, "bold"), bg="white")
        attendance_label.grid(row=6, column=0, padx=10, pady=10, sticky="w")

        self.atten_combo = ttk.Combobox(attendance_frame, width=27,textvariable=self.var_atten_attendance, font=("times new roman", 12, "bold"), state="readonly")
        self.atten_combo["values"] = ("Status", "Present", "Absent")
        self.atten_combo.current(0)
        self.atten_combo.grid(row=6, column=1, padx=10, pady=10)

          # buttons frame
        btn_frame=Frame(attendance_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=340,width=715,height=35)

        import_btn=Button(btn_frame,text="Import csv",command=self.importCsv,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        import_btn.grid(row=0,column=0)

        export_btn=Button(btn_frame,text="Export csv",command = self.exportCsv,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        export_btn.grid(row=0,column=1)

        update_btn=Button(btn_frame,text="Update",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",width=17,command = self.reset_data,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)



    def create_right_frame(self):
        # Right label frame
        right_frame = LabelFrame(self.root, borderwidth=2, bg="white", relief="ridge",
                                 text="Attendance Details", font=("times new roman", 12, "bold"))
        right_frame.place(x=750, y=210, width=720, height=580)

        table_frame=Frame(right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=680,height=445)

         #===============scroll bar table==================
        scroll_x=ttk.Scrollbar(right_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(right_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(right_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)
        
        
        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")
        
        self.AttendanceReportTable["show"]="headings"
        
        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)
        
        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

    #=====================fetch data===========================        
    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)
     
    # import csv       
    def importCsv(self):
       global mydata
       mydata.clear()
       fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
       with open(fln) as myfile:
           csvread=csv.reader(myfile,delimiter=",")
           for i in csvread:
               mydata.append(i)
           self.fetchData(mydata) 

    # export csv
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export to","Your data exported to"+os.path.basename(fln)+"sucessfully")
        except Exception as es:
            messagebox.showerror('Error',f'Due to:{str(es)}',parent=self.root)
           
    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])     
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])
        
    def reset_data(self):
        self.var_atten_id.set("")     
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")



if __name__ == "__main__":
     root = Tk()
     obj = Attendance(root)
     root.mainloop()