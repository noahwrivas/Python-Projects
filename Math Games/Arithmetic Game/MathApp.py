""" 
    Noah Rivas
    1/19/2019
    This program uses the Kivy Framework, therefore there is a '.kv' file that will need to be paired with 
    this file. The goal of this program is to help someone learn how to do basic math at a faster pace. 
    There will be random numbers that will appear of sizes that you can control, and the goal is to answer
    the expression as quickly as possible. The program allows you to make mistakes but you will not be able
    to contine until you get the question correct. You may restart by entering quit and any point. Quitting
    will reset your score but will allow you to choose 'game modes'. You can select what opperation you would 
    like to use by entering either '+', '-', '*', '/', or 'R' for random. The random mode will not choose one 
    at random but will instead change as the game progresses. You will have the option to choose an opperator
    when prompted in the beginning or after restarting. After, you must select the number of digits you would
    like to practice with. The number you enter will allow numbers to generate from 1 to (10^n)-1, where n 
    is the number that you selected.
"""

import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.properties import NumericProperty
from kivy.uix.behaviors.focus import FocusBehavior
import random, math
 
class MathGridLayout(GridLayout):
    score = NumericProperty(0)
    correct = NumericProperty(1)    
    digits = NumericProperty(2)
    count = NumericProperty(1)
    isDigitsSet = NumericProperty(0)
    isOpperandSet = NumericProperty(0)  
    add = NumericProperty(0)
    sub = NumericProperty(0)
    mul = NumericProperty(0)
    div = NumericProperty(0)
    rand = NumericProperty(0)   
    randOpperator = NumericProperty(0)

    def Game(self, text):
        """ Game Logic """
        self.setOpperand(text)
        self.setDigits(text)
        self.getNextNumbers()
        self.checkInput(text)
        self.restart(text)
        self.passNumbers()
        self.count += 1

    def setOpperand(self, text):
        """ Set the opperator for the game """
        if self.isOpperandSet == 0:
            try:
                if text == "+":
                    self.add = 1
                    self.isOpperandSet = 1
                elif text == "-":
                    self.sub = 1
                    self.isOpperandSet = 1
                elif text == "*":
                    self.mul = 1
                    self.isOpperandSet = 1
                elif text == "/":
                    self.div = 1
                    self.isOpperandSet = 1
                elif text == "R" or text == "r":
                    self.rand = 1
                    self.isOpperandSet = 1
                else:
                    print("Error, No Opperand")
            except Exception as e:
                print("setOpperand:\t" + str(e))

    def setDigits(self, text):
        """ Determine the number of digits used """
        if self.isOpperandSet == 1:
            if self.isDigitsSet == 0:     
                self.display.text = "How many digits?"
                try:
                    # only takes first symbol to limit maximum possible digits to 9
                    textinput = list(text)
                    textinput = "".join(textinput.pop(0))
                    # create a list of 9's and then join them together and convert to a list
                    nines = int("".join(["9" for i in range(int(textinput))]))
                    self.digits = nines
                    self.isDigitsSet = 1
                    print("try end")
                except Exception as e:
                    print("setDigits:\t" + str(e))

    def getNextNumbers(self):
        """ Generate the next set of numbers """
        self.nextRandNum1 = random.randrange(1, self.digits)
        self.nextRandNum2 = random.randrange(1, self.digits)
        if self.add == 1:
            self.nextRandAnswer = self.nextRandNum1 + self.nextRandNum2
        elif self.sub == 1:
            self.nextRandAnswer = abs(self.nextRandNum1 - self.nextRandNum2)
        elif self.mul == 1:
            self.nextRandAnswer = (self.nextRandNum1 * self.nextRandNum2)
        elif self.div == 1:
            if self.nextRandNum1 > self.nextRandNum2:
                self.nextRandAnswer = math.floor((self.nextRandNum1 / self.nextRandNum2))
            else:
                self.nextRandAnswer = math.floor((self.nextRandNum2 / self.nextRandNum1))
        elif self.rand == 1:
            # 1 => +, 2 => -, 3 => *, 4 => /
            randArray = [1, 2, 3, 4]
            self.randOpperator = random.choice(randArray)
            if self.randOpperator == 1:
                self.nextRandAnswer = self.nextRandNum1 + self.nextRandNum2
            elif self.randOpperator == 2:
                self.nextRandAnswer = abs(self.nextRandNum1 - self.nextRandNum2)
            elif self.randOpperator == 3:
                self.nextRandAnswer = (self.nextRandNum1 * self.nextRandNum2)
            else:
                if self.nextRandNum1 > self.nextRandNum2:
                    self.nextRandAnswer = math.floor((self.nextRandNum1 / self.nextRandNum2))
                else:
                    self.nextRandAnswer = math.floor((self.nextRandNum2 / self.nextRandNum1))
        else:
            self.nextRandAnswer = 0

    def checkInput(self, text):
        """ Check is answer was correct """
        if self.isDigitsSet == 1:
            if text:
                self.textbox.focus = True
                try:
                    if int(text) == self.currentRandAnswer:
                        self.score += 1
                        print("Correct, You answered {}".format(text))
                        self.correct = 1
                    else:
                        print("Incorrect, You guessed {}, the answer is {}".format(text, self.currentRandAnswer))
                except Exception as e:
                    pass

    def passNumbers(self):
        """ Pass new set to current set """
        if self.isDigitsSet == 1:
            if self.correct == 1:
                self.currentRandNum1 = self.nextRandNum1
                self.currentRandNum2 = self.nextRandNum2  
                self.currentRandAnswer = self.nextRandAnswer
                if self.add == 1 or (self.randOpperator == 1 and self.rand == 1):
                    self.display.text = str(self.currentRandNum1) + "   +   " + str(self.currentRandNum2)
                if self.sub == 1 or (self.randOpperator == 2 and self.rand == 1):
                    if self.currentRandNum1 > self.currentRandNum2:
                        self.display.text = "{}   -   {}".format(self.currentRandNum1, self.currentRandNum2)
                    else:
                        self.display.text = "{}   -   {}".format(self.currentRandNum2, self.currentRandNum1)
                if self.mul == 1 or (self.randOpperator == 3 and self.rand == 1):
                    self.display.text = "{}   *   {}".format(self.currentRandNum1, self.currentRandNum2)
                if self.div == 1 or (self.randOpperator == 4 and self.rand == 1):
                    if self.currentRandNum1 > self.currentRandNum2:
                        self.display.text = "{}   /   {}".format(self.currentRandNum1, self.currentRandNum2)
                    else:
                        self.display.text = "{}   /   {}".format(self.currentRandNum2, self.currentRandNum1)
                self.correct = 0   

    def restart(self, text):
        if text == "Quit" or text == "quit":
            self.score = 0
            self.count = 1
            self.isOpperandSet = 0
            self.isDigitsSet = 0
            self.add = 0
            self.sub = 0
            self.mul = 0
            self.div = 0
            self.rand = 0
            self.randOpperator = 0
            self.correct = 1
            self.digits = 2
            self.currentRandNum1 = None
            self.currentRandNum2 = None
            self.currentRandAnswer = None
            self.display.text = "Please enter an opperand\nex: '+'  '-'  '*'  '/'  or  'R'"

class MathApp(App):
    def build(self):
        return MathGridLayout()
 
MathApp = MathApp()
MathApp.run()