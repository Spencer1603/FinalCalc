'''
Created on Dec 11, 2018

@author: M.Spencer, M. Reilling, A. Hicks
'''
from tkinter import *
import tkinter.messagebox
import math
import data

class CalculatorFunction():
    def __init__(self):
        CalculatorFrame.__init__()
        
    def getandreplace(self):
        self.expression = CalculatorFrame._displayArea.get()
        self.newtext=self.expression.replace('SQRT(','^')
        self.newtext=self.newtext.replace('math.sqrt(','**')
              
    def equals(self):
        #when the equal button is pressed
        self.getandreplace()
        try: 
            self.value = eval(self.newtext) #evaluate the expression using the eval function
        except SyntaxError or NameError:
            CalculatorFrame._displayArea.delete(0,END)
            CalculatorFrame._displayArea.insert(0,'Invalid Input!')
        else:
            CalculatorFrame._displayArea.delete(0,END)
            CalculatorFrame._displayArea.insert(0,self.value)
    
    def clearall(self): 
        #CE, or Clear Everything, clears the entry field
        CalculatorFrame._displayArea.delete(0,END)
    
    def clear1(self):
        #C, or Clear, deletes one entry
        self.txt = CalculatorFrame.get()[:-1]
        CalculatorFrame._displayArea.delete(0,END)
        CalculatorFrame._displayArea.insert(0,self.txt)   
     
    def action(self, argi): 
        #Pressed button's value inserted at end of entry field
        if argi == "=":
            self.equals()
        elif argi == "C":
            self.clear1()
        elif argi == "CE":
            self.clearall()
        else:
            CalculatorFrame._displayArea.insert(END, argi)
            
class CalculatorFrame(Frame):
    def __init__(self, master):
    
        tkinter.Frame.__init__(self, master)
        self.master = master
        self.master.title("Calculator")
        self.grid()
        
        self.button_dict = data.button_dict

        #creates and configures the display
        self._display = Frame(master)
        self._display.grid(row = 0, column = 0, columnspan = 5, sticky = N+S+E+W)
        self._displayArea = Text(self._display, width = 30, height = 10)
        self._displayArea.configure(font = ("Arial", 24, "bold"))
        self._displayArea.grid(row = 0, column = 0, sticky = N+S+E+W)
        self._displayArea.focus_set()

        self.create_buttons()
        
    def create_buttons(self):
        #loops through to assign values for each button
        button_column = 0
        button_row = 1
        i = 0
        self._text_buttons = data.button_rows
        self._text_val = data.button_vals
        for button_rows in self._text_buttons:
            for text_button in button_rows:             
                self.config_button(i, text_button, button_row, button_column)
                i += 1
                button_column += 1
            button_row += 1
            button_column = 0
    
    def config_button(self, i, text_button, button_row, button_column):
        #creates and configures buttons, using variables from loops
        n = list(self.button_dict.keys())[list(self.button_dict.values()).index(text_button)]
        self.button_dict[n] = tkinter.Button(self.master, text=text_button, width=6, command=lambda:CalculatorFunction.action(self=self, argi=text_button))
        self.button_dict[n].config(padx=6, pady=3, font=("Arial", 18))
        self.button_dict[n].grid(row=button_row,column=button_column)        
              
def main():
    #sets up our GUI
    cal = tkinter.Tk()
    CalculatorFrame(cal)
    cal.mainloop()
     
    
main() 