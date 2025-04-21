import tkinter as tk
from tkinter import Tk, filedialog, messagebox
from tkinter import ttk


def m(root):
    l2 = tk.Label(root, text="PyWizardToolkit - 0.0.1")
    l2.pack(pady=10)

    l1 = tk.Label(root, text="Enter the program name.")
    l1.pack()

    e1 = tk.Entry(root)
    e1.pack(pady=10)

    l2 = tk.Label(root, text=f"Selected Folder: {''}.")
    l2.pack()

    b1 = tk.Button(root, text='Select Project Folder')
    b1.pack(pady=10)

    l3 = tk.Label(root, text=f"Selected File: {''}.")
    l3.pack()

    b2 = tk.Button(root, text='Select Project Main File')
    b2.pack(pady=10)

    pb = ttk.Progressbar(
    root,
    orient='horizontal',
    mode='determinate',
    length=280
    )
    pb.pack()

    b3 = tk.Button(root, text='Create Installer', command=pb.start)
    b3.pack(pady=10)








def main_screen():
    root = tk.Tk()
    root.title("PyWizardToolkit")
    root.geometry('950x400')
    root.resizable(False, False)
                
    m(root)

    root.iconify()
    root.update()
    root.deiconify()
    root.mainloop()

main_screen()