from tkinter import *
import TransferFunction
import Ifstatement

WINDOW_HEIGHT = 300
WINDOW_WIDTH = 300


class Interface:
    b0 = "b0"
    a0 = "a0"
    a1 = "a1"
    a2 = "a2"
    a3 = "a3"


    def createString(self):
        string = "s^4 + " + str(self.a3)
        string += "*s^3 + " + str(self.a2)
        string += "*s^2 + " + str(self.a1)
        string += "*s^1 + " + str(self.a0)
        return string

    def __init__(self):
        self.root = Tk()

        self.b0_label = Label(master=self.root, text="b0: ").grid(row=0, column=0)
        self.b0_input = Entry(master=self.root)
        self.b0_input.grid(row=0, column=1)
        self.a0_label = Label(master=self.root, text="a0: ").grid(row=1, column=0)
        self.a0_input = Entry(master=self.root)
        self.a0_input.grid(row=1, column=1)
        self.a1_label = Label(master=self.root, text="a1: ").grid(row=2, column=0)
        self.a1_input = Entry(master=self.root)
        self.a1_input.grid(row=2, column=1)
        self.a2_label = Label(master=self.root, text="a2: ").grid(row=3, column=0)
        self.a2_input = Entry(master=self.root)
        self.a2_input.grid(row=3, column=1)
        self.a3_label = Label(master=self.root, text="a3: ").grid(row=4, column=0)
        self.a3_input = Entry(master=self.root)
        self.a3_input.grid(row=4, column=1)
        self.sinus = Radiobutton(master=self.root, text="Sinus signal", value=1).grid(row=5, column=0)
        self.recktangle = Radiobutton(master=self.root, text="Recktangle signal", value=2).grid(row=6, column=0)
        self.triangle = Radiobutton(master=self.root, text="Triangle signal", value=3).grid(row=7, column=0)

        self.start_button = Button(master=self.root, text="Start", command=self.start).grid(row=8, column=0)

        self.Routh_stability_check = Label(master=self.root, bg="yellow", width=3, height=1, text="R").grid(row=1, column=3)
        self.Hurwitz_stability_check = Label(master=self.root, bg="green", width=3, height=1, text="R-H").grid(row=3, column=3)

        self.tf_denominator_label = Label(master=self.root, text=self.b0).grid(row=1, column=2)
        self.tf_label = Label(master=self.root, text="----------------------------------------").grid(row=2, column=2)
        self.tf_numerator_label = Label(master=self.root, text=self.createString()).grid(row=3, column=2)


    def start(self):
        try:
            self.b0 = int(self.b0_input.get())
            self.a0 = int(self.a0_input.get())
            self.a1 = int(self.a1_input.get())
            self.a2 = int(self.a2_input.get())
            self.a3 = int(self.a3_input.get())
        except ValueError:
            print("Input must be an integer")
            return 0

        print(type(self.b0))
        self.tf_denominator_label = Label(master=self.root, text="                                                                   ").grid(row=1, column=2)
        self.tf_numerator_label = Label(master=self.root, text="                                                                    ").grid(row=3, column=2)                          #REFRESSSHHHHHHHHH
        self.tf_denominator_label = Label(master=self.root, text=self.b0).grid(row=1, column=2)
        self.tf_numerator_label = Label(master=self.root, text=self.createString()).grid(row=3, column=2)

        print(type(self.a3))
        parameters = TransferFunction.TransferFunction.read_dictionary(self.b0, self.a0, self.a1, self.a2, self.a3)
        is_routh_stable = Ifstatement.Ifstatement.routh_stability_check(parameters)
        if is_routh_stable:
            self.Routh_stability_check = Label(master=self.root, bg="green", width=3, height=1, text="R").grid(row=1, column=3)
        else:
            self.Routh_stability_check = Label(master=self.root, bg="red", width=3, height=1, text="R").grid(row=1, column=3)

        is_hurwitz_stable = Ifstatement.Ifstatement.hurwitz_stability_check(parameters)

        if is_hurwitz_stable == 1:
            self.Hurwitz_stability_check = Label(master=self.root, bg="green", width=3, height=1, text="R-H").grid(row=3, column=3)
        elif is_hurwitz_stable == 0:
            self.Hurwitz_stability_check = Label(master=self.root, bg="yellow", width=3, height=1, text="R-H").grid(row=3, column=3)
        else:
            self.Hurwitz_stability_check = Label(master=self.root, bg="red", width=3, height=1, text="R-H").grid(row=3, column=3)





    def mainwindow(self):
        self.root.title('Title')
        self.root.config(bg="white", width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
        self.root.mainloop()


#interface = Interface()


#interface.mainwindow()


