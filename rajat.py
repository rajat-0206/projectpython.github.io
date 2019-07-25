import tkinter as tk
from tkinter import *
from tkinter import messagebox
import os
window=tk.Tk()
window.title("Jumple Juggle")
window.geometry('900x900')
window.configure(background="#82E0AA")    
def main():
    def login():
        flag=1
        user=phone.get()
        pas=password.get()
        if(str.isdigit(user)==False or len(user)!=10):
                messagebox.showerror("Signup", "Input a valid number")
                loginph.set("")
                flag=0
        if(flag==1):
            if(os.path.exists(user)):
                file=open(user,"rt")
                text=file.readline()
                text=text[0:-1]
                if(text==pas):
                    print(pas,text)
                else:
                    messagebox.showerror("Login","Wrong Password")
                    lpass.set("")
            else:
                msg=messagebox.askquestion("Login","This number is not registered.Do you want to signup?",icon='warning')
                if(msg=="yes"):
                    window.destroy()
                    signup()
    Label(window,text="LOGIN",fg="#E74C3C",bg="#82E0AA",font=("LOGIN", 48),justify="center").grid(row=1,column=5)
    Label(window,text="Phone Number",fg="Black",bg="#82E0AA",font=("Phone Number", 20),justify="left").grid(row=14)
    loginph= StringVar()
    phone=Entry(window,bd=3,fg="Black",cursor="mouse",bg="white",textvariable=loginph)
    phone.grid(row=14,column=4)
    lpass= StringVar()
    Label(window,text="Password",fg="Black",bg="#82E0AA",font=("Password", 20),justify="left",).grid(row=16)
    password=Entry(window,bd=3,fg="Black",cursor="mouse",bg="White",show="*",textvariable=lpass)
    password.grid(row=16,column=4)
    Loginbt=Button(window,text="Login",bg="#E74C3C",fg="black",height="2",width="6",font="YELLOWTAIL",relief="flat",activeforeground="white",activebackground="#E74C3C",command=login).grid(row=20,column=3)
    window.mainloop()

def signup():
    def register():
            flag=1
            phn=phone.get()
            if(str.isdigit(phone.get())==False or len(phone.get())!=10):
                messagebox.showerror("Signup", "Input a valid number")
                num.set("")
                flag=0
            nam=name.get()
            email=Email.get()
            pas=password.get()
            if(len(pas)<8):
                chkpas.set("")
                messagebox.showerror("Signup", "Password must be 8 character long")
                flag=0
            if(str.isalpha(nam)==False):
                messagebox.showerror("Signup","Name must be in letters")
                namvar.set("")
                flag=0
            if("@" not in email or ".com" not in email):
                messagebox.showerror("Signup", "Input a valid Email")
                em.set("")
                flag=0
            import os
            if(flag==1):
                if(os.path.exists(phone.get())):
                    messagebox.showerror("Signup", "This number is already registered")
                    num.set("")
                else:
                    file=open(phn,"wt")
                    file.write(pas)
                    file.write("\n")
                    file.write(nam)
                    file.write("\n")
                    file.write(email)
                    file.close()
                    messagebox.showinfo("Signup", "You are registered succesfully")
                    sign.destroy()
                    
            return
    sign=tk.Tk()
    sign.title("SIGN UP")
    sign.geometry("900x900")
    sign.configure(background="White")
    Label(sign,text="REGISTER",fg="Blue",bg="white",font=("REGISTER", 48),justify="center").grid(row=1)
    num= StringVar()
    Label(sign,text="Phone Number",fg="Black",bg="white",font=("Phone Number", 20),justify="left").grid(row=4)
    phone=Entry(sign,bd=3,fg="Black",cursor="mouse",bg="White",textvariable=num)
    phone.grid(row=4,column=4)
    Label(sign,text="Password",fg="Black",bg="white",font=("Password", 20),justify="left",).grid(row=6)
    chkpas= StringVar()
    password=Entry(sign,bd=3,fg="Black",cursor="mouse",bg="White",show="*",textvariable=chkpas)
    password.grid(row=6,column=4)
    Label(sign,text="Name",fg="Black",bg="white",font=("Name", 20),justify="left").grid(row=8)
    namvar= StringVar()
    name=Entry(sign,bd=3,fg="Black",cursor="mouse",bg="White",textvariable=namvar)
    name.grid(row=8,column=4)
    Label(sign,text="Email",fg="Black",bg="white",font=("Email", 20),justify="left",).grid(row=10)
    em= StringVar()
    Email=Entry(sign,bd=3,fg="Black",cursor="mouse",bg="White",textvariable=em)
    Email.grid(row=10,column=4)
    signupbt=Button(sign,text="Register",bg="Black",fg="White",height="2",width="6",command=register).grid(row=15,column=2)
    sign.mainloop()

main()