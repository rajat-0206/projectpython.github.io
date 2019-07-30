import tkinter as tk
from tkinter import *
from tkinter import messagebox
import os  
question1={"option":{1:"twice",2:"a day",3:"brush your",4:"teeth"},"answer":"brush your teeth twice a day "}
question2={"option":{1:"a story",2:"narrating",3:"tomorrow",4:"I will be"},"answer":"I will be narrating a story tomorrow "}
question3={"option":{1:"pray to",2:"we should",3:"daily",4:"god"},"answer":"we should pray to god daily "}
question4={"option":{1:"father",2:"my",3:"me",4:"trust"},"answer":"my father trust me "}
question5={"option":{1:"Delhi",2:"fort",3:"is in",4:"Red"},"answer":"Red fort is in Delhi "}
question6={"option":{1:"the",2:"ball",3:"with",4:"Rohan",5:"is playing"},"answer":"Rohan is playing with the ball "}
question7={"option":{1:"love",2:"of others",3:"good manners",4:"win the",5:"and respect"},"answer":"good manners win the love and respect of others "}
question8={"option":{1:"the",2:"the",3:"kept",4:"rail safe",5:"sleeper"},"answer":"the sleeper kept the rail safe "}
question9={"option":{1:"the",2:"jumped",3:"the dog",4:"pond",5:"into"},"answer":"the dog jumped into the pond "}
question10={"option":{1:"is",2:"to school",3:"late",4:"Rishu",5:"always"},"answer":"Rishu is always late to school "}
question11={"option":{1:"who is",2:"strangers",3:"respectful",4:"a person",5:"even",6:"like"},"answer":"even strangers like person who is respectful "}
question12={"option":{1:"saves us",2:"turns away",3:"a soft answer",4:"anger and",5:"a pitfall",6:"from many"},"answer":"a soft answer turns away anger and saves us from many a pitfall  "}
question13={"option":{1:"when",2:"best",3:"good manners can",4:"one is",5:"be learnt",6:"young"},"answer":"good amnners can be learnt best when one is young "}
question14={"option":{1:"deadly weapons",2:"of",3:"science has",4:"warfare",5:"given",6:"man"},"answer":"science has given man deadly weapons of warfare "}
question15={"option":{1:"armed",2:"which are",3:"miracles",4:"science has",5:"man with inventions",6:"not less than"},"answer":"science has armed man with inventions which are not less than miracles "}

level1=[]
level1.insert(0,question1)
level1.insert(1,question2)
level1.insert(2,question3)
level1.insert(3,question4)
level1.insert(4,question5)
level1.insert(5,question6)
level1.insert(6,question7)
level1.insert(7,question8)
level1.insert(8,question9)
level1.insert(9,question10)
level1.insert(10,question11)
level1.insert(11,question12)
level1.insert(12,question13)
level1.insert(13,question14)
level1.insert(14,question15)
exp=""
i=0
point=0
gameplay=0
def main():
    window=tk.Tk()
    window.title("Jumple Juggle")
    window.geometry('900x900')
    window.configure(background="#82E0AA")  
    window.iconbitmap("Game.ico")
    def login():
        flag=1
        user=phone.get()
        pas=password.get()
        if(str.isdigit(user)==False or len(user)!=10):
                messagebox.showerror("Login", "Input a valid number")
                loginph.set("")
                flag=0
        if(pas==""):
            messagebox.showerror("Login", "Enter password first")
            flag=0
        if(flag==1):
            if(os.path.exists(user)):
                file=open(user,"rt")
                text=file.readline()
                text=text[0:-1]
                if(text==pas):
                    window.destroy()
                    game(user)
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
                    main()
                    
            return
    sign=tk.Tk()
    sign.title("SIGN UP")
    sign.iconbitmap("Game.ico")
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
    
def game(phno):
    forward=phno
    global i
    global point
    global exp
    rajat=tk.Tk()
    rajat.configure(bg="#F1C40F")
    rajat.iconbitmap("Game.ico")
     #view profile
    def viewprofile():
        def hide():
            profileframe.destroy()
        profileframe=Frame(rajat,bg="#E74C3C",height="50",width="60")
        profileframe.grid(row=2,column=1,rowspan=50,columnspan="90",sticky="N")
        Label(profileframe,text="Profile",bg="#E74C3C",width="50").grid(row=1,column=0,columnspan="4")
        cut=Button(profileframe,text="X",command=hide,bg="#E74C3C",bd=0,highlightcolor="Red")
        cut.grid(row=1,column=4,sticky="E")
        file=open("8447234865","rt")
        file.readline()
        Label(profileframe,text="Phone Number:",bg="#E74C3C").grid(row=3,column=1,sticky="W")
        no=IntVar()
        Entry(profileframe,state="disabled",textvariable=no,justify="center",bd=0,disabledbackground="#E74C3C",disabledforeground="#17202A").grid(row=3,column=2,sticky="W")
        no.set(forward)
        Label(profileframe,text="Name:",bg="#E74C3C").grid(row=4,column=1,sticky="W")
        Name=StringVar()
        Entry(profileframe,state="disabled",textvariable=Name,justify="center",bd=0,disabledbackground="#E74C3C",disabledforeground="#17202A").grid(row=4,column=2,sticky="W")
        tempvar1=file.readline()
        Name.set(tempvar1)
        Label(profileframe,text="Phone Number:",bg="#E74C3C").grid(row=5,column=1,sticky="W")
        Emailid=StringVar()
        Entry(profileframe,state="disabled",textvariable=Emailid,justify="center",bd=0,disabledbackground="#E74C3C",disabledforeground="#17202A").grid(row=5,column=2,sticky="W")
        tempvar2=file.readline()
        Emailid.set(tempvar2)
        file.close()
    def logout():
        global exp
        global point
        global i
        exp=""
        i=0
        point=0
        rajat.destroy()
        main()
    user=Label(rajat,text="Hello Rajat",bg="#F1C40F",fg="#3498DB")
    user.grid(row=1,column=4,sticky="E")
    mb=  Menubutton (rajat, text="▼",bd=0,bg="#F1C40F",activebackground="#F1C40F",activeforeground="Blue")
    mb.grid(row=1,column=5,sticky="W")
    mb.menu =  Menu ( mb, tearoff = 0 )
    mb["menu"] =  mb.menu
    mb.menu.add_cascade( label="View Profile",command=viewprofile)
    mb.menu.add_cascade( label="Logout",command=logout)
    setans= StringVar()
    ansbox=Entry(rajat,text="",width="50",state="disabled",textvariable=setans)
    ansbox.grid(row=5,column=1,columnspan=5,sticky="W",ipady="3",pady="4")
    rajat.title("Jumble Juggle")
    file=open(phno,"rt")
    file.readline()
    usernam=file.readline()
    file.close()
    usernam="Hello "+str.capitalize(usernam)
    pointbox=Label(rajat,text="Points:",bg="#F1C40F")
    pointbox.grid(row=1,column=0,sticky="E")
    poin= IntVar()
    poin.set(point)
    setpoint=Entry(rajat,state="disabled",bd=0,textvariable=poin,disabledbackground="#F1C40F")
    setpoint.grid(row=1,column=1,sticky="W")
    poin.set(point)
    user=Label(rajat,text=usernam,bg="#F1C40F",fg="#3498DB")
    user.grid(row=1,column=4,sticky="E")
    def add(got):
        global exp
        exp=exp+got
        exp=exp+" "
        print(exp)
        setans.set(exp)
        forward=phno
    def check():
        global exp
        global point
        global i
        global gameplay
        if(exp==level1[i]["answer"]):
            print("true")
            exp=""
            setans.set(exp)
            point+=5
            i+=1
            rajat.destroy()
            gameplay+=1
            game(forward)
        else:
            exp=""
            setans.set(exp)
            i+=1
            rajat.destroy()
            gameplay+=1
            game(forward)
    def clear():
        global exp
        exp=""
        setans.set(exp)
    bt1=Button(rajat,text=level1[i]["option"][1],height="4",bg="#5DADE2",fg="#CB4335",bd=0,command=lambda: add(level1[i]["option"][1]))
    bt2=Button(rajat,text=level1[i]["option"][2],height="4",bg="#5DADE2",fg="#CB4335",bd=0,command=lambda: add(level1[i]["option"][2]))
    bt3=Button(rajat,text=level1[i]["option"][3],height="4",bg="#5DADE2",fg="#CB4335",bd=0,command=lambda: add(level1[i]["option"][3]))
    bt4=Button(rajat,text=level1[i]["option"][4],height="4",bg="#5DADE2",fg="#CB4335",bd=0,command=lambda: add(level1[i]["option"][4]))
    bt1.grid(row=3,column=1)
    bt2.grid(row=3,column=2)
    bt3.grid(row=3,column=3)
    bt4.grid(row=3,column=4)
    if(i>=5):
        bt5=Button(rajat,text=level1[i]["option"][5],height="4",bg="#5DADE2",fg="#CB4335",bd=0,command=lambda: add(level1[i]["option"][5]))
        bt5.grid(row=3,column=5)
    if(i>=10):
        bt6=Button(rajat,text=level1[i]["option"][6],height="4",bg="#5DADE2",fg="#CB4335",bd=0,command=lambda: add(level1[i]["option"][6]))
        bt6.grid(row=3,column=6)
    chk=Button(rajat,text="Submit",command=check,bd=0,width="5",height="2",bg="#E74C3C",fg="White")
    chk.grid(row=10,column=4,sticky="W",ipadx=3,ipady=2)
    ans=Label(rajat,text="Answer:",bg="#F1C40F")
    ans.grid(row=5,column=0,sticky="E")
    clr=Button(rajat,text="Clear",command=clear,bd=0,width="5",height="2",bg="#E74C3C",fg="White")
    clr.grid(row=10,column=3,sticky="E",padx=1,ipadx=3,ipady=2)
        #from here we are making instruction
    if(gameplay==0):
        def destroy():
            frame.destroy()
            frame=Frame(rajat,bg="#2ECC71")
        frame.grid(row=2,column=1,rowspan=50,columnspan="90",sticky="N")
        intro=Label(frame,text="Instruction",width="50",bg="#2ECC71")
        intro.grid(row=1,column=0,rowspan=2)
        cross=Button(frame,text="X",command=destroy,bg="#2ECC71",bd=0,highlightcolor="Red")
        t1=Label(frame,text="1. This game contain many boxes which contain different words written on them.",bg="#2ECC71",height="2")
        t1.grid(row=3,sticky="W")
        t2=Label(frame,text="2. You have to click on boxes in such a way that words when joined\ntogether form a meaningful sentece.",bg="#2ECC71",height="2")
        t2.grid(row=5,sticky="W")
        t3=Label(frame,text="3. Click on the submit button when you are sure sentence is meaningful.",bg="#2ECC71",height="2")
        t3.grid(row=7,sticky="W")
        t4=Label(frame,text="4. If you think you have clicked on wrong box, you can click on\nclear button to reset your answer.",bg="#2ECC71",height="2")
        t4.grid(row=9,sticky="W")
        t5=Label(frame,text="5. The game contain three level and 5 question in each level. ",bg="#2ECC71",height="2")
        t5.grid(row=11,sticky="W")
        t6=Label(frame,text="6. You will get 5 points on correct answer and 0 if answer is wrong. ",bg="#2ECC71",height="2")
        t6.grid(row=13,sticky="W")
        cross.grid(row=1,column=4,ipadx=2,ipady=2)
    rajat.mainloop()

main()