from operator import truediv
import tkinter as tk
import randomword

class game:

    def __init__(self, lives):

        self.lives = lives
        self.gameWord = randomword.chooseWord() #Using randonword.py to obtain a randomword.
        self.guessProgress = "_" * len(self.gameWord)
        self.guessedLetters = [""]

    #Functions to change the variables of the game
    def loseLife(self):

        self.lives -= 1

    def setGuessProgress(self, guessProgress):

        self.guessProgress = guessProgress

    #Check to see if the guess is [A-Z|a-z] and is a single character
    @staticmethod
    def guessIsValid(guess):

        if (guess.isalpha() and len(guess) == 1):

            return True

        else:

            False

    #Make a guess and update variables accordingly
    #@staticmethod
    def makeGuess(self, guess):

        guess = guess.lower()

        #Check if the guess is just a single letter of alphabet 
        if (self.guessIsValid(guess)):

            if (guess in self.guessedLetters):

                return ("Lives: " + str(self.lives)), self.guessProgress, "Guess already made!"

            elif (guess not in self.gameWord):

                self.loseLife()
                return ("Lives: " + str(self.lives)) , self.guessProgress, "Enter a letter A-Z|a-z"

            else:

                self.guessedLetters.append(guess)

                asList = list(self.guessProgress)
                indices = [i for i, letter in enumerate(self.gameWord) if letter == guess]
                for index in indices:
                    asList[index] = guess
                guessProgress = "".join(asList)
                self.setGuessProgress(guessProgress)
                
                return ("Lives: " + str(self.lives)), self.guessProgress, "You guessed a letter correctly!"
        else:

            return ("Lives: " + str(self.lives)), self.guessProgress, "Input not valid, Enter a letter A-Z|a-z"

    def checkGameStatus(self):

        if (self.guessProgress == self.gameWord):

            return True, "You Won"

        elif (self.lives <= 0):

            return True, ("You Lost, word was: " + self.gameWord)

        else:

            False



#newgame = game(9)
#print("Gameword:  " + newgame.gameWord)
#print("Guess Progress: " + newgame.guessProgress)
#print("Lives: " + str(newgame.lives))

