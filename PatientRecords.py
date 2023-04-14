from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

import mysql.connector as sqltor

con = sqltor.connect(host="localhost", user="root", passwd="123456", database="patient_rec")
if con.is_connected():
    print("Connection Successful...")



class Patient:
    def __init__(self,root):
        self.root=root
        self.root.title("Patient Record System")
        self.root.geometry("1360x694+0+0")

        lbltitle=Label(self.root,bd=20,relief=RIDGE,
                       text="➕PATIENT RECORDS",fg="light green",bg="white",font=("times new roman",50,"bold"))
        lbltitle.pack(side=TOP,fill=X)

        # ======================================DataFrame========================
        Dataframe=Frame(self.root,bd=15,relief=RIDGE)
        Dataframe.place(x=0,y=130,width=1360,height=500)

        DataframeLeft=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,
                                 font=("arial",18,"bold"),text="Patient Information", fg="gray" )
        DataframeLeft.place(x=6,y=5,width = 976,height = 460 )

        # ========================================== buttons =====================================

        Buttonframe = Frame(self.root, bd=15, relief=RIDGE)
        Buttonframe.place(x=0, y=628, width=1360, height=65)

        def addRec():
            patientNameVar = entry_name.get()
            ageVar = txtage.get()
            DOBVar = txtdob.get()
            genderVar = gender_comobobox.get()
            PatientIDVar = txtpatientID.get()
            MobVar = txtmobilenumber.get()
            BloodTypeVar = txtbloodtype.get()
            BPVar = txtbp.get()
            HeightVar = txtheight.get()
            weightVar = txtweight.get()
            addressVar = txtaddress.get(1.0, END)
            complaintVar = txtComplaint.get(1.0, END)
            diagnosisVar = txtDiagnosis.get(1.0, END)
            prevMedVar = txtprevious_medication.get(1.0, END)
            prescribedMedVar = txtPrescribed_Medication.get(1.0, END)
            qry1="INSERT INTO records(PatientName,Age,DOB,Gender,PatientID,Mobile,BloodType,BP,Height,Weight,Address,PatientComplaint,PatientDiagnosis,PreviousMedication,PrescribedMedication)values('{}',{},'{}','{}','{}',{},'{}','{}',{},{},'{}','{}','{}','{}','{}')".format(patientNameVar,
                                                                                                                                                                                                                                                                                  ageVar,
                                                                                                                                                                                                                                                                                  DOBVar,
                                                                                                                                                                                                                                                                                  genderVar,
                                                                                                                                                                                                                                                                                  PatientIDVar,
                                                                                                                                                                                                                                                                                  MobVar,
                                                                                                                                                                                                                                                                                  BloodTypeVar,
                                                                                                                                                                                                                                                                                  BPVar,
                                                                                                                                                                                                                                                                                  HeightVar,
                                                                                                                                                                                                                                                                                  weightVar,
                                                                                                                                                                                                                                                                                  addressVar,
                                                                                                                                                                                                                                                                                  complaintVar,
                                                                                                                                                                                                                                                                                  diagnosisVar,
                                                                                                                                                                                                                                                                                  prevMedVar,
                                                                                                                                                                                                                                                                                  prescribedMedVar)
            cursor1 = con.cursor()
            cursor1.execute(qry1)
            con.commit()

            messagebox.showinfo(message="Patient Data Was Recorded Successfully...")

        def delRec():
            PatientIDVar = txtpatientID.get()
            qry2 = "DELETE FROM records where PatientID = {}".format(PatientIDVar)
            cursor2 = con.cursor()
            cursor2.execute(qry2)
            con.commit()

            messagebox.showinfo(message="Patient Data Was Deleted successfully...")

        button1 = Button(root,
                        text="Add Details",
                        font=("Arial", 12, "bold"),
                        padx=275,
                        bg="light gray",
                        command=addRec)
        button1.place(x=16, y=644)

        button2 = Button(root,
                        text="Delete Details",
                        font=("Arial", 12, "bold"),
                        padx=281,
                        bg="light gray",
                        command=delRec)
        button2.place(x=666, y=644)




        # ==========================labels and entrys=============================
        #1 patient name
        lbl_patient_name= Label(DataframeLeft,text ="Patient Name",font=("arial",12,"bold"),padx= 2, pady=6)
        lbl_patient_name.grid(row = 0,column=0,sticky =W )
        entry_name = Entry(DataframeLeft,width=26,font =("arial",12,"bold"))
        entry_name.grid(row=0,column =1)

        #2 age
        age = Label(DataframeLeft,text ="Age",font=("arial",12,"bold"),padx= 2, pady=6)
        age.grid(row=1, column=0, sticky=W)
        txtage=ttk.Entry(DataframeLeft,width=26, font=("arial", 12, "bold"))
        txtage.grid(row=1,  column=1)

        #3 DOB
        dob = Label(DataframeLeft,text ="DOB",font=("arial",12,"bold"),padx= 2, pady=6)
        dob.grid(row=2, column=0, sticky=W)
        txtdob=ttk.Entry(DataframeLeft,width=26, font=("arial", 12, "bold"))
        txtdob.grid(row=2,  column=1)

        #4 gender combobox
        gender= Label(DataframeLeft,text="Gender", font=("arial", 12, "bold"), padx=2, pady=6)
        gender.grid(row=3, column=0,sticky = W )
        gender_comobobox = ttk.Combobox(DataframeLeft, font=("arial", 12, "bold"),width =24)
        gender_comobobox["values"]=("Male","Female","Other")
        gender_comobobox.grid(row=3, column=1)
        gender_comobobox.current(0)

        #5 Patient ID
        patientID = Label(DataframeLeft,text ="Patient ID",font=("arial",12,"bold"),padx= 2, pady=6)
        patientID.grid(row=4, column=0, sticky=W)
        txtpatientID=ttk.Entry(DataframeLeft, width=26, font=("arial", 12, "bold"))
        txtpatientID.grid(row=4,  column=1)

        #6 mobile number
        mobilenumber = Label(DataframeLeft,text ="Mobile Number",font=("arial",12,"bold"),padx= 2, pady=6)
        mobilenumber.grid(row=5, column=0, sticky=W)
        txtmobilenumber=ttk.Entry(DataframeLeft, width=26,font=("arial", 12, "bold"))
        txtmobilenumber.grid(row=5,  column=1)

        #7 BLOOD TYPE
        bloodtype = Label(DataframeLeft,text ="Blood Type",font=("arial",12,"bold"),padx= 2, pady=6)
        bloodtype.grid(row=6, column=0, sticky=W)
        txtbloodtype=ttk.Entry(DataframeLeft, width=26, font=("arial", 12, "bold"))
        txtbloodtype.grid(row=6,  column=1)

        #8 Blood Pressure
        bp =Label(DataframeLeft,text ="BP",font=("arial",12,"bold"),padx= 2, pady=6)
        bp.grid(row=7, column=0, sticky=W)
        txtbp=ttk.Entry(DataframeLeft, width=26, font=("arial", 12, "bold"))
        txtbp.grid(row=7,  column=1)

        #9 Height
        height =Label(DataframeLeft,text ="Height",font=("arial",12,"bold"),padx= 2, pady=6)
        height.grid(row=8,column = 0 ,sticky =W)
        txtheight=ttk.Entry(DataframeLeft, width=26, font=("arial", 12, "bold"))
        txtheight.grid(row=8,  column=1)

        #10 Weight
        weight = Label(DataframeLeft,text ="Weight",font=("arial",12,"bold"),padx= 2, pady=6,)
        weight.grid(row=9, column=0, sticky=W)
        txtweight=ttk.Entry(DataframeLeft, width=26, font=("arial", 12, "bold"))
        txtweight.grid(row=9,  column=1)

        #11  address
        address = Label(DataframeLeft,text="Address",font=("arial",12,"bold"),padx= 2,pady=6)
        address.grid(row=10, column=0, sticky=W)
        txtaddress=Text(DataframeLeft, height=3, width=29, font=("arial", 11, "bold"))
        txtaddress.place(x=125,y=355)



        #=================================iamage===============================

        img = Image.open("hospitalOrg1.png")
        img = img.resize((317, 448), Image.ANTIALIAS)
        self.Photoimg = ImageTk.PhotoImage(img)
        lblimg = Label(self.root, image=self.Photoimg, bd=4, relief=RIDGE)
        lblimg.place(x=1013, y=160, width=317, height=448)

        #================================right side============================================================
        #empty column
        empty = Label(DataframeLeft,text="                      ",font=("arial",12,"bold"),padx= 2,pady=6)
        empty.grid(row=1, column=3, sticky=W)

        #12  Patient Complaint
        Complaint = Label(DataframeLeft,text="Patient Complaint",font=("arial",12,"bold"),padx= 2,pady=6)
        Complaint.grid(row=0, column=4, sticky=W)
        txtComplaint=Text(DataframeLeft, height=7, width=36, font=("arial", 11, "bold"))
        txtComplaint.place(x=640,y=0)
        #13 Diagnosis
        Diagnosis = Label(DataframeLeft,text="Patient Diagnosis",font=("arial",12,"bold"),padx= 2,pady=6)
        Diagnosis.grid(row=4, column=4, sticky=W)
        txtDiagnosis=Text(DataframeLeft, height=7, width=36, font=("arial", 11, "bold"))
        txtDiagnosis.place(x=640,y=140)

        #14  Previous Medication
        previous_medication = Label(DataframeLeft,text="Previous Medication",font=("arial",12,"bold"),padx= 2,pady=6)
        previous_medication.grid(row=8, column=4, sticky=W)
        txtprevious_medication=Text(DataframeLeft, height=3, width=36, font=("arial", 11, "bold"))
        txtprevious_medication.place(x=640,y=282)

        #15  Prescribed Medication
        Prescribed_Medication = Label(DataframeLeft,text="Prescribed Medication",font=("arial",12,"bold"),padx= 2,pady=6)
        Prescribed_Medication.grid(row=10, column=4, sticky=W)
        txtPrescribed_Medication=Text(DataframeLeft, height=3, width=36, font=("arial", 11, "bold"))
        txtPrescribed_Medication.place(x=640,y=355)


root=Tk()
ob=Patient(root)
root.mainloop()
