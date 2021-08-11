from tkinter import *
from tkinter import ttk

import mysql as mysql
import mysql.connector

from tkinter import messagebox
from PIL import Image, ImageTk




class PharmacyManagementSystem:

    def __init__(self, root):

        self.root = root
        self.root.title("Pharmacy Management System")
        # self.root.attributes("-fullscreen", TRUE)
        self.root.geometry("1350x950+0+0")






        # ============= add Medicine Variable ===============

        self.Ref = StringVar()
        self.MedName = StringVar()






        # ============== add data variable ==================

        self.ref = StringVar()
        self.comName = StringVar()
        self.medType = StringVar()
        self.medName = StringVar()
        self.lotNo = StringVar()
        self.issueDate = StringVar()
        self.expDate = StringVar()
        self.uses = StringVar()
        self.sideEff = StringVar()
        self.precWar = StringVar()
        self.dosage = StringVar()
        self.tabPrice = StringVar()






        # ===================================================

        l1 = Label(self.root, text="Pharmacy Management System", bd=15, relief=RIDGE, fg="white", bg="darkGreen",
                   font=("times new roman", 50, "bold"), padx=2, pady=4)
        l1.pack(side=TOP, fill=X)

        i1 = Image.open("image/a.png")
        i1 = i1.resize((90, 80), Image.ANTIALIAS)
        self.photo1 = ImageTk.PhotoImage(i1)
        b1 = Button(self.root, image=self.photo1, borderwidth=0)
        b1.place(x=60, y=16)






        # ============ data frame =============

        DataFrame = Frame(self.root, bd=15, relief=RIDGE, padx=20)
        DataFrame.place(x=0, y=120, width=1279, height=400)

        DataFrameLeft = LabelFrame(DataFrame, bd=15, relief=RIDGE, text="Medicine Information", fg="darkGreen",
                                   font=("times new roman", 20, "bold"))
        DataFrameLeft.place(x=0, y=5, height=352, width=700)

        DataFrameRight = LabelFrame(DataFrame, bd=15, relief=RIDGE, text="Medicine Add Department", fg="darkGreen",
                                    font=("times new roman", 20, "bold"))
        DataFrameRight.place(x=710, y=5, height=352, width=500)







        # ============== button frame ==============

        ButtonFrame = Frame(self.root, bd=15, relief=RIDGE, padx=20)
        ButtonFrame.place(x=0, y=535, height=65, width=1279)






        # ============ main button ===============

        btnAddData = Button(ButtonFrame, command=self.AddMedicineData, bg="darkGreen", fg="white",
                            font=("times new roman", 13, "bold"),
                            text="Add Medicine")
        btnAddData.place(x=0, y=0, height=35, width=115)

        btnUpdateMed = Button(ButtonFrame, command=self.Update, bg="darkGreen", fg="white",
                              font=("times new roman", 13, "bold"),
                              text="Update")
        btnUpdateMed.place(x=116, y=0, height=35, width=115)

        btnDeleteMed = Button(ButtonFrame, command=self.Delete, bg="red", fg="white",
                              font=("times new roman", 13, "bold"),
                              text="Delete")
        btnDeleteMed.place(x=232, y=0, height=35, width=115)

        btnResetMed = Button(ButtonFrame, command=self.Reset, bg="darkGreen", fg="white",
                             font=("times new roman", 13, "bold"),
                             text="Reset")
        btnResetMed.place(x=348, y=0, height=35, width=115)

        btnExitMed = Button(ButtonFrame, command=self.Exit, bg="darkGreen", fg="white", font=("times new roman", 13, "bold"),
                            text="Exit")
        btnExitMed.place(x=464, y=0, height=35, width=115)







        # ============= search by ==============

        l2 = Label(ButtonFrame, text="Search By", font=("times new roman", 13, "bold"), padx=2, bg="blue", fg="white")
        l2.place(x=632, y=0, height=35, width=115)




        # ================ variable ================

        self.combo_var = StringVar()
        self.entry_var = StringVar()






        combo = ttk.Combobox(ButtonFrame, textvariable=self.combo_var, font=("times new roman", 13, "bold"), state="readonly")
        combo["values"] = ("ref", "medName", "lotNo")
        combo.current(0)
        combo.place(x=749, y=0, height=35, width=115)

        txtSearch = Entry(ButtonFrame, textvariable=self.entry_var, bd=3, relief=RIDGE, font=("times new roman", 13, "bold"))
        txtSearch.place(x=864, y=0, height=35, width=115)

        btnSearch = Button(ButtonFrame, command=self.SearchData, bg="darkGreen", fg="white", font=("times new roman", 13, "bold"),
                           text="Search")
        btnSearch.place(x=980, y=0, height=35, width=115)

        btnShowall = Button(ButtonFrame, command=self.FetchDataBottom, bg="darkGreen", fg="white", font=("times new roman", 13, "bold"),
                            text="Show All")
        btnShowall.place(x=1096, y=0, height=35, width=115)






        # ============ label and ref number =============

        l3 = Label(DataFrameLeft, text="Reference No", font=("times new roman", 17, "bold"), padx=2)
        l3.place(x=30, y=15, height=35, width=140)

        conn = mysql.connector.connect(host="localhost", username="root", password="root",
                                       database="pharma")
        my_cursor = conn.cursor()
        my_cursor.execute("select ref from MedAddDept")
        row = my_cursor.fetchall()

        cb1 = ttk.Combobox(DataFrameLeft, textvariable=self.ref, font=("times new roman", 13, "bold"),
                               state="readonly")
        cb1["values"] = row
        cb1.current(0)
        cb1.place(x=210, y=15, height=35, width=115)






        l4 = Label(DataFrameLeft, text="Company Name", font=("times new roman", 17, "bold"), padx=2)
        l4.place(x=27, y=60, height=35, width=170)

        l4t1 = Entry(DataFrameLeft, textvariable=self.comName, bd=3, relief=RIDGE, font=("times new roman", 13, "bold"))
        l4t1.place(x=210, y=60, height=35, width=115)






        l5 = Label(DataFrameLeft, text="Medicine Type", font=("times new roman", 17, "bold"), padx=2)
        l5.place(x=22, y=105, height=35, width=170)

        combol5 = ttk.Combobox(DataFrameLeft, textvariable=self.medType, font=("times new roman", 13, "bold"),
                               state="readonly")
        combol5["values"] = ("Tablet", "Liquid", "Capsule", "Topical Medicine", "Drop", "Inhale", "Injection")
        combol5.current(0)
        combol5.place(x=210, y=105, height=35, width=115)






        l6 = Label(DataFrameLeft, text="Medicine Name", font=("times new roman", 17, "bold"), padx=2)
        l6.place(x=27, y=150, height=35, width=170)

        conn = mysql.connector.connect(host="localhost", username="root", password="root",
                                       database="pharma")
        my_cursor = conn.cursor()
        my_cursor.execute("select medName from MedAddDept")
        row1 = my_cursor.fetchall()

        combol6 = ttk.Combobox(DataFrameLeft, textvariable=self.medName, font=("times new roman", 13, "bold"),
                               state="readonly")
        combol6["values"] = row1
        combol6.current(0)
        combol6.place(x=210, y=150, height=35, width=115)






        l7 = Label(DataFrameLeft, text="Lot No", font=("times new roman", 17, "bold"), padx=2)
        l7.place(x=13, y=195, height=35, width=110)

        l7t2 = Entry(DataFrameLeft, textvariable=self.lotNo, bd=3, relief=RIDGE, font=("times new roman", 13, "bold"))
        l7t2.place(x=210, y=195, height=35, width=115)






        l8 = Label(DataFrameLeft, text="Issue Date", font=("times new roman", 17, "bold"), padx=2)
        l8.place(x=30, y=240, height=35, width=110)

        l8t3 = Entry(DataFrameLeft, textvariable=self.issueDate, bd=3, relief=RIDGE,
                     font=("times new roman", 13, "bold"))
        l8t3.place(x=210, y=240, height=35, width=115)






        l9 = Label(DataFrameLeft, text="Exp Date", font=("times new roman", 17, "bold"), padx=2)
        l9.place(x=339, y=15, height=35, width=140)

        l9t4 = Entry(DataFrameLeft, textvariable=self.expDate, bd=3, relief=RIDGE, font=("times new roman", 13, "bold"))
        l9t4.place(x=520, y=15, height=35, width=115)






        l10 = Label(DataFrameLeft, text="Uses", font=("times new roman", 17, "bold"), padx=2)
        l10.place(x=325, y=60, height=35, width=120)

        l10t5 = Entry(DataFrameLeft, textvariable=self.uses, bd=3, relief=RIDGE, font=("times new roman", 13, "bold"))
        l10t5.place(x=520, y=60, height=35, width=115)






        l11 = Label(DataFrameLeft, text="Side Effect", font=("times new roman", 17, "bold"), padx=2)
        l11.place(x=358, y=105, height=35, width=120)

        l11t6 = Entry(DataFrameLeft, textvariable=self.sideEff, bd=3, relief=RIDGE,
                      font=("times new roman", 13, "bold"))
        l11t6.place(x=520, y=105, height=35, width=115)






        l12 = Label(DataFrameLeft, text="Prec-Warning", font=("times new roman", 17, "bold"), padx=2)
        l12.place(x=358, y=150, height=35, width=150)

        l12t7 = Entry(DataFrameLeft, textvariable=self.precWar, bd=3, relief=RIDGE,
                      font=("times new roman", 13, "bold"))
        l12t7.place(x=520, y=150, height=35, width=115)






        l13 = Label(DataFrameLeft, text="Dosage", font=("times new roman", 17, "bold"), padx=2)
        l13.place(x=325, y=195, height=35, width=150)

        l13t8 = Entry(DataFrameLeft, textvariable=self.dosage, bd=3, relief=RIDGE, font=("times new roman", 13, "bold"))
        l13t8.place(x=520, y=195, height=35, width=115)






        l14 = Label(DataFrameLeft, text="Tablet Price", font=("times new roman", 17, "bold"), padx=2)
        l14.place(x=350, y=240, height=35, width=150)

        l14t9 = Entry(DataFrameLeft, textvariable=self.tabPrice, bd=3, relief=RIDGE,
                      font=("times new roman", 13, "bold"))
        l14t9.place(x=520, y=240, height=35, width=115)







        # ============ data frame right ================

        i3 = Image.open("image/d.jpg")
        i3 = i3.resize((150, 84), Image.ANTIALIAS)
        self.photo3 = ImageTk.PhotoImage(i3)
        b3 = Button(self.root, image=self.photo3, borderwidth=0)
        b3.place(x=1060, y=185)






        l15 = Label(DataFrameRight, text="Reference No", font=("times new roman", 17, "bold"))
        l15.place(x=15, y=15, height=35, width=140)

        l15t10 = Entry(DataFrameRight, textvariable=self.Ref, font=("times new roman", 13, "bold"), bd=3, relief=RIDGE)
        l15t10.place(x=170, y=15, height=35, width=115)






        l16 = Label(DataFrameRight, text="Medicine Name", font=("times new roman", 16, "bold"))
        l16.place(x=15, y=60, height=35, width=140)

        l16t11 = Entry(DataFrameRight, textvariable=self.MedName, font=("times new roman", 13, "bold"), bd=3,
                       relief=RIDGE)
        l16t11.place(x=170, y=60, height=35, width=115)







        # ============ side frame ================

        side_frame = Frame(DataFrameRight, bd=4, relief=RIDGE, bg="white")
        side_frame.place(x=15, y=105, height=185, width=270)






        sc_x = ttk.Scrollbar(side_frame, orient=HORIZONTAL)
        sc_x.pack(side=BOTTOM, fill=X)

        sc_y = ttk.Scrollbar(side_frame, orient=VERTICAL)
        sc_y.pack(side=RIGHT, fill=Y)

        self.medicine_table = ttk.Treeview(side_frame, column=("ref", "medName"), xscrollcommand=sc_x.set,
                                           yscrollcommand=sc_y.set)

        sc_x.config(command=self.medicine_table.xview)
        sc_y.config(command=self.medicine_table.yview)






        self.medicine_table.heading("ref", text="Ref")
        self.medicine_table.heading("medName", text="Medicine Name")

        self.medicine_table["show"] = "headings"
        self.medicine_table.pack(fill="both", expand=1)

        self.medicine_table.column("ref", width=100)
        self.medicine_table.column("medName", width=100)







        self.medicine_table.bind("<ButtonRelease-1>", self.ShowData)






        # =============== Medicine Add Button =================

        downFrame = Frame(DataFrameRight, bd=4, relief=RIDGE, bg="darkGreen")
        downFrame.place(x=300, y=105, width=151, height=185)






        btnAddMed = Button(downFrame, command=self.AddMedicine, text="Add", font=("times new roman", 13, "bold"))
        btnAddMed.place(x=10, y=10, height=35, width=125)

        btnUpdateMed = Button(downFrame, command=self.UpdateMedicine, text="Update", font=("times new roman", 13, "bold"))
        btnUpdateMed.place(x=10, y=50, height=35, width=125)

        btnDelMed = Button(downFrame, command=self.DeleteMedicine, text="Delete", font=("times new roman", 13, "bold"))
        btnDelMed.place(x=10, y=92, height=35, width=125)

        btnClearMed = Button(downFrame, command=self.ClearText, text="Clear", font=("times new roman", 13, "bold"))
        btnClearMed.place(x=10, y=132, height=35, width=125)






        # ============ Frame Details ==================

        FrameDetails = Frame(self.root, bd=15, relief=RIDGE, bg="darkGreen")
        FrameDetails.place(x=0, y=615, width=1279, height=335)






        # ============= Main Table and ScrollBar ==================

        Table_frame = Frame(self.root, bd=15, relief=RIDGE)
        Table_frame.place(x=20, y=635, height=295, width=1238.5)






        scroll_x = ttk.Scrollbar(Table_frame, orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM, fill=X)

        scroll_y = ttk.Scrollbar(Table_frame, orient=VERTICAL)
        scroll_y.pack(side=RIGHT, fill=Y)

        self.pharmacyTable = ttk.Treeview(Table_frame, column=("ref", "companyName",
                                                               "type", "tabletName", "lotNo", "issueDate", "expDate",
                                                               "uses", "sideEffect",
                                                               "warning", "dosage", "price"),
                                          xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.config(command=self.pharmacyTable.xview)
        scroll_y.config(command=self.pharmacyTable.yview)






        self.pharmacyTable.heading("ref", text="Reference No")
        self.pharmacyTable.heading("companyName", text="Company Name")
        self.pharmacyTable.heading("type", text="Medicine Type")
        self.pharmacyTable.heading("tabletName", text="Tablet Name")
        self.pharmacyTable.heading("lotNo", text="Lot No")
        self.pharmacyTable.heading("issueDate", text="Issue Date")
        self.pharmacyTable.heading("expDate", text="Exp Date")
        self.pharmacyTable.heading("uses", text="Uses")
        self.pharmacyTable.heading("sideEffect", text="Side Effect")
        self.pharmacyTable.heading("warning", text="Warning")
        self.pharmacyTable.heading("dosage", text="Dosage")
        self.pharmacyTable.heading("price", text="Price")

        self.pharmacyTable["show"] = "headings"
        self.pharmacyTable.pack(fill="both", expand=1)






        self.pharmacyTable.column("ref", width=100)
        self.pharmacyTable.column("companyName", width=100)
        self.pharmacyTable.column("type", width=100)
        self.pharmacyTable.column("tabletName", width=100)
        self.pharmacyTable.column("lotNo", width=100)
        self.pharmacyTable.column("issueDate", width=100)
        self.pharmacyTable.column("expDate", width=100)
        self.pharmacyTable.column("uses", width=100)
        self.pharmacyTable.column("sideEffect", width=100)
        self.pharmacyTable.column("warning", width=100)
        self.pharmacyTable.column("dosage", width=100)
        self.pharmacyTable.column("price", width=100)







        self.FetchDataMedicine()
        self.FetchDataBottom()
        self.pharmacyTable.bind("<ButtonRelease-1>", self.ShowDataMedicine)






        # ============= Add Medicine Functionality Declaration ==============

    def AddMedicine(self):

        conn = mysql.connector.connect(host="localhost", username="root", password="root",
                                       database="pharma")
        my_cursor = conn.cursor()
        my_cursor.execute("insert into medAddDept(ref, medName) values(%s, %s)",
                          (self.Ref.get(), self.MedName.get()))
        conn.commit()

        self.FetchDataMedicine()
        messagebox.showinfo("Message", "Medicine added Successfully !")
        self.ShowData()

        conn.close()





    def FetchDataMedicine(self):

        conn = mysql.connector.connect(host="localhost", username="root", password="root",
                                       database="pharma")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from medAddDept")
        rows = my_cursor.fetchall()

        if len(rows) != 0:
            self.medicine_table.delete(*self.medicine_table.get_children())

            for i in rows:
                self.medicine_table.insert("", END, values=i)
            conn.commit()

        conn.close()






    # ================= med update show data ===================

    def ShowData(self, event=""):

        cursor_row = self.medicine_table.focus()
        content = self.medicine_table.item(cursor_row)
        row = content["values"]
        self.Ref.set(row[0])
        self.MedName.set(row[1])






    def UpdateMedicine(self):

        if self.Ref.get() == "" or self.MedName.get() == "":
            messagebox.showerror("Message", "All Fields Are Required !")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="root",
                                           database="pharma")
            my_cursor = conn.cursor()
            my_cursor.execute("update medAddDept set medName=%s where ref=%s", (self.MedName.get(),
                                                                                self.Ref.get()))
            conn.commit()

            self.FetchDataMedicine()
            messagebox.showinfo("Success", "Medicine Updated Successfully !")

            conn.close()






    def DeleteMedicine(self):

        conn = mysql.connector.connect(host="localhost", username="root", password="root",
                                       database="pharma")
        my_cursor = conn.cursor()

        # sql = "delete from medAddDept where ref=%s"
        # val = (self.Ref.get(),)
        # my_cursor.execute(sql, val)

        my_cursor.execute("delete from medAddDept where ref=%s", (self.Ref.get(),))

        conn.commit()

        self.FetchDataMedicine()
        messagebox.showinfo("Success", "Medicine Deleted Successfully !")

        conn.close()






    def ClearText(self):

        self.Ref.set("")
        self.MedName.set("")






    # ================== Main Table =====================

    def AddMedicineData(self):

        if self.ref.get() == "" or self.lotNo.get() == "":
            messagebox.showerror("Message", "All Fields Are Required !")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="root",
                                           database="pharma")
            my_cursor = conn.cursor()

            sql = "insert into medInfo values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            val = (self.ref.get(), self.comName.get(), self.medType.get(), self.medName.get(),
                   self.lotNo.get(), self.issueDate.get(), self.expDate.get(), self.uses.get(),
                   self.sideEff.get(), self.precWar.get(), self.dosage.get(), self.tabPrice.get(),)

            my_cursor.execute(sql, val)
            conn.commit()

            messagebox.showinfo("Message", "Data Inserted Successfully !")
            self.FetchDataBottom()

            conn.close()







    def FetchDataBottom(self):

        conn = mysql.connector.connect(host="localhost", username="root", password="root",
                                       database="pharma")
        my_cursor = conn.cursor()

        my_cursor.execute("select * from medInfo")
        row = my_cursor.fetchall()

        if len(row) != 0:
            self.pharmacyTable.delete(*self.pharmacyTable.get_children())

            for i in row:
                self.pharmacyTable.insert("", END, values=i)
            conn.commit()

        conn.close()






    def ShowDataMedicine(self, event=""):

        cursor_row = self.pharmacyTable.focus()
        content = self.pharmacyTable.item(cursor_row)
        row = content["values"]

        self.ref.set(row[0])
        self.comName.set(row[1])
        self.medType.set(row[2])
        self.medName.set(row[3])
        self.lotNo.set(row[4])
        self.issueDate.set(row[5])
        self.expDate.set(row[6])
        self.uses.set(row[7])
        self.sideEff.set(row[8])
        self.precWar.set(row[9])
        self.dosage.set(row[10])
        self.tabPrice.set(row[11])






    def Update(self):

        if self.ref.get() == "":
            messagebox.showinfo("Message", "All Fields Are Required !")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="root",
                                           database="pharma")
            my_cursor = conn.cursor()

            my_cursor.execute("update medInfo set comName=%s, medType=%s, medName=%s, lotNo=%s,"
                              " issueDate=%s, expDate=%s, uses=%s, sideEff=%s, precWar=%s,"
                              " dosage=%s, tabPrice=%s where ref=%s",
                              (self.comName.get(), self.medType.get(), self.medName.get(),
                               self.lotNo.get(), self.issueDate.get(), self.expDate.get(),
                               self.uses.get(), self.sideEff.get(), self.precWar.get(),
                               self.dosage.get(), self.tabPrice.get(), self.ref.get()))

            conn.commit()

            self.FetchDataBottom()
            conn.close()

            messagebox.showinfo("Message", "Record has been Updated Successfully")






    def Delete(self):

        conn = mysql.connector.connect(host="localhost", username="root", password="root",
                                       database="pharma")
        my_cursor = conn.cursor()

        sql = "delete from medInfo where ref=%s"
        val = (self.ref.get(),)

        my_cursor.execute(sql, val)
        conn.commit()

        self.FetchDataBottom()
        conn.close()

        messagebox.showinfo("Message", "Record Deleted Successfully")





    def Reset(self):

        self.comName.set("")
        self.lotNo.set("")
        self.issueDate.set("")
        self.expDate.set("")
        self.uses.set("")
        self.precWar.set("")
        self.sideEff.set("")
        self.dosage.set("")
        self.tabPrice.set("")






    def SearchData(self):

        conn = mysql.connector.connect(host="localhost", username="root", password="root",
                                       database="pharma")
        my_cursor = conn.cursor()

        my_cursor.execute("select * from medInfo where "+str(self.combo_var.get()) +
                          " LIKE " + str(self.entry_var.get()))

        rows = my_cursor.fetchall()

        if len(rows) != 0:
            self.pharmacyTable.delete(*self.pharmacyTable.get_children())

            for i in rows:
                self.pharmacyTable.insert("", END, values=i)
            conn.commit()

        conn.close()






    def Exit(self):

        self.root.destroy()







if __name__ == "__main__":

    root = Tk()
    obj = PharmacyManagementSystem(root)
    root.mainloop()
