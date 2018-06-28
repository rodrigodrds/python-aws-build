# import opsutils  
import os
from tkinter import *
from tkinter import filedialog


if __name__ == "__main__":
    version = "1.0.1"
    print("="*25,f"v{version}", "="*25)
    name = input("Whats your name: ")
    print(f"Hello, {name}")
    input("pause...")
    pasta = os.path.expanduser("~")

    root = Tk()
    root.filename =  filedialog.askopenfilename(
        initialdir=pasta, 
        title="Select file", 
        filetypes = (("jpeg files","*.jpg"),("all files","*.*"))
    )
    filename = root.filename
    root.destroy()
    print(filename)
