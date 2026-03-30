# Project-using-tkinter

# Task Pad (TP)

Task Pad is a lightweight, all-in-one desktop productivity tool built with Python. It features a versatile **Text Editor** for long-form writing and a dedicated **Task Manager** for tracking daily to-do items.

📂 How the Code Works (Line-by-Line)
1. Core Setup & Imports
import tkinter as tr: Imports the standard Python interface for creating the Graphic User Interface (GUI).
from tkinter import filedialog, messagebox: Adds specific "pop-up" tools for opening/saving files and showing alert messages.
from datetime import datetime: Imports the system clock to allow real-time date and time stamping.
simple = tr.Tk(): Initialises the main application window (the "root" of the project).
2. The Text Editor (Think Pad)
text = tr.Text(...): Creates the multi-line text entry widget where the user types their notes.
wrap=tr.WORD: A smart setting that ensures long words move to the next line instead of breaking in the middle.
text.pack(expand=True, fill=tr.BOTH): Tells the text box to stretch and fill the entire window automatically if the user resizes it.
3. Functional Logic (The "Brain")
def new_tasks(): Clears the text widget from the first character (1.0) to the very end (END) to start a fresh note.
def open_tasks(): Triggers a system "Open" window, reads the selected file’s content, and inserts it into the editor.
def save_tasks(): Grabs everything typed in the editor and writes it to a .txt file on the hard drive.
def date_time(): Fetches the current system time and "stamps" it at the cursor's current position using text.insert('insert', ...).
4. Zoom & Customisation
global font_size: Tells the function to modify the main font variable defined at the top of the script.
text.config(font=(..., font_size)): Dynamically updates the text area's appearance every time the user clicks "Zoom In" or "Zoom Out."
5. Menu System
Menubutton = tr.Menu(simple): Creates the top horizontal navigation bar.
add_cascade(...): Creates the drop-down categories (e.g., File, Edit, Help).
add_command(...): Links a specific text label (like "Save") to its Python function.
6. Execution
simple.mainloop(): The final engine that keeps the window open and "listens" for mouse clicks or keyboard typing.

output of my project

![image alt](https://github.com/karthik-s-22222/Project-using-tkinter/blob/46455869135faf6b0d10c1f0e69314a1a5d19a7a/output1.png)
![image alt](https://github.com/karthik-s-22222/Project-using-tkinter/blob/3e83b491d0272218f4c0cb7be49723e148c91db1/output2.png)
![image alt](https://github.com/karthik-s-22222/Project-using-tkinter/blob/3c2c53340e539f40b950f36a58f82c60dbc7df8c/output3.png)
![image alt](https://github.com/karthik-s-22222/Project-using-tkinter/blob/8d1429cec1bff07ad3c89069c4c576ce6a206ae8/output4.png)

## 🚀 Key Features

- **Think Pad (Editor):** A clean writing space with support for opening/saving files and timestamping.
- **Dynamic Zoom:** Quickly adjust text size (Zoom In/Out) for better readability.
- **Task Manager:** A structured list view to add, track, and delete specific tasks.
- **Data Persistence:** Tasks are automatically saved to `tasks.txt` and reloaded on startup.
- **Cross-Platform:** Runs on any system with Python installed (Windows, macOS, Linux).

## 🛠️ Built With

* [Python](https://www.python.org) - The programming language used.
* [Tkinter](https://docs.python.org) - Python's built-in GUI framework.

## 📥 Installation & Usage

1. **Clone the repository:**
   git clone https://github.com
or download by pressing code and zip file can be downloaded

