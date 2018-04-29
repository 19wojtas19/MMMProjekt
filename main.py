import TransferFunction
import PlotDraw
import Window


def read_dictionary():
    dictionary = {"b0": None, "a3": None, "a2": None, "a1": None, "a0": None }
    for key, value in dictionary.items():
        try:
            value = int(input(key))
        except ValueError:
            print("Not an integer!")
            return None
    return dictionary

def main():
    Window.mainwindow()
    dictionary = read_dictionary()
    tf = TransferFunction.TransferFunction(dictionary)
    pass

if __name__ == '__main__':
    main()
