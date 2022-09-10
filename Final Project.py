"""
Program: Daily List
Author: Maurice Fingers
Date: 10 May 2022
Purpose: The purpose of this program is all user to enter daily task that the need to get done
and be able to delete them once they are completed. The can aslo click on the Affirmation button that
will allow them to be able to read the ones pre listed and input new ones that can make their day better.
"""



from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import os

root=Tk()

#Defines the functions.
def updateTasks():
    clear_listbox()
    for task in tasks:
        lb.insert("end", task)


def clear_listbox():
    lb.delete(0, "end")

def newTask():
    task = my_entry.get()
    if task != "":
        lb.insert(END, task)
        my_entry.delete(0, "end")
    else:
        messagebox.showwarning("Warning", "Task was not entered.")

def deleteTask():
    conf = messagebox.askquestion(
        "Delete Task","Are you sure you want to delete the task")
    print(conf)
    if conf.upper() =="YES":
        lb.delete(ANCHOR)
    else:
        pass
        

def deleteAllTask():
    conf = messagebox.askquestion(
        "Delete All", " Do you want to delete all task?")
    print(conf)
    if conf.upper() == "YES":
        global tasks
        tasks = []
        updateTasks()
    else:
        pass

#Opens up second window. 
def affirmationsTask():
    window = Toplevel()
    window.title("Affirmations")
    window.geometry("200x300+250+200")
    window.resizable(False,False)
    day =["I am enough\n", "I love myself\n",
          "I am worthy\n", "I am grateful\n", "I am focused\n",
          "I am strong\n", "I am in charge\n","I am powerful"]
    text = Text(window)
    text.configure(font=("Curlz MT",18))
    text.pack(pady=10,)
    for day in day:
        text.insert(END, day)

    

def exitTask():
    confex = messagebox.askquestion(
        "Confirmation"," Are you sure you want close all windows?")
    print(confex)
    if confex.upper() == "YES":
        root.destroy()
    else:
         pass


# Sets the size and title for the main page
root.geometry('450x450+400+200')
root.title("Daily List")
root.resizable(width=False, height=False)

#Displays the background image on the main page.
img_file = Image.open('flower.jpg')
bg = ImageTk.PhotoImage(img_file)
bgl = Label(root,image=bg)
bgl.place(x=0, y=0, relwidth=1,relheight=1)

frame = Frame(root)
frame.pack(pady=10)

#Creates the listbox for the Daily list page
lb = Listbox(
    frame,
    width=25,
    height=8,
    font=("Curlz MT", 16),
    bd=0,
    fg='#464646',
    highlightthickness=0,
    selectbackground='#a6a6a6',
    activestyle="none",
    
)
lb.pack(side=LEFT, fill=BOTH)

#The lis for the main page
task_list = [
    "Pick up kids",
    "Pay Bills",
    "Make Dinner",
    "Kids Bed Time",
    "Finish School Work",
    "Take trash out",
    "Do Laundry",
    "Mop Floors",
    "Date Night!!!"
    ]

for item in task_list:
    lb.insert(END, item)

#Makes the scrollbar for the listbox
sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

#Displays insert for Daily list
my_entry = Entry(
    root,
    font=("Curlz MT",20)
    )

my_entry.pack(pady=16)

#Creates frame for buttons
button_frame = Frame(root)
button_frame.pack(pady=10)

#Displays button 
addTask_btn = Button(
    button_frame,
    text='Add Task',
    font=("Curlz MT",12),
    bg='#c5f776',
    padx=20,
    pady=10,
    command=newTask
)
addTask_btn.pack(fill=BOTH, expand=True, side=TOP)

delTask_btn = Button(
    button_frame,
    text="Delete Task",
    font=("Curlz MT",12),
    bg='#ff8b61',
    padx=20,
    pady=10,
    command=deleteTask
)
delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

deleteAllTask_btn = Button(
    button_frame,
    text="Delete All",
    font=("Curlz MT",12),
    bg='#ff8b61',
    padx=20,
    pady=10,
    command=deleteAllTask
)
deleteAllTask_btn.pack(fill=BOTH, expand=True, side=LEFT)


affirmationsTask_btn = Button(
    button_frame,
    text="Affirmations",
    font=("Curlz MT",12),
    bg='#ff8b61',
    padx=20,
    pady=10,
    command= affirmationsTask
)
affirmationsTask_btn.pack(fill=BOTH, expand=True, side=LEFT)



exitTask_btn = Button(
    button_frame,
    text="Exit",
    font=("Curlz MT",12),
    bg='#ff8b61',
    padx=20,
    pady=10,
    command=exitTask
)
exitTask_btn.pack(fill=BOTH, expand=True, side=LEFT)


#End of main loop
root.mainloop()
