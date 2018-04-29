import tkinter
from tkinter import messagebox as tkMessageBox
from tkinter import *

WINDOW_HEIGHT = 300
WINDOW_WIDTH = 300

root = Tk()

transfer_function_frame = Frame(master=root, width=600, height=200, bg="green").grid(row=0, column=1)
signal_frame = Frame(master=root, width=300, height=400, bg="red").grid(row=1)
plot_frame = Frame(master=root, width=600, height=400, bg="yellow").grid(row=1, column=1)
parameters_frame = Frame(master=root, width=300, height=200, bg="blue").grid(row=0, column=0)
b0_label = Label(master=parameters_frame, text="b0: ").grid(row=0, column = 0)
b0_input = Entry(master=parameters_frame).grid( row=0, column=0)
a0_label = Label(master=parameters_frame, text="b0: ").grid(row=0, column = 0)
a0_input = Entry(master=parameters_frame).grid(row=0, column=0)
a1_label = Label(master=parameters_frame, text="b0: ").grid(row=0, column = 0)
a1_input = Entry(master=parameters_frame).grid(row=0, column=0)
a2_label = Label(master=parameters_frame, text="b0: ").grid(row=0, column = 0)
a2_input = Entry(master=parameters_frame).grid(row=0, column=0)
a3_label = Label(master=parameters_frame, text="b0: ").grid(row=0, column = 0)
a3_input = Entry(master=parameters_frame).grid(row=0, column=0)



def ssijmifiuta():
    tkMessageBox.showerror("Title", "Content")



def mainwindow():
    root.title('Title')
    root.config(bg="white", width=WINDOW_WIDTH, height=WINDOW_HEIGHT)

    root.mainloop()

