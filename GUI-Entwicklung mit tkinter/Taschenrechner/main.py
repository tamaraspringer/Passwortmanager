from tkinter import *


class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")
        
        self.display = Entry(master, width=15, font=('Roboto', 25), bd=0, bg='#F5F5F5', fg='#212121', justify=RIGHT)
        self.display.grid(row=0, column=0, columnspan=6, padx=6, pady=6)


        # Erstellen der Buttons
        self.create_button('C', 1, 0, bg='#25e9b9')
        self.create_button('(', 1, 1)
        self.create_button(')', 1, 2)
        self.create_button('/', 1, 3, bg='#25e9b9')
        self.create_button('7', 2, 0)
        self.create_button('8', 2, 1)
        self.create_button('9', 2, 2)
        self.create_button('*', 2, 3, bg='#25e9b9')
        self.create_button('4', 3, 0)
        self.create_button('5', 3, 1)
        self.create_button('6', 3, 2)
        self.create_button('-', 3, 3, bg='#25e9b9')
        self.create_button('1', 4, 0)
        self.create_button('2', 4, 1)
        self.create_button('3', 4, 2)
        self.create_button('+', 4, 3, bg='#25e9b9')
        self.create_button('C', 5, 0, bg='#25e9b9')
        self.create_button('0', 5, 1,)
        self.create_button('.', 5, 2)
        self.create_button('=', 5, 3, bg='#25e9b9')

        master.configure(bg='#4d616a')
        
    def create_button(self, text, row, column, columnspan=1, rowspan=1, bg='#E0E0E0', fg='#212121'):
        button = Button(self.master, text=text, width=7, height=3, font=('Roboto', 10), bg=bg, fg=fg, bd=0, command=lambda: self.button_click(text))
        button.grid(row=row, column=column, columnspan=columnspan, rowspan=rowspan, padx=2, pady=2)

    def button_click(self, text):
        if text == '=':
            try:
                result = str(eval(self.display.get()))
                self.display.delete(0, END)
                self.display.insert(0, result)
            except ZeroDivisionError:
                self.display.delete(0, END)
                self.display.insert(0, "Error: Division durch Null")
            except:
                self.display.delete(0, END)
                self.display.insert(0, "Error: Ungültige Eingabe")
        elif text == 'C':
            self.display.delete(0, END)
        else:
            self.display.insert(END, text)

root = Tk()
my_gui = Calculator(root)
root.geometry("290x370")
root.resizable(False, False)
root.iconbitmap("GUI-Entwicklung mit tkinter\Taschenrechner\icon.ico")
root.mainloop()
