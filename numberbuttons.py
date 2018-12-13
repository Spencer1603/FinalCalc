'''
Created on Dec 11, 2018

@author: M.Spencer, M. Reilling, A. Hicks
'''
from tkinter import *
import tkinter.messagebox
import math
import os.path

class CalculatorFunction(CalculatorFrame):
    def __init__:
        super.__init__()
        
    def getandreplace(self, argi):
        '(',')'   'SQRT','^',
              
    def equals(self):
        #when the equal button is pressed
        self.getandreplace()
        try: 
            self.value= eval(self.newtext) #evaluate the expression using the eval function
        except SyntaxError or NameErrror:
            CalculatorFrame._displayArea.delete(0,END)
            CalculatorFrame._displayArea.insert(0,'Invalid Input!')
        else:
           CalculatorFrame.delete(0,END)
           CalculatorFrame.insert(0,self.value)
    
    def squareroot(self):
        #squareroot method
        tryExcept()
        else:
            self.sqrtval=math.sqrt(self.value)
            CalculatorFrame.delete(0,END)
            CalculatorFrame.insert(0,self.sqrtval)

    def square(self):
        #square method
        tryExcept()
        else:
            self.sqval=math.pow(self.value,2)
            CalculatorFrame.delete(0,END)
            CalculatorFrame.insert(0,self.sqval)
    
    def clearall(self): 
        #CE, or Clear Everything, clears the entry field
        self.e.delete(0,END)
    
    def clear1(self):
        #C, or Clear, deletes one entry
        self.txt=self.e.get()[:-1]
        self.e.delete(0,END)
        self.e.insert(0,self.txt)   
     
    def action(self, argi): 
        #Pressed button's value inserted at end of entry field
        if argi == "=":
            self.equals()
        elif argi == "C"
        elif argi == "CE"
        else:
            self.e.insert(END, argi)
            
class CalculatorFrame(Frame):
    def create_buttons(self):
        button_column = 0
        button_row = 1
        text_buttons = [['SQRT','^','(',')'] ['7','8','9','*'], ['4','5','6','/'], ['1','2','3','+'], ['0','.', 'C', 'CE'], ['=']]
        for button_rows in text_buttons:
            for text_button in button_rows:               
                self.config_button(text_button, button_row, button_column)
                button_column += 1
            button_row += 1
            button_column = 0
    
    def config_button(self, txt, button_row, button_column):
        key = list(self.create_buttons.keys())[list(self.create_buttons.values()).index(text_button)]
        self.calculator_buttons_texts[key] = tk.Button(self.master, text=text_button, width=12, command=lambda:CalculatorFunction.action(text_button))
        self.calculator_buttons_texts[key].config(padx=14, pady=12, font=("Arial", 18))
        self.calculator_buttons_texts[key].grid(row=button_row,column=button_column)
    
    def __init__(self, master):
    
        Frame.__init__(self)
        self.master.title("Calculator")
        self.grid()

        self._display = Frame(master)
        self._display.grid(row = 0, column = 0, rowspan = 2, columnspan = 5, sticky = N+S+E+W)
        self._displayArea = Text(self._display, width = 60, height = 10)
        self._displayArea.configure(font = ("Arial", 24, "bold"))
        self._displayArea.grid(row = 0, column = 0, sticky = N+S+E+W)
        self._displayArea.focus_set()
        
        #Number Buttons
        self.create_buttons()

          
                      
def main():
    cal = tk.Tk()
    Calculator(cal)
    cal.mainloop() 
    
main()               