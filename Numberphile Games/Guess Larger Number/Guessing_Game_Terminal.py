"""
This program simulates 2 people playing the following game together. Player one picks 2 random numbers hidden from 
player 1. Player 1 then picks their own random number then blindly picks one of the 2 numbers that player 2 picked.
Player 1 will then compare the number they randomly generated and the number that was revealed to them. Then make an
educated guess as to whether the hidden number is larger or smaller than the other number player 2 generated.

let 'a' = player 2's first number, let 'b' = player 2's second number, let 'n' = player 1's random number,

if a < n, then assume a < n < b,    if b < n, then assume b < n < a

this reasoning will provide a 16% increase in accuracy from it orginally being a 50% chance of guessing correctly.

Link: https://www.youtube.com/watch?v=ud_frfkt1t0 
"""

import random
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

class GuessingGame:
    
    def __init__(self, turns):
        self.gameRunning = True
        self.numOne = 0
        self.numTwo = 0
        self.randomNumber = 0
        self.chosenNumber = 0
        self.points = 0
        # self.guess = True #True = numOne larger, numTwo smaller,     False = numOne smaller, numTwo larger

    def randomNumberGeneration(self):
        self.numOne = random.uniform(-999999, 999999)
        self.numTwo = random.uniform(-999999, 999999)
        self.randomNumber = random.uniform(-999999, 999999)

    def simulate(self):
        self.chosenNumber = random.choice([self.numOne, self.numTwo])
        if self.chosenNumber == self.numOne:            
            if self.numOne > self.randomNumber:         
                if self.numOne > self.numTwo:           
                    self.points += 1   
                else:
                    pass
            else:
                if self.numOne < self.randomNumber:
                    if self.numOne < self.numTwo:
                        self.points += 1
                    else:
                        pass
        else:                                           
            if self.numTwo > self.randomNumber:         
                if self.numTwo > self.numOne:          
                    self.points += 1   
                else:
                    pass
            else:
                if self.numTwo < self.randomNumber:
                    self.guess = True
                    if self.numTwo < self.numOne:
                        self.points += 1
                    else:
                        pass

    def debug(self):
        if self.chosenNumber == self.numOne:            
            if self.numOne > self.randomNumber:         
                self.guess = True                       
                if self.numOne > self.numTwo:           
                    self.correct = True               
                else:
                    self.correct = False
            else:
                if self.numOne < self.randomNumber:
                    self.guess = False
                    if self.numOne < self.numTwo:
                        self.correct = True
                    else:
                        self.correct = False
        else:                                           
            if self.numTwo > self.randomNumber:         
                self.guess = False
                if self.numTwo > self.numOne:          
                    self.correct = True                 
                else:
                    self.correct = False
            else:
                if self.numTwo < self.randomNumber:
                    self.guess = True
                    if self.numTwo < self.numOne:
                        self.guess = True
                    else:
                        self.guess = False
        print("numOne: {}, numTwo: {}, rand: {}, chosenNum: {}, guess {}, correct: {}".format(self.numOne, self.numTwo, self.randomNumber, self.chosenNumber, self.guess, self.correct))
        
    def stats(self, round):
        accuracy = (self.points / (round + 1)) * 100
        print("Percent Accuracy: {}".format(accuracy))

    def run(self):
        for round in range(turns):
            self.randomNumberGeneration()
            self.simulate()
            # self.debug()
            self.stats(round)

if __name__ == "__main__":    
    turns = 100000
    GuessingGame(turns).run()
