import tkinter as tk
import randomword

class game:

    def __init__(self, lives, guessProgress, guessedLetters):

        self.lives = lives
        self.gameWord = randomword.chooseWord()
        self.guessProgress = guessProgress
        self.guessedLetters = guessedLetters

    def loseLife():

        game.lives -= 1

    def getLives():

        return game.lives

    def getGuessProgress():

        return game.guessProgress

    def setGuessProgress(guessProgress):

        game.guessProgress = guessProgress

    def getGuessedLetters():

        return game.guessedLetters

    def setGuessedLetters(guessedLetters):

        game.setGuessedLetters = guessedLetters

