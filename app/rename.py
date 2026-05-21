from tkinter import *
from pathlib import Path

def rename_file():
    old_file = Path("files/mad-sokka.jpeg")
    new_file = Path("files/trial-renamed.jpeg")

    old_file.rename(new_file)

    label.config(text="Renamed successfully!")

window = Tk()

window.title("File Renamer")
window.geometry("300x200")

button = Button(window, text="Rename File", command=rename_file)
button.pack(pady=20)

label = Label(window, text="")
label.pack()

window.mainloop()