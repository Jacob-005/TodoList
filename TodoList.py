from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import datetime

mainwind=Tk()

def todo_lst_win():
    fname=user_name_entry.get()
    
    def open_file():
        lis=[]
        f=open(fname+".txt","r")
        global c
        r=f.read() 
        c=1
        for i in r:
            if i=='\n':
                c+=1
        f.close()
        f1=open(fname+".txt","r")
        for i in range(c):
            p=f1.readline()
            for j in p:
                if j!=" ":
                    list_box.insert(list_box.size(),p)
                    z=(list_box.get(0,END))
                    for i in z:
                        if i not in lis and i!='\n':
                            lis.append(i)
            list_box.delete(0,END)
            for k in lis:
                list_box.insert(list_box.size(),k) 
        f1.close()

    def add():
        tasks=entry.get()
        list_box.insert(list_box.size(),entry.get())
        entry.delete(0,END)


    def lis_box_del():
       
        for i in reversed(list_box.curselection()):
            list_box.delete(i)
    
    def del_all_lis():
        list_box.delete(0,END)

    def save():
        f=open(fname+".txt","w")
        l=[]
        for i in range(list_box.size()):
            task=str(list_box.get(i))
            l.append(task)
        for j in l:
            f.write(j+'\n')
        if f is None:
            return
        f.close()
   
    #Todo list window
    windows=Tk()

    w=400
    h=600

    screen_width=windows.winfo_screenwidth()
    screen_height=windows.winfo_screenheight()

    x=(screen_width/2)-(w/2)
    y=(screen_height/2)-(h/2)

    windows.geometry("%dx%d+%d+%d"%(w,h,x,y))


    windows.title("To-Do List")
    windows.config(background="#7e33e8")
    
    label=Label(windows,text="Tasks",fg="#ffffff",bg="#0004ff",font=("Arial",17))
    label.place(x=0,y=0)
    
    entry=Entry(windows,font=("Comic Sans MS",15),bg="#00FF00")
    entry.place(x=75,y=0)
    
    add_button=Button(windows,font="ComicSans",command=add,text="Add",bg="#120aff",fg="White")
    add_button.place(x=325,y=0)
    
    delete_all_button=Button(windows,font="ComicSansMS",text="Deleteall",command=del_all_lis,bg="#120aff",fg="White")
    delete_all_button.place(x=175,y=365)
    
    open_button=Button(windows,font="ComicSans",command=open_file,text="Load",bg="#120aff",fg="White")
    open_button.place(x=180,y=35)
    
    
    list_box=Listbox(windows,font=("Comic Sans MS",15),bg="#4361ee",selectmode=MULTIPLE)
    list_box.place(x=75,y=70)
    
    
    list_box_delbutton=Button(windows,font="ComicSansMS",text="Deletetask",command=lis_box_del,bg="#120aff",fg="White")
    list_box_delbutton.place(x=80,y=365)
    
    save_button=Button(windows,font="ComicSansMS",text="Save",command=save,bg="#120aff",fg="White")
    save_button.place(x=255,y=365)

def open_text():
    f=open(fname+"dry"+".txt","r")
    r=f.read()
    text.insert(END,r)
    f.close()

def save_text():
    f=open(fname+"dry"+".txt","w")
    g=text.get("1.0",END)
    f.write(g)
    f.close()
    
def delete():
    text.delete(1.0,END)

def login_diary():
    global text
    global fname
    fname=user_name_entry.get()
    ruf=open("Username Diary.txt","r")
    ur=ruf.read()
    sp=ur.split()
    if fname not in sp:
        messagebox.showerror(title='Error',message='Username Does not Exists')
    else:
        # Diary Window
        diarywind=Tk()
        diarywind.config(background='#7241ff')
        text=Text(diarywind,bg="#02fbff",font=("ComicSansMS",10),height=30,width=100,padx=10,pady=10,
                  fg="Medium Blue")
        text.pack(padx=10,pady=50)
        now=datetime.datetime.now()
        
        text.insert(1.0,now.strftime('%d/%m/%y'+' %H:%M:%S'))
        
        frame=Frame(diarywind,bg="pink",bd=3,relief=RAISED)
        frame.place(x=250,y=553)
        
        diry_label=Label(diarywind,text='Share your thoughts and story in your Diary',fg="Black",font=("News701 BT",16),
                         bg='#5a95ff')
        diry_label.place(x=150,y=10)

        save_button=Button(frame,text="Save",command=save_text,font=("ComicSansMS",16),bg="#8ea4fa",fg="White")
        save_button.pack(side=LEFT)

        open_button=Button(frame,text="Open",command=open_text,font=("ComicSansMS",16),bg="#8ea4fa",fg="White")
        open_button.pack(side=RIGHT)
        
        delete_button=Button(frame,text="Delete all",command=delete,font=("ComicSansMS",16),bg="#8ea4fa",fg="White")
        delete_button.pack(side=RIGHT)

        loginwndow.destroy()
        

def sign_diary():
    global text
    global fname
    fname=user_name_entry.get()
    ruf=open("Username Diary.txt","r+")
    ur=ruf.read()
    sp=ur.split()
    if fname in sp:
        messagebox.showerror(title='Error',message='Username Already Exists')
    
    else:
        uw=ruf.write(fname+'\n')
        ruf.close()
        
        # Diary Window
        diarywind=Tk()
        diarywind.config(background='#7241ff')
        text=Text(diarywind,bg="#02fbff",font=("ComicSansMS",10),height=30,width=100,padx=10,pady=10,
                  fg="Purple")
        text.pack(padx=10,pady=50)
        now=datetime.datetime.now()
        
        text.insert(1.0,now.strftime('%d/%m/%y'+' %H:%M:%S'))
        
        frame=Frame(diarywind,bg="pink",bd=3,relief=RAISED)
        frame.place(x=250,y=553)
        
        diry_label=Label(diarywind,text='Share your thoughts and story in your Diary',fg="Black",font=("News701 BT",16),
                         bg='#5a95ff')
        diry_label.place(x=150,y=10)

        save_button=Button(frame,text="Save",command=save_text,font=("ComicSansMS",16),bg="#8ea4fa",fg="White")
        save_button.pack(side=LEFT)

        open_button=Button(frame,text="Open",command=open_text,font=("ComicSansMS",16),bg="#8ea4fa",fg="White")
        open_button.pack(side=RIGHT)
        
        delete_button=Button(frame,text="Delete all",command=delete,font=("ComicSansMS",16),bg="#8ea4fa",fg="White")
        delete_button.pack(side=RIGHT)
        
        signupwndow.destroy()
    

def login_window():   
    fname=user_name_entry.get()
    f=open(fname+".txt","a")
    f.close()
    ruf=open("Username.txt","r")
    ur=ruf.read()
    sp=ur.split()
    if fname not in sp:
        messagebox.showerror(title='Error',message='Username Does not Exists')
    else:
        todo_lst_win()
        loginwndow.destroy()

def signup_window():
    fname=user_name_entry.get()
    f=open(fname+".txt","a")
    f.close()
    ruf=open("Username.txt","r+")
    ur=ruf.read()
    sp=ur.split()
    if fname in sp:
        messagebox.showerror(title='Error',message='Username Already Exists')
    
    else:
        uw=ruf.write(fname+'\n')
        ruf.close()
        todo_lst_win()
        signupwndow.destroy()

# Sign Up Window
def sign_up():
    global signupwndow
    
    signupwndow=Tk()
    
    global user_name_entry

    w=385
    h=120

    screen_width=signupwndow.winfo_screenwidth()
    screen_height=signupwndow.winfo_screenheight()

    x=(screen_width/2)-(w/2)
    y=(screen_height/2)-(h/2)

    signupwndow.geometry("%dx%d+%d+%d"%(w,h,x,y))
    
    signupwndow.title("Sign Up Window")
    signupwndow.config(background="#2d6ce0")
   
    frame=Frame(signupwndow,bd=1,relief=RAISED,bg="#6e3ade")
    frame.place(x=10,y=10)
    
    diary_swic_button=Button(frame,text="Diary",command=sign_diary,font=("ComicSansMS",12,"bold"),pady=4.5,padx=3,bg="#3f33e8",fg="White")
    diary_swic_button.grid(row=1,column=0,columnspan=1)
    
    login_winswic_button=Button(frame,text="Sign Up",command=signup_window,font=("ComicSansMS",14),bg="#3f33e8",fg="White")
    login_winswic_button.grid(row=1,column=1,columnspan=2)
    
    user_name_label=Label(frame,text="Username",fg="#ffffff",bg="#3f33e8",font=("ComicSansMS",17))
    user_name_label.grid(row=0,column=0)
    
    user_name_entry=Entry(frame,font=("Comic Sans MS",15),bg="#bf4ddb")
    user_name_entry.grid(row=0,column=1)
    user_name_entry.focus()
    
    mainwind.destroy()

# Login Window
def login():
    global loginwndow
    
    global user_name_entry
    
    loginwndow=Tk()
    
    global user_name_entry

    w=385
    h=120

    screen_width=loginwndow.winfo_screenwidth()
    screen_height=loginwndow.winfo_screenheight()

    x=(screen_width/2)-(w/2)
    y=(screen_height/2)-(h/2)

    loginwndow.geometry("%dx%d+%d+%d"%(w,h,x,y))

   
    loginwndow.title("Login Window")
    loginwndow.config(background="#2d6ce0")
   
    frame=Frame(loginwndow,bd=1,relief=RAISED,bg="#6e3ade")
    frame.place(x=10,y=10)
    
    diary_swic_button=Button(frame,text="Diary",command=login_diary,font=("ComicSansMS",12,"bold"),pady=4.5,padx=3,bg="#3f33e8",fg="White")
    diary_swic_button.grid(row=1,column=0,columnspan=1)
    
    sign_winswic_button=Button(frame,text="Login",command=login_window,font=("ComicSansMS",15),bg="#3f33e8",fg="White")
    sign_winswic_button.grid(row=1,column=1,columnspan=2)
    
    user_name_label=Label(frame,text="Username",fg="#ffffff",bg="#3f33e8",font=("ComicSansMS",17))
    user_name_label.grid(row=0,column=0)
    
    user_name_entry=Entry(frame,font=("Comic Sans MS",15),bg="#bf4ddb")
    user_name_entry.grid(row=0,column=1)
    user_name_entry.focus()
    
    mainwind.destroy()

# First Window
w=400
h=500

screen_width=mainwind.winfo_screenwidth()
screen_height=mainwind.winfo_screenheight()

x=(screen_width/2)-(w/2)
y=(screen_height/2)-(h/2)

mainwind.geometry("%dx%d+%d+%d"%(w,h,x,y))
mainwind.title("Sign Up Window")

frame1=Frame(mainwind)
frame1.pack()

photo=PhotoImage(file="Untitled.png")

bglabel=Label(frame1,image=photo)
bglabel.pack()

frame=Frame(frame1,bg="pink",bd=3,relief=RAISED)
frame.place(x=125,y=250)

signup_button=Button(frame,text="Sign Up",command=sign_up,font=("ComicSansMS",16),bg="#8ea4fa",fg="White")
signup_button.pack(side=LEFT)

login_button=Button(frame,text="Login",command=login,font=("ComicSansMS",16),bg="#8ea4fa",fg="White")
login_button.pack(side=RIGHT)

mainwind.mainloop()

