import os
import sys
import tkinter as tr

from tkinter import filedialog, messagebox   # filedialog for open file and save file $messagebox is for confirm when saving file 
from tkinter import *                        # This is working for scroll function for my Task pad
from tkinter.messagebox import showinfo      # T0his is working for message box in help_menu to show my typed info
from tkinter import TkVersion                # This is for version info in help menu to show python and tkinter version
from datetime import datetime               # This is for Real Date and Time in my Task pad      

# Here i have used (simple) instead of (root)
simple= tr.Tk()                    
simple.title (" Task Pad (TP) ")
simple.geometry( '900x600' )

folder_path = os.path.dirname(os.path.abspath(r"C:\Users\DELL\Desktop\PROJECT 021"))
icon_path = os.path.join(folder_path, "taskpad.ico")

try:
    simple.iconbitmap(icon_path)
except Exception as e:
    print(f"Icon Error: {e}")

# Font setter/setting
text =tr.Text(
    simple,
    simple.title(" Untilted - Task "),
    wrap=tr.WORD,
    font=('Times New Roman', 14)
)

text.pack(expand=True,fill=tr.BOTH)

#new, open, save, exit
def new_tasks():
    simple.title( " Untitled - Task " )
    task =None
    text.delete(1.0, tr.END)

def open_tasks():
    file_path= filedialog.askopenfilename(
        defaultextension='.txt',
        filetypes = [("All Files ","*.*"),(" Task Files ", '*.txt' ,)]
    )

    if file_path:
        with open (file_path, 'r') as file:
                text.delete(1.0,tr.END)
                text.insert(tr.END, file.read())

def save_tasks():
    file_path =filedialog.asksaveasfilename(initialfile= 'untitled.txt',
        defaultextension= '.txt',
        filetypes = [("All Files ","*.*"),('Task Files,' ".txt")]
    )
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text.get (1.0, tr.END))
                                                                         
            messagebox.showinfo ("Info", ' The Task Was Saved Successfully ') # after saving pop/confirm alert will be displayed
    else:
         file = open( file='w')
         file.write


def print_task():
    content = text.get(1.0, tr.END)
    task_file = "print_task_file.txt"
    with open(task_file, "w") as file:
        file.write(content)
    try:
        if os.name == 'nt': 
            os.startfile(task_file, "print")
        
        messagebox.showinfo("Print", "Sent to printer successfully!")
    except Exception as E:
        messagebox.showerror("Error", f"Could not print: {E}")


def cut():
        text.event_generate(("<<Cut>>"))

def copy():
        text.event_generate(("<<Copy>>"))

def paste():
        text.event_generate(("<<Paste>>"))


#This is for real date and time in my Task pad   
def date_time():
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")  # Format: YYYY-MM-DD HH:MM:SS
    text.insert('insert', current_time)

font_size = 14  
def zoom_in():
    font_size += 4
    text.config(font=('Times New Roman', font_size))

def zoom_out():
    if font_size  >4: 
        font_size -= 2
        text.config(font=('Times New Roman', font_size))

#Message
def help_menu():
      showinfo("Task Pad Message" ,'''My Name is 'karthik.S'
Thanks For Visting on Task Pad''')
      
def version():
    messagebox.showinfo("Version Info", f"python version: {sys.version}\n Tkinter Version: {tr.TkVersion}")

#Scroll bar command for task pad
Scroll =Scrollbar(text)
Scroll.pack(side=RIGHT, fill=Y)
Scroll.config(command=text.yview)
text.config(yscrollcommand=Scroll.set)


Menubutton = tr.Menu(simple)
simple.config(menu=Menubutton)


ToDoList_menu=tr.Menu(Menubutton,tearoff=0)
Edit_menu =tr.Menu(Menubutton, tearoff=0)
date_time_menu = tr.Menu(Menubutton, tearoff=0)
zoom_menu = tr.Menu(Menubutton, tearoff=0)
Help_menu =tr.Menu(Menubutton, tearoff=0)

Menubutton.add_cascade(label='TodoList', menu=ToDoList_menu)
Menubutton.add_cascade(label='Edit',menu= Edit_menu)
Menubutton.add_cascade(label="Date & Time", menu= date_time_menu)
Menubutton.add_cascade(label="Zoom",menu= zoom_menu)
Menubutton.add_cascade(label="Help",menu= Help_menu)

ToDoList_menu.add_command(label="New", command= new_tasks)
ToDoList_menu.add_command(label='Open', command= open_tasks)
ToDoList_menu.add_command(label="Save", command= save_tasks)
ToDoList_menu.add_command(label="print", command= print_task)
ToDoList_menu.add_separator()
ToDoList_menu.add_command(label='Exit', command=simple.quit)

Edit_menu.add_command(label="cut_tasks", command= cut)
Edit_menu.add_command(label='copy_tasks', command= copy)
Edit_menu.add_command(label="paste_Tasks", command= paste)

date_time_menu.add_command(label="Real Date & Time", command= date_time)

zoom_menu.add_command(label="Zoom In", command= zoom_in)
zoom_menu.add_command(label="Zoom Out", command= zoom_out)

Help_menu.add_command(label="Message", command= help_menu)
Help_menu.add_command(label="version", command= version)

#This for my pop up Task pad
simple.mainloop()