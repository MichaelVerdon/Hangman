import requests
import random

import tkinter as tk



def main():

    #variables used in most functions
    global gameWord
    global guessProgress
    global chosenLetters

    #Acquire number of lives
    lives = getDifficulty()

    #Acquire variables 
    chosenLetters = []
    gameWord = chooseWord()
    guessProgress = ["_"] * len(gameWord)

    gameEnd = False

    #Game Loop
    print(guessProgress)
    #print(gameWord)

    while(gameEnd == False):

        tuple = makeGuess(lives, guessProgress) #Handles Guessing and returns progress + lives
        lives = tuple[0]
        guessProgress = tuple[1]
        gameEnd = checkGameStatus(lives)

    loseOrWin(lives)
    replay()


#This function chooses a random word using requests from a webpage
def chooseWord():

    #Initialises a webpage that is a list of words
    words_src = "https://www.mit.edu/~ecprice/wordlist.10000"
    randomWord = ""

    #Only picks words with a length of at least 6
    while (len(randomWord) < 6):

        #request to get words from webpage
        response = requests.get(words_src)

        #Get the word list and parse by newlines
        wordsList = response.content.splitlines()
        
        #Pick a random word 
        randomWord = random.choice(wordsList).lower().decode("utf-8")
    
    return randomWord


#Getting difficulty determines number of attempts you have
def getDifficulty():

    difficulty = input("Input 1-4 for a difficulty, 1-Easy 2-Medium 3-Hard 4-LOL: ")

    if (difficulty == "1"):

        attempts = 14

    elif (difficulty == "2"):

        attempts = 10

    elif (difficulty == "3"):

        attempts = 7

    else:

        attempts = 4

    return attempts


#Verify the guess input is valid
def verifyInput(word):

    if (word.isalpha()):

        inputIsValid = True

    else:

        inputIsValid = False
        print("Error, Please input a character in the alphabet")

    return inputIsValid


#Handles guess making
def makeGuess(lives, guessProgress):

    guess = input("Enter your guess: ")

    if (verifyInput(guess)):

        guess.lower()

        if (guess in chosenLetters):

            print("You have already guessed this word!")

            print(guessProgress)

        elif (guess not in gameWord):

            chosenLetters.append(guess)
            print("Incorrect guess")
            lives -= 1
            print("You have " + str(lives) + " remaining.")
            print(guessProgress)

        else:

            chosenLetters.append(guess)

            asList = list(guessProgress)
            indices = [i for i, letter in enumerate(gameWord) if letter == guess]
            for index in indices:
                asList[index] = guess
            guessProgress = "".join(asList)
                
            print(guessProgress)

    return lives, guessProgress

def checkGameStatus(lives):

    if (lives == 0 or guessProgress == gameWord):

        gameEnd = True

    else:

        gameEnd = False

    return gameEnd

def loseOrWin(lives):

    if (lives == 0):

        print("You are a failure.")
        print("The word you didn't have the brain capacity to compute was: " + gameWord)

    else:

        print("You Guessed the Word!")

def replay():

    status = input("Would you like to play again? y/n: ").lower()

    if (status == "y"):

        main()

    if (status == "x"):

        quit()

def GUI():

    #Create basic elements
    root = tk.Tk()
    root.resizable(False,False)
    canvas = tk.Canvas(root, height=720, width=1280, bg="#616A6B")
    canvas.pack()
    canvas.grid(columnspan=9, rowspan=16)

    welcomeMSG = "Welcome to Hangman, press the start button to play!"
    welcomeLabel = tk.Label(root, text=welcomeMSG, font="Arial", bg="#616A6B")
    welcomeLabel.grid(columnspan=4, column=1, row=1)

    root.mainloop() 

    

GUI()







