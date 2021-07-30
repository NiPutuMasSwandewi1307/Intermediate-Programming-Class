#import kivy
from kivy.app import App
from kivy.core import text
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder
import math as m
import kivy.utils

#import regular expression
import re

#Load kv file
Builder.load_file("calculator.kv")

#Root calculator application layout
class calculatorLayout(Widget):

    ####################################################
    # This method is executed when a number is pressed.#
    # input: the number that is pressed                #
    # output: add the number to the display label      #
    ####################################################
    def addNumber(self, number):
        # Get the current text displayed
        currentText = self.ids.displayLbl.text

        if (currentText == '0' or currentText=='Error!'):
            # Put the number on the display if nothing is there
            self.ids.displayLbl.text = number
        else:
            # If there is something displayed, get the last number
            lastNumber = re.split("\+|-|\*|/",currentText)[-1]
            if(lastNumber == '0'):
                # If the last number is 0, replace 0 with the number to avoid leading 0 (error in python)
                self.ids.displayLbl.text = self.ids.displayLbl.text[:-1] + number
            else:
                # Otherwise, add the number at the end
                self.ids.displayLbl.text += number

    #######################################################
    # This method is executed when an operator is pressed.#
    # input: the operator that is pressed                 #
    # output: add the operator to the display label       #
    #######################################################
    def addOperator(self, operator):
        # Get the current text displayed
        currentText = self.ids.displayLbl.text

        # Operator must follow a number
        lastChar = currentText[-1]
        if (lastChar in '0123456789'):
            self.ids.displayLbl.text += operator
    
    #Belum bener
    def calculate_sc(self,event):
        # print('btn..')
        currentText = self.ids.displayLbl.text
        btn = event.widget
        # text = btn['text']
        print(text)
        ex = currentText.get()
        result = ''
        if text == '^':
            print('pow')
            base, pow = ex.split(',')
            print(base)
            print(pow)
            result = m.pow(int(base), int(pow))
    
    #Rencananya make yang kayak gini karena masih sedikit bingung kalo angkanya lebih dari satu mau buat pow
    #dengan eval() gimana sebaiknya
# class Operations:
#     def __init__(self, num1=0, num2=0, ope=''):
#         self.num1= float(num1)
#         self.num2= float(num2)
#         self.ope= ope

#     def make_operation(self):
#         try:
#             if self.ope == "+":
#                 self.res= self.num1 + self.num2
#             elif self.ope == "-":
#                 self.res= self.num1 - self.num2
#             elif self.ope == "x":
#                 self.res= self.num1 * self.num2
#             elif self.ope == "/":
#                 try:
#                     self.res= self.num1 / self.num2
#                 except ZeroDivisionError as ex:
#                     print("sorry! you can't devide by 0")
#                     self.res= self.num1
#             elif self.ope == "%":
#                 self.res= self.num1 % self.num2
#             elif self.ope == "^":
#                 self.res= self.num1 ** self.num2
#             return self.res
#         except Exception as ex:
#             print('looks like you have a '+str(ex))


    ###################################################################################
    # Use python eval() function to calculate mathematical equation in the label.     #
    # input:                                                                          #
    # output: display calculation result in to label or Error! if exception is raised #
    ###################################################################################
    def calculate(self):
        # Get the current text displayed
        currentText = self.ids.displayLbl.text
        try:
            # Calculate result
            result = eval(currentText)
            # Remove trailing zero
            if(result==int(result)):
                result = int(result)
            # Display result
            self.ids.displayLbl.text = str(result)
        except:
            # Catch exception (calculation error)
            self.ids.displayLbl.text = "Error!"



    ##################################
    # Reset the display label to 0   #
    # input:                         #
    # output: 0 in the display label #
    ##################################
    def clear(self):
        self.ids.displayLbl.text = '0'

    #################################################################
    # Delete the last entry in the display lebel                    #
    # input:                                                        #
    # output: display text without the last character or 0 if empty #
    #################################################################
    def remove(self):
        # Get the current text displayed
        currentText = self.ids.displayLbl.text
        if (len(currentText)==1 or currentText=="Error!"):
            # If only one number or "Error!" in display, reset to 0
            self.ids.displayLbl.text = "0"
        else:
            # Else remove last character
            self.ids.displayLbl.text = currentText[:-1]

    ######################################################################
    # Add a decimal point to the last number, if it's an integer         #
    # input:                                                             #
    # output: add a decimal point to the last number, if it's an integer #
    ######################################################################
    def addPoint(self):
        # Get the current text displayed
        currentText = self.ids.displayLbl.text
        # Get the last number
        lastNumber = re.split("\+|-|\*|/",currentText)[-1]
        # Add decimal point only if there isn't one already
        if ('.' not in lastNumber and currentText != "Error!"):
            self.ids.displayLbl.text += '.'

# Kivy App Class
class calculator(App):
    def build(self):
        return calculatorLayout()

# Run Kivy App
if (__name__ == "__main__"):
    calculator().run()