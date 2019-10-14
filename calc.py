from tkinter import *
import math
import parser
import tkinter.messagebox

root = Tk() # constructor called
root.title('Calculator')

# calculator window
root.configure(background = 'Light Yellow') #  yellow for the window background
root.resizable(width = False, height = False) # user will not be able to resize the window
root.geometry("311x211") # dimensions for window

# calculator is the frame object
calculator = Frame(root)
calculator.grid()

class Calculator():
    def __init__(self):
        self.total = 0
        self.current = ''
        self.input_value = True
        self.check_sum = False
        self.operator = ''
        self.result = False

    def number_enter(self, num):
        self.result = False
        first_number = txtDisplay.get()
        second_number = str(num)
        
        if(self.input_value): # if input_value is True
            self.current = second_number
            self.input_value = False
            
        else:
            if(second_number == '.'):
                if(second_number in first_number):
                    return
            self_current = second_number + first_number
        self.display(self.current)
    
    def display(self, value):
        txtDisplay.delete(0, END)
        txtDisplay.insert(0, value)
        
add_numbers = Calculator() # calling constructor of calculator class


txtDisplay = Entry(calculator, font = ('Arial', 23), bg = 'Light Yellow', bd = 1, width = 18, justify = RIGHT)
# bd = 10 signifies border
txtDisplay.grid(row = 0, column = 0, columnspan = 4, pady = 1)
txtDisplay.insert(0, '0')

# digits on the calculator
numberpad = '789456123'
buttons = list()
i = 0
for j in range(2,5):
    for k in range(3):
        buttons.append(Button(calculator, width = 6, height = 1,
                    font = ('Arial', 13), bg = 'Light Yellow', bd = 1, text = numberpad[i]))
        buttons[i].grid(row = j, column = k, pady = 1)
        buttons[i]['command'] = lambda x = numberpad[i]: add_numbers.number_enter(x)
        i += 1
#_____________________________________________________STANDARD OPERATIONS_____________________________________________________#

clear_button = Button(calculator, text = 'C', width = 6, height = 1,
                      font = ('Arial', 13), bg = 'Light Yellow', bd = 1).grid(row = 1, column = 0, pady = 1)
clearall_button = Button(calculator, text = 'CE', width = 6, height = 1,
                      font = ('Arial', 13), bg = 'Light Yellow', bd = 1).grid(row = 1, column = 1, pady = 1)

delete_button = Button(calculator, text = '<del', width = 6, height = 1, font = ('Arial', 13),
                     bg = 'Light Yellow', bd = 1).grid(row = 1, column = 2, pady = 1)
add_button = Button(calculator, text = '+', width = 6, height = 1, font = ('Arial', 13),
                    bg = 'Light Yellow', bd = 1).grid(row = 1, column = 3, pady = 1)
sub_button = Button(calculator, text = '-', width = 6, height = 1, font = ('Arial', 13),
                    bg = 'Light Yellow', bd = 1).grid(row = 2, column = 3, pady = 1)
mult_button = Button(calculator, text = '*', width = 6, height = 1, font = ('Arial', 13),
                    bg = 'Light Yellow', bd = 1).grid(row = 3, column = 3, pady = 1)
div_button = Button(calculator, text = '÷', width = 6, height = 1, font = ('Arial', 13),
                    bg = 'Light Yellow', bd = 1).grid(row = 4, column = 3, pady = 1)

zero_button = Button(calculator, text = '0', width = 6, height = 1, font = ('Arial', 13),
                    bg = 'Light Yellow', bd = 1).grid(row = 5, column = 0, pady = 1)
dot_button = Button(calculator,text = '.', width = 6, height = 1, font = ('Arial', 13),
                    bg = 'Light Yellow', bd = 1).grid(row = 5, column = 1, pady = 1)
PM_button = Button(calculator,text = chr(177), width = 6, height = 1, font = ('Arial', 13),
                    bg = 'Light Yellow', bd = 1).grid(row = 5, column = 2, pady = 1)
equal_button = Button(calculator,text = '=', width = 6, height = 1, font = ('Arial', 13),
                    bg = 'Light Yellow', bd = 1).grid(row = 5, column = 3, pady = 1)

#____________________________________________________SCIENTIFIC OPERATIONS_____________________________________________________#

PI_button = Button(calculator, text = 'π', width = 6, height = 1,
                      font = ('Arial', 13), bg = 'Light Yellow', bd = 1).grid(row = 1, column = 4, pady = 1)
cos_button = Button(calculator, text = 'cos', width = 6, height = 1,
                      font = ('Arial', 13), bg = 'Light Yellow', bd = 1).grid(row = 1, column = 5, pady = 1)
tan_button = Button(calculator, text = 'tan', width = 6, height = 1, font = ('Arial', 13),
                     bg = 'Light Yellow', bd = 1).grid(row = 1, column = 6, pady = 1)
sin_button = Button(calculator, text = 'sin', width = 6, height = 1, font = ('Arial', 13),
                    bg = 'Light Yellow', bd = 1).grid(row = 1, column = 7, pady = 1)
#------------------------------------------------------------------------------------------------------------------------------
twoPI_button = Button(calculator, text = '2π', width = 6, height = 1, font = ('Arial', 13),
                    bg = 'Light Yellow', bd = 1).grid(row = 2, column = 4, pady = 1)
cosh_button = Button(calculator, text = 'cosh', width = 6, height = 1, font = ('Arial', 13),
                    bg = 'Light Yellow', bd = 1).grid(row = 2, column = 5, pady = 1)
tanh_button = Button(calculator, text = 'tanh', width = 6, height = 1, font = ('Arial', 13),
                    bg = 'Light Yellow', bd = 1).grid(row = 2, column = 6, pady = 1)
sinh_button = Button(calculator, text = 'sinh', width = 6, height = 1, font = ('Arial', 13),
                    bg = 'Light Yellow', bd = 1).grid(row = 2, column = 7, pady = 1)
#------------------------------------------------------------------------------------------------------------------------------
log_button = Button(calculator,text = 'log', width = 6, height = 1, font = ('Arial', 13),
                    bg = 'Light Yellow', bd = 1).grid(row = 3, column = 4, pady = 1)
exponent_button = Button(calculator,text = '^exp', width = 6, height = 1, font = ('Arial', 13),
                    bg = 'Light Yellow', bd = 1).grid(row = 3, column = 5, pady = 1)
mod_button = Button(calculator,text = '%', width = 6, height = 1, font = ('Arial', 13),
                    bg = 'Light Yellow', bd = 1).grid(row = 3, column = 6, pady = 1)
epsilon_button = Button(calculator,text = 'e', width = 6, height = 1, font = ('Arial', 13),
                    bg = 'Light Yellow', bd = 1).grid(row = 3, column = 7, pady = 1)
#------------------------------------------------------------------------------------------------------------------------------
log2_button = Button(calculator,text = 'log2', width = 6, height = 1, font = ('Arial', 13),
                    bg = 'Light Yellow', bd = 1).grid(row = 4, column = 4, pady = 1)
degree_button = Button(calculator,text = 'deg', width = 6, height = 1, font = ('Arial', 13),
                    bg = 'Light Yellow', bd = 1).grid(row = 4, column = 5, pady = 1)
obrace_button = Button(calculator,text = '(', width = 6, height = 1, font = ('Arial', 13),
                    bg = 'Light Yellow', bd = 1).grid(row = 4, column = 6, pady = 1)
cbrace_button = Button(calculator,text = ')', width = 6, height = 1, font = ('Arial', 13),
                    bg = 'Light Yellow', bd = 1).grid(row = 4, column = 7, pady = 1)
#------------------------------------------------------------------------------------------------------------------------------
fact_button = Button(calculator,text = 'x!', width = 6, height = 1, font = ('Arial', 13),
                    bg = 'Light Yellow', bd = 1).grid(row = 5, column = 4, pady = 1)
and_button = Button(calculator,text = '&&', width = 6, height = 1, font = ('Arial', 13),
                    bg = 'Light Yellow', bd = 1).grid(row = 5, column = 5, pady = 1)
or_button = Button(calculator, text = '||', width = 6, height = 1, font = ('Arial', 13),
                     bg = 'Light Yellow', bd = 1).grid(row = 5, column = 6, pady = 1)
not_button = Button(calculator,text = '!', width = 6, height = 1, font = ('Arial', 13),
                    bg = 'Light Yellow', bd = 1).grid(row = 5, column = 7, pady = 1)

#---------------------------------------------------Label---------------------------------------------------------------------#

label_display = Label(calculator, text='Scientific Calculator', font = ('Arial', 18), justify = CENTER)
label_display.grid(row = 0, column = 4, columnspan = 4)

#------------------------------------------MENU------------------------------------------#
def Exit():
    Exit = tkinter.messagebox.askyesno('Calculator', 'Do you want to exit: ')
    if(Exit > 0):
        root.destroy() # termination of program
        return
    
def Standard():
    root.resizable(width = False, height = False) # user will not be able to resize the window
    root.geometry("311x211") # dimensions for window

    
def Scientific():
    root.resizable(width = False, height = False) # user will not be able to resize the window
    root.geometry("568x211") # dimensions for window

    
menubar = Menu(calculator)

# toolbar menu -- File
filemenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = 'File', menu = filemenu)
# options under File Menu below: 
filemenu.add_command(label = 'Standard', command = Standard)
filemenu.add_command(label = 'Scientific', command = Scientific)
filemenu.add_separator() # separate Leave from above options
filemenu.add_command(label = 'Leave', command = Exit)

# toolbar menu -- Edit
editmenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = 'Edit', menu = editmenu)
# options under Edit Menu below: 
editmenu.add_command(label = 'Cut')
editmenu.add_command(label = 'Copy')
editmenu.add_command(label = 'Paste')

# toolbar menu -- Help
helpmenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = 'Help', menu = helpmenu)
# options under Help Menu below: 
helpmenu.add_command(label = 'View Help')

root.config(menu = menubar)
root.mainloop()
