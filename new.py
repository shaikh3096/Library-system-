import tkinter
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import datetime

def main():
      win=Tk()
      app=Login_Window(win)
      win.mainloop()

class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")
         # =================================varibles======================
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_security_q=StringVar()
        self.var_security_a=StringVar()
        self.var_pswd=StringVar()
        self.var_confirm_pswd=StringVar()

        
        
        self.bg=ImageTk.PhotoImage(file="Images/Login_bg.jpg")
    
        lblimg1=Label(self.root,image=self.bg)
        lblimg1.place(x=0,y=0,relwidth=1,relheight=1)
        
        
        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)
        
        img1 = Image.open("Images/Logo.jpg")
        img1= img1.resize((100,100),Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        
        
        lblimg1=Label(image=self.photoimg1,bg="black",borderwidth=0)
        lblimg1.place(x=730,y=180,width=100,height=100)
        
        get_str=Label(frame,text="Get Started",font=("comic sans ms",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=100)
        
        #label
        username=lbl=Label(frame,text="Username",font=("comic sans ms",15,"bold"),fg="white",bg="black")
        username.place(x=70,y=145)
        
        self.txtuser=ttk.Entry(frame,textvariable=self.var_email,font=("comic sans ms",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)
        
        Password=lbl=Label(frame,text="Password",font=("comic sans ms",15,"bold"),fg="white",bg="black")
        Password.place(x=70,y=215)
        
        self.txtpass=ttk.Entry(frame,textvariable=self.var_pswd,font=("comic sans ms",15,"bold"))
        self.txtpass.place(x=40,y=250,width=270)
        
        #login button
        btn_login=Button(frame,command=self.login,text="Login",font=("comic sans ms",15,"bold"),bd=3,relief=RIDGE,fg="black",bg="white")
        btn_login.place(x=110,y=300,width=120,height=35)
      
      #register button
        registerbtn=Button(frame,text="New User Register",command=self.register_window,font=("comic sans ms",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=90,y=350,width=160)
        
      #forget pass   
        forgotpassbtn=Button(frame,text="Forgot Password",command=self.forgot_password_window,font=("comic sans ms",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")            
        forgotpassbtn.place(x= 90,y=380,width=160)
        
    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window) 
        
        
    def login(self):
        if self.txtuser.get()==" "or self.txtpass.get()==" ":
            messagebox.showerror("Error","all fields required")
        elif self.txtuser.get()=="123" and self.txtpass.get()=="123":
            messagebox.showinfo("Success","welcome to Book Nook!!")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Root123$",database="db")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and pswd=%s",(
                                                                                        self.var_email.get(),
                                                                                        self.var_pswd.get()
                                                                                ))
                
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username & Password")
            else:
                open_main=messagebox.askyesno("YesNo","Access only admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=LibraryManagementSystem(self.new_window)
                    
                else:
                    if not open_main:
                        return
                    conn.commit()
                    conn.close()
                    
                
                    
        
    # ===================reset password==============================================
    def reset_pass(self):
        if self.combo_security_q.get()=="Select":
            messagebox.showerror("Error","Select the security question",parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","Please enter the answer",parent=self.root2)
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error","Please enter the new password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Root123$",database="db")
            my_cursor=conn.cursor()
            qury=("select * from register where email=%s and security_q=%s and security_a=%s")
            vlaue=(self.txtuser.get(),self.combo_security_q.get(),self.txt_security.get())
            my_cursor.execute(qury,vlaue)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter correct answer",parent=self.root2)
            else:
                query=("update register set pswd=%s where email=%s")
                value=(self.txt_newpass.get(),self.txtuser.get())
                my_cursor.execute(query,value)
                
                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your password has been reset,please login new password",parent=self.root2)
                self.root2.destroy()
            
                        
                
     # ==================================forgot password window====================================
    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please Enter the email address to reset password")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Root123$",database="db")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            print(row)
               
            if row==None:
                messagebox.showerror("My Error","Please enter the valid user name")  
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+610+170")
                
                l=Label(self.root2,text="Forget Password",font=("comic sans ms",15,"bold"),fg="white",bg="black")
                l.place(x=0,y=10,relwidth=1)
                
                security_q=Label(self.root2,text="Select Security Questions",font=("comic sans ms",15,"bold"),bg="tan",fg="black")
                security_q.place(x=50,y=80)
                
                self.combo_security_q=ttk.Combobox(self.root2,font=("comic sans ms",15,"bold"),state="readonly")
                self.combo_security_q["values"]=("Select","Your Birth Place","Your School name","Your BestFriend name")
                self.combo_security_q.place(x=50,y=110,width=250)
                self.combo_security_q.current(0)


                security_a=Label(self.root2,text="Security Answer",font=("comic sans ms",15,"bold"),bg="tan",fg="black")
                security_a.place(x=50,y=150)

                self.txt_security=ttk.Entry(self.root2,font=("comic sans ms",15))
                self.txt_security.place(x=50,y=180,width=250)
                             
                new_pass=Label(self.root2,text="New Password",font=("comic sans ms",15,"bold"),bg="tan",fg="black")
                new_pass.place(x=50,y=220)


                self.txt_newpass=ttk.Entry(self.root2,font=("comic sans ms",15))
                self.txt_newpass.place(x=50,y=250,width=250)
                        
                btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("comic sans ms",15,"bold"),fg="white",bg="green")
                btn.place(x=100,y=290)
                        
                btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("comic sans ms",15,"bold"),fg="white",bg="green")
                btn.place(x=100,y=290)   
           #=======================================REGISTER====================================================================      
                
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x800+0+0")

       # =================================varibles======================
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_security_q=StringVar()
        self.var_security_a=StringVar()
        self.var_pswd=StringVar()
        self.var_confirm_pswd=StringVar()


         # ===============bg image================
        self.bg=ImageTk.PhotoImage(file="Images/Register_bg.jpg")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

       
         # ===============left image================
        leftframe=Frame(self.root,bg="white")
        leftframe.place(x=50,y=100,width=470,height=550)
        
        bg1=Image.open("Images/Register_book.jpg")
        bg1=bg1.resize((470,550),Image.Resampling.LANCZOS)
        self.photoimage2=ImageTk.PhotoImage(bg1)
        
        left_lbl=Label(leftframe,image=self.photoimage2,bd=0,relief=RIDGE)
        left_lbl.place(x=0,y=0,width=470,height=550)

         # =============main frame============
        frame=Frame(self.root,bg="tan")
        frame.place(x=520,y=100,width=800,height=550)

        Register_lbl=Label(frame,text="REGISTER HERE",font=("comic sans ms",20,"bold"),fg="black",bg="tan")
        Register_lbl.place(x=20,y=20)

         #===================label and entry====================

         # -------------------row1 
        fname=Label(frame,text="First Name",font=("comic sans ms",15,"bold"),fg="black",bg="tan")
        fname.place(x=50,y=100)
       
        self.fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("comic sans ms",15,"bold"))
        self.fname_entry.place(x=50,y=130,width=250)

        l_name=Label(frame,text="Last Name",font=("comic sans ms",15,"bold"),bg="tan",fg="black")
        l_name.place(x=370,y=100)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("comic sans ms",15))
        self.txt_lname.place(x=370,y=130,width=250)

    #=====================Labels========================

        contact=Label(frame,text="Contact No",font=("comic sans ms",15,"bold"),bg="tan",fg="black")
        contact.place(x=50,y=170)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("comic sans ms",15))
        self.txt_contact.place(x=50,y=200,width=250)

        email=Label(frame,text="Email",font=("comic sans ms",15,"bold"),bg="tan",fg="black")
        email.place(x=370,y=170)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("comic sans ms",15))
        self.txt_email.place(x=370,y=200,width=250)

     
         #===================Security Q and A==========================

        security_q=Label(frame,text="Select Security Questions",font=("comic sans ms",15,"bold"),bg="tan",fg="black") 
        security_q.place(x=50,y=240)

        self.combo_security_q=ttk.Combobox(frame,textvariable=self.var_security_q,font=("comic sans ms",15,"bold"),state="readonly")
        self.combo_security_q["values"]=("Select","Your Birth Place","Your School name","Your BestFriend name")
        self.combo_security_q.place(x=50,y=270,width=250)
        self.combo_security_q.current(0)



        security_a=Label(frame,text="Security Answer",font=("comic sans ms",15,"bold"),bg="tan",fg="black")
        security_a.place(x=370,y=240)

        self.txt_security=ttk.Entry(frame,textvariable=self.var_security_a,font=("comic sans ms",15))
        self.txt_security.place(x=370,y=270,width=250)

         # --------------------Password
        
        pswd=Label(frame,text="Password",font=("comic sans ms",15,"bold"),bg="tan",fg="black")
        pswd.place(x=50,y=310)

        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pswd,font=("comic sans ms",15))
        self.txt_pswd.place(x=50,y=340,width=250)

        confirm_pswd=Label(frame,text="Confirm Password",font=("comic sans ms",15,"bold"),bg="tan",fg="black")
        confirm_pswd.place(x=370,y=310)

        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confirm_pswd,font=("comic sans ms",15))
        self.txt_confirm_pswd.place(x=370,y=340,width=250)

         # =====================checkbutton=================
        self.var_check=IntVar()
        self.checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree the Terms and Conditions",font=("comic sans ms",12,"bold"),onvalue=1,offvalue=0)
        self.checkbtn.place(x=50,y=380)

         # ==================buttons===================
        registerbtn=Button(frame,command=self.register_data,text="Register",font=("comic sans ms",15,"bold"),bd=3,relief=RIDGE,fg="tan",bg="black")
        registerbtn.place(x=100,y=450,width=120,height=35)

        lginbtn=Button(frame,text="Login-in now",command=self.return_login,font=("comic sans ms",15,"bold"),bd=3,relief=RIDGE,fg="tan",bg="black")
        lginbtn.place(x=370,y=450,width=140,height=35)


   # ======================Function declarition=========================    
    
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_security_q.get()=="Select":
            messagebox.showerror("Error","All fields are required")
        elif self.var_pswd.get()!=self.var_confirm_pswd.get():
            messagebox.showerror("Error","password and confirm password must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree our term and conditions")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Root123$",database="db")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exist. Please try another email")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",( 
                                                                                         self.var_fname.get(),
                                                                                         self.var_lname.get(),
                                                                                         self.var_contact.get(),
                                                                                         self.var_email.get(),
                                                                                         self.var_security_q.get(),
                                                                                         self.var_security_a.get(),
                                                                                         self.var_pswd.get()
                                                                                         
                                                                                       ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Sucess","Registered Sucessfully") 
               
    def return_login(self):
        self.root.destroy()      







class LibraryManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Library Management System")
        self.root.geometry("1550x800+0+0")

#==============================Variables================================================================

        self.member_var=StringVar()
        self.prnno_var=StringVar()
        self.title_var=StringVar()
        self.firstname_var=StringVar()
        self.lastname_var=StringVar()
        self.address1_var=StringVar()
        self.address2_var=StringVar()
        self.postid_var=StringVar()
        self.mobile_var=StringVar()
        self.bookid_var=StringVar()
        self.booktitle_var=StringVar()
        self.author_var=StringVar()
        self.dateborrowed_var=StringVar()
        self.datedue_var=StringVar()
        self.days_var=StringVar()
        self.latereturnfine_var=StringVar()
        self.dateoverdue_var=StringVar()
        self.price_var=StringVar()



 
        lbltitle=Label(self.root,text="The Book Nook",bg="tan",fg="black",bd=20,relief=RIDGE,font=("times new roman",50,"bold"),padx=2,pady=6)
        lbltitle.pack(side=TOP,fill=X)

        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="black")
        frame.place(x=0,y=130,width=1530,height=400)

#=============================Data Frame Left====================================================================
 
        DataFrameLeft=LabelFrame(frame,text="Library Membership Information",bg="blanchedalmond",fg="brown",bd=10,relief=RIDGE,font=("times new roman",15,"bold"))
        DataFrameLeft.place(x=0,y=5,width=900,height=360)

        lblMember=Label(DataFrameLeft,bg="blanchedalmond",fg="brown",text="Member",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblMember.grid(row=0,column=0,sticky=W)

        comMember=ttk.Combobox(DataFrameLeft,font=("times new roman",12,"bold"),textvariable=self.member_var,width=27,state="readonly")
        comMember["value"]=("Admin Staff","Student","Lecturer")
        comMember.grid(row=0,column=1)

        lblPRN_No=Label(DataFrameLeft,bg="blanchedalmond",fg="brown",text="PRN Number",font=("arial",12,"bold"),padx=2)
        lblPRN_No.grid(row=1,column=0,sticky=W)
        txtPRN_No=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.prnno_var,width=29)
        txtPRN_No.grid(row=1,column=1)

        lblTitle=Label(DataFrameLeft,bg="blanchedalmond",fg="brown",text="ID No.",font=("arial",12,"bold"),padx=2,pady=4)
        lblTitle.grid(row=2,column=0,sticky=W)
        txtTitle=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.title_var,width=29)
        txtTitle.grid(row=2,column=1)

        lblFirstName=Label(DataFrameLeft,bg="blanchedalmond",fg="brown",text="First Name",font=("arial",12,"bold"),padx=2,pady=6)
        lblFirstName.grid(row=3,column=0,sticky=W)
        txtFirstName=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.firstname_var,width=29)
        txtFirstName.grid(row=3,column=1)

        lblLastName=Label(DataFrameLeft,bg="blanchedalmond",fg="brown",text="Last Name",font=("arial",12,"bold"),padx=2,pady=6)
        lblLastName.grid(row=4,column=0,sticky=W)
        txtLastName=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.lastname_var,width=29)
        txtLastName.grid(row=4,column=1)

        lblAddress1=Label(DataFrameLeft,bg="blanchedalmond",fg="brown",text="Address 1",font=("arial",12,"bold"),padx=2,pady=6)
        lblAddress1.grid(row=5,column=0,sticky=W)
        txtAddress1=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.address1_var,width=29)
        txtAddress1.grid(row=5,column=1)

        lblAddress2=Label(DataFrameLeft,bg="blanchedalmond",fg="brown",text="Address 2",font=("arial",12,"bold"),padx=2,pady=6)
        lblAddress2.grid(row=6,column=0,sticky=W)
        txtAddress2=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.address2_var,width=29)
        txtAddress2.grid(row=6,column=1)

        lblPostCode=Label(DataFrameLeft,bg="blanchedalmond",fg="brown",text="Postal Code",font=("arial",12,"bold"),padx=2,pady=4)
        lblPostCode.grid(row=7,column=0,sticky=W)
        txtPostCode=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.postid_var,width=29)
        txtPostCode.grid(row=7,column=1)

        lblMobile=Label(DataFrameLeft,bg="blanchedalmond",fg="brown",text="Mobile No.",font=("arial",12,"bold"),padx=2,pady=6)
        lblMobile.grid(row=8,column=0,sticky=W)
        txtMobile=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.mobile_var,width=29)
        txtMobile.grid(row=8,column=1)

        lblBookID=Label(DataFrameLeft,bg="blanchedalmond",fg="brown",text="Book ID",font=("arial",12,"bold"),padx=2)
        lblBookID.grid(row=0,column=2,sticky=W)
        txtBookID=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.bookid_var,width=29)
        txtBookID.grid(row=0,column=3)

        lblBookTitle=Label(DataFrameLeft,bg="blanchedalmond",fg="brown",text="Book Title",font=("arial",12,"bold"),padx=2,pady=6)
        lblBookTitle.grid(row=1,column=2,sticky=W)
        txtBookTitle=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.booktitle_var,width=29)
        txtBookTitle.grid(row=1,column=3)

        lblAuthor=Label(DataFrameLeft,bg="blanchedalmond",fg="brown",text="Author",font=("arial",12,"bold"),padx=2,pady=6)
        lblAuthor.grid(row=2,column=2,sticky=W)
        txtAuthor=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.author_var,width=29)
        txtAuthor.grid(row=2,column=3)

        lblDateBorrowed=Label(DataFrameLeft,bg="blanchedalmond",fg="brown",text="Date Borrowed",font=("arial",12,"bold"),padx=2,pady=6)
        lblDateBorrowed.grid(row=3,column=2,sticky=W)
        txtDateBorrowed=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.dateborrowed_var,width=29)
        txtDateBorrowed.grid(row=3,column=3,sticky=W)

        lblDateDue=Label(DataFrameLeft,bg="blanchedalmond",fg="brown",text="Date Due",font=("arial",12,"bold"),padx=2,pady=6)
        lblDateDue.grid(row=4,column=2,sticky=W)
        txtDateDue=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.datedue_var,width=29)
        txtDateDue.grid(row=4,column=3)

        lblDaysOnBook=Label(DataFrameLeft,bg="blanchedalmond",fg="brown",text="Days On Book",font=("arial",12,"bold"),padx=2,pady=6)
        lblDaysOnBook.grid(row=5,column=2,sticky=W)
        txtDaysOnBook=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.days_var,width=29)
        txtDaysOnBook.grid(row=5,column=3)

        lblLateReturnFine=Label(DataFrameLeft,bg="blanchedalmond",fg="brown",text="Late Return Fine",font=("arial",12,"bold"),padx=2,pady=6)
        lblLateReturnFine.grid(row=6,column=2,sticky=W)
        txtLateReturnFine=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.latereturnfine_var,width=29)
        txtLateReturnFine.grid(row=6,column=3)

        lblDateOverDue=Label(DataFrameLeft,bg="blanchedalmond",fg="brown",text="Date Over Due",font=("arial",12,"bold"),padx=2,pady=6)
        lblDateOverDue.grid(row=7,column=2,sticky=W)
        txtDateOverDue=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.dateoverdue_var,width=29)
        txtDateOverDue.grid(row=7,column=3)

        lblPrice=Label(DataFrameLeft,bg="blanchedalmond",fg="brown",text="Price",font=("arial",12,"bold"),padx=2,pady=6)
        lblPrice.grid(row=8,column=2,sticky=W)
        txtPrice=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.price_var,width=29)
        txtPrice.grid(row=8,column=3)

#=========================================Data Frame Right====================================================================

        DataFrameRight=LabelFrame(frame,text="Book Deatails",bg="blanchedalmond",fg="brown",bd=10,relief=RIDGE,font=("times new roman",15,"bold"))
        DataFrameRight.place(x=910,y=5,width=540,height=350)

        self.txtBox=Text(DataFrameRight,font=("arial",12,"bold"),bg="blanchedalmond",fg="brown",width=32,height=16,padx=2,pady=6)
        self.txtBox.grid(row=0,column=2)

        listScrollbar=Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0,column=1,sticky="ns")

        listBooks=['Head First Book','Learn Python the Hard Way','Python Programming','Secrete Rahshy','Python Cookbook',
                   'Intro to Machine Learning','Machine Techno','My Python','Elite Jungle Python',
                   'Machine Python','Advance Python','Inton Python','ReadChilli Python','Python Crash Course']


#==========================================BOOK DATA======================================================== 
        
        def SelectBook(event=""):
            value=str(listBox.get(listBox.curselection()))
            x=value
            if(x=="Head First Book"):
                self.bookid_var.set("1001")
                self.booktitle_var.set("Python Manual")
                self.author_var.set("Paul Berry")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.days_var.set(15)
                self.latereturnfine_var.set("Rs.15")
                self.datedue_var.set("NO")
                self.price_var.set("Rs.300")

            elif(x=="Learn Python the Hard Way"):
                self.bookid_var.set("1002")
                self.booktitle_var.set("Basic of Python")
                self.author_var.set("Zed A. Shan")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.days_var.set(15)
                self.latereturnfine_var.set("Rs.15")
                self.datedue_var.set("NO")
                self.price_var.set("Rs.300")

            elif(x=="Python Programming"):
                self.bookid_var.set("1002")
                self.booktitle_var.set("Introduction to Python")
                self.author_var.set("John Zhele")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.days_var.set(15)
                self.latereturnfine_var.set("Rs.15")
                self.datedue_var.set("NO")
                self.price_var.set("Rs.300")

            elif(x=="Secrete Rahshy"):
                self.bookid_var.set("1003")
                self.booktitle_var.set("Basic Python")
                self.author_var.set("Ref.Kapil Kamble")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.days_var.set(15)
                self.latereturnfine_var.set("Rs.15")
                self.datedue_var.set("NO")
                self.price_var.set("Rs.300")

            elif(x=="Python Cookbook"):
                self.bookid_var.set("1004")
                self.booktitle_var.set("Python Cookbook")
                self.author_var.set("Brian Jones")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.days_var.set(15)
                self.latereturnfine_var.set("Rs.15")
                self.datedue_var.set("NO")
                self.price_var.set("Rs.300")

            elif(x=="Intro to Machine Learning"):
                self.bookid_var.set("1005")
                self.booktitle_var.set("Intro to Machine Learning")
                self.author_var.set("Sarah Guiado")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.days_var.set(15)
                self.latereturnfine_var.set("Rs.15")
                self.datedue_var.set("NO")
                self.price_var.set("Rs.300")

            elif(x=="Machine Techno"):
                self.bookid_var.set("1006")
                self.booktitle_var.set("Machine Techno")
                self.author_var.set("John Zhele")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.days_var.set(15)
                self.latereturnfine_var.set("Rs.15")
                self.datedue_var.set("NO")
                self.price_var.set("Rs.300")

            elif(x=="My Python"):
                self.bookid_var.set("1007")
                self.booktitle_var.set("My Python")
                self.author_var.set("Paul Berry")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.days_var.set(15)
                self.latereturnfine_var.set("Rs.15")
                self.datedue_var.set("NO")
                self.price_var.set("Rs.300")


            elif(x=="Elite Jungle Python"):
                self.bookid_var.set("1008")
                self.booktitle_var.set("Elite Jungle Python")
                self.author_var.set("Zed A. Shan")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.days_var.set(15)
                self.latereturnfine_var.set("Rs.15")
                self.datedue_var.set("NO")
                self.price_var.set("Rs.300")

            elif(x=="Machine Python"):
                self.bookid_var.set("1009")
                self.booktitle_var.set("Machine Python")
                self.author_var.set("Brian Jones")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.days_var.set(15)
                self.latereturnfine_var.set("Rs.15")
                self.datedue_var.set("NO")
                self.price_var.set("Rs.300")

            elif(x=="Advance Python"):
                self.bookid_var.set("1010")
                self.booktitle_var.set("Advance Python")
                self.author_var.set("Brian Jones")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.days_var.set(15)
                self.latereturnfine_var.set("Rs.15")
                self.datedue_var.set("NO")
                self.price_var.set("Rs.300")

            elif(x=="Inton Python"):
                self.bookid_var.set("1011")
                self.booktitle_var.set("Inton Python")
                self.author_var.set("John Zhele")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.days_var.set(15)
                self.latereturnfine_var.set("Rs.15")
                self.datedue_var.set("NO")
                self.price_var.set("Rs.300")

            elif(x=="ReadChilli Python"):
                self.bookid_var.set("1012")
                self.booktitle_var.set("ReadChilli Python")
                self.author_var.set("John Zhele")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.days_var.set(15)
                self.latereturnfine_var.set("Rs.15")
                self.datedue_var.set("NO")
                self.price_var.set("Rs.300")

            elif(x=="Python Crash Course"):
                self.bookid_var.set("1002")
                self.booktitle_var.set("Python Crash Course")
                self.author_var.set("Ref.Kapil Kamble")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.days_var.set(15)
                self.latereturnfine_var.set("Rs.15")
                self.datedue_var.set("NO")
                self.price_var.set("Rs.300")

            

           
            


        listBox=Listbox(DataFrameRight,font=("arial",12,"bold"),width=20,height=16)
        listBox.bind("<<ListboxSelect>>",SelectBook)
        listBox.grid(row=0,column=0,padx=4)
        listScrollbar.config(command=listBox.yview)

        for item in listBooks:
            listBox.insert(END,item)


#==================================BUTTON FRAME=======================================================================================================
        Framebutton=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="black")
        Framebutton.place(x=0,y=530,width=1530,height=70)

        btnAddData=Button(Framebutton,command=self.add_data,text="Add Data",font=("arial",12,"bold"),width=23,bg="palegoldenrod",fg="brown")
        btnAddData.grid(row=0,column=0)

        btnShowData=Button(Framebutton,command=self.showData,text="Show Data",font=("arial",12,"bold"),width=23,bg="palegoldenrod",fg="brown")
        btnShowData.grid(row=0,column=1)

        btnUpdate=Button(Framebutton,command=self.update,text="Update",font=("arial",12,"bold"),width=23,bg="palegoldenrod",fg="brown")
        btnUpdate.grid(row=0,column=2)

        btnDelete=Button(Framebutton,command=self.delete,text="Delete",font=("arial",12,"bold"),width=23,bg="palegoldenrod",fg="brown")
        btnDelete.grid(row=0,column=3)

        btnReset=Button(Framebutton,command=self.reset,text="Reset",font=("arial",12,"bold"),width=23,bg="palegoldenrod",fg="brown")
        btnReset.grid(row=0,column=4)

        btnExit=Button(Framebutton,command=self.iExit,text="Exit",font=("arial",12,"bold"),width=23,bg="palegoldenrod",fg="brown")
        btnExit.grid(row=0,column=5)

#==================================INFORMATION FRAME=======================================================================================================
        FrameDetails=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="black")
        FrameDetails.place(x=0,y=590,width=1530,height=210)

        Table_frame=Frame(FrameDetails,bd=6,relief=RIDGE,bg="palegoldenrod")
        Table_frame.place(x=0,y=2,width=1460,height=190)

        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)

        self.library_table=ttk.Treeview(Table_frame,column=("membertype","prnno","title","firstname","lastname","address1",
                                                            "address2","postid","mobile","bookid","booktitle","author","dateborrowed",
                                                            "datedue","days","latereturnfine","dateoverdue","price"),
                                                            xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)
        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)


        
        self.library_table.heading("membertype",text="Member Type")
        self.library_table.heading("prnno",text="PRN No.")
        self.library_table.heading("title",text="Title")
        self.library_table.heading("firstname",text="First Name")
        self.library_table.heading("lastname",text="Last Name")
        self.library_table.heading("address1",text="Address 1")
        self.library_table.heading("address2",text="Address 2")
        self.library_table.heading("postid",text="Post ID")
        self.library_table.heading("mobile",text="Mobile")
        self.library_table.heading("bookid",text="Book ID")
        self.library_table.heading("booktitle",text="Book Title")
        self.library_table.heading("author",text="Author")
        self.library_table.heading("dateborrowed",text="Date Borrowed")
        self.library_table.heading("datedue",text="Date Due")
        self.library_table.heading("days",text="Days On Book")
        self.library_table.heading("latereturnfine",text="Late Return Fine")
        self.library_table.heading("dateoverdue",text="Date Overdue")
        self.library_table.heading("price",text="Price")

        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH,expand=1)
        
        self.library_table.column("membertype",width=100)
        self.library_table.column("prnno",width=100)
        self.library_table.column("title",width=100)
        self.library_table.column("firstname",width=100)
        self.library_table.column("lastname",width=100)
        self.library_table.column("address1",width=100)
        self.library_table.column("address2",width=100)
        self.library_table.column("postid",width=100)
        self.library_table.column("mobile",width=100)
        self.library_table.column("bookid",width=100)
        self.library_table.column("booktitle",width=100)
        self.library_table.column("author",width=100)
        self.library_table.column("dateborrowed",width=100)
        self.library_table.column("datedue",width=100)
        self.library_table.column("days",width=100)
        self.library_table.column("latereturnfine",width=100)
        self.library_table.column("dateoverdue",width=100)
        self.library_table.column("price",width=100)

        self.fetch_data()
        self.library_table.bind("<ButtonRelease-1>",self.get_cursor)


    def add_data(self):
        

        conn = mysql.connector.connect(host="localhost",user="root",password="Root123$",database="db")
        my_cursor = conn.cursor()
        my_cursor.execute("INSERT into new_library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                self.member_var.get(),
                                                                                                self.prnno_var.get(),
                                                                                                self.title_var.get(),
                                                                                                self.firstname_var.get(),
                                                                                                self.lastname_var.get(),
                                                                                                self.address1_var.get(),
                                                                                                self.address2_var.get(),
                                                                                                self.postid_var.get(),
                                                                                                self.mobile_var.get(),
                                                                                                self.bookid_var.get(),
                                                                                                self.booktitle_var.get(),
                                                                                                self.author_var.get(),
                                                                                                self.dateborrowed_var.get(),
                                                                                                self.datedue_var.get(),
                                                                                                self.days_var.get(),
                                                                                                self.latereturnfine_var.get(),
                                                                                                self.dateoverdue_var.get(),
                                                                                                self.price_var.get()
                                  
                                                                                                                   ))
        conn.commit()
        self.fetch_data()
        conn.close()

        messagebox.showinfo("SUCCESS","Data added succesfully")


    def update(self):


        conn = mysql.connector.connect(host="localhost",user="root",password="Root123$",database="db")
        my_cursor = conn.cursor()
        my_cursor.execute("update new_library set member=%s,title=%s,firstname=%s,lastname=%s,address1=%s,address2=%s,postid=%s,mobile=%s,bookid=%s,booktitle=%s,author=%s,dateborrowed=%s,datedue=%s,days=%s,latereturnfine=%s,dateoverdue=%s,price=%s where prnno=%s",(
                                                                                                self.member_var.get(),
                                                                                                self.title_var.get(),
                                                                                                self.firstname_var.get(),
                                                                                                self.lastname_var.get(),
                                                                                                self.address1_var.get(),
                                                                                                self.address2_var.get(),
                                                                                                self.postid_var.get(),
                                                                                                self.mobile_var.get(),
                                                                                                self.bookid_var.get(),
                                                                                                self.booktitle_var.get(),
                                                                                                self.author_var.get(),
                                                                                                self.dateborrowed_var.get(),
                                                                                                self.datedue_var.get(),
                                                                                                self.days_var.get(),
                                                                                                self.latereturnfine_var.get(),
                                                                                                self.dateoverdue_var.get(),
                                                                                                self.price_var.get(),
                                                                                                self.prnno_var.get(),
                                                                            ))
        conn.commit()
        self.fetch_data()
        self.reset()
        conn.close()

        messagebox.showinfo("Success","Information Updated")







    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost",user="root",password="Root123$",database="db")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * from new_library")
        rows=my_cursor.fetchall()

        if len(rows)!=0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("",END,values=i)
            conn.commit()
            conn.close()


    def get_cursor(self,event=""):
        cursor_row=self.library_table.focus()
        content=self.library_table.item(cursor_row) 
        row=content['values']
          
        self.member_var.set(row[0]),
        self.prnno_var.set(row[1]),
        self.title_var.set(row[2]),
        self.firstname_var.set(row[3]),
        self.lastname_var.set(row[4]),
        self.address1_var.set(row[5]),
        self.address2_var.set(row[6]),
        self.postid_var.set(row[7]),
        self.mobile_var.set(row[8]),
        self.bookid_var.set(row[9]),
        self.booktitle_var.set(row[10]),
        self.author_var.set(row[11]),
        self.dateborrowed_var.set(row[12]),
        self.datedue_var.set(row[13]),
        self.days_var.set(row[14]),
        self.latereturnfine_var.set(row[15]),
        self.dateoverdue_var.set(row[16]),
        self.price_var.set(row[17])

    def showData(self):
        self.txtBox.insert(END,"Member Type:\t\t"+self.member_var.get()+"\n")
        self.txtBox.insert(END,"PRN NO:\t\t"+self.prnno_var.get()+"\n")
        self.txtBox.insert(END,"First Name:\t\t"+self.firstname_var.get()+"\n")
        self.txtBox.insert(END,"Last Name:\t\t"+self.lastname_var.get()+"\n")
        self.txtBox.insert(END,"Address 1:\t\t"+self.address1_var.get()+"\n")
        self.txtBox.insert(END,"Address 2:\t\t"+self.address2_var.get()+"\n")
        self.txtBox.insert(END,"Post Code:\t\t"+self.postid_var.get()+"\n")
        self.txtBox.insert(END,"Mobile Number:\t\t"+self.mobile_var.get()+"\n")
        self.txtBox.insert(END,"Book ID:\t\t"+self.bookid_var.get()+"\n")
        self.txtBox.insert(END,"Book Title:\t\t"+self.booktitle_var.get()+"\n")
        self.txtBox.insert(END,"Author:\t\t"+self.author_var.get()+"\n")
        self.txtBox.insert(END,"Date Borrowed:\t\t"+self.dateborrowed_var.get()+"\n")
        self.txtBox.insert(END,"Date Due:\t\t"+self.datedue_var.get()+"\n")
        self.txtBox.insert(END,"Days on Book:\t\t"+self.days_var.get()+"\n")
        self.txtBox.insert(END,"Date Overdue:\t\t"+self.dateoverdue_var.get()+"\n")
        self.txtBox.insert(END,"Price:\t\t"+self.price_var.get()+"\n")

    def reset(self):
        self.member_var.set(""),
        self.prnno_var.set(""),
        self.title_var.set(""),
        self.firstname_var.set(""),
        self.lastname_var.set(""),
        self.address1_var.set(""),
        self.address2_var.set(""),
        self.postid_var.set(""),
        self.mobile_var.set(""),
        self.bookid_var.set(""),
        self.booktitle_var.set(""),
        self.author_var.set(""),
        self.dateborrowed_var.set(""),
        self.datedue_var.set(""),
        self.days_var.set(""),
        self.dateoverdue_var.set(""),
        self.latereturnfine_var.set(""),
        self.price_var.set("")
        self.txtBox.delete("1.0",END)

    def iExit(self):
        iExit=tkinter.messagebox.askyesno("Library","Do you want to exit?")
        if iExit>0:
            self.root.destroy()
            return


    def delete(self):
        if self.prnno_var.get()=="":
            messagebox.showerror("Error","First select the member")
        else:
            conn = mysql.connector.connect(host="localhost",user="root",password="Root123$",database="db")
            my_cursor = conn.cursor()
            query="delete from new_library where prnno=%s"
            value=(self.prnno_var.get(),)
            my_cursor.execute(query,value)

            conn.commit()
            self.fetch_data()
            self.reset()
            conn.close()

            messagebox.showinfo("Success","Member has been deleted")
            

        




if __name__=="__main__":
    
    main()