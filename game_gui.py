import tkinter as tk
import class_game

easyLives = 14
mediumLives = 10
hardLives = 7
lolLives = 4

def clickedSubmit(game, guess):

    #Variable for game info which is a list compromising of
    #lives, guessprogress, any error or messages to index and
    #update the gui information
    gameInfo = game.makeGuess(guess)
    currentLives, guessProgress, gameMessage = gameInfo
    livesLabel["text"] = currentLives
    guessLabel["text"] = guessProgress
    errorLabel["text"] = gameMessage

    #gameStatus = game.checkGameStatus() None object errors :(
    #gameEnd, endMessage = gameStatus

    #Return true if game is over
    if (game.checkGameStatus()):

        gameStatus = game.checkGameStatus()
        errorLabel["text"] = gameStatus[1] #Index game message, tuple unpacking worked too but kept giving none object errors.

        #Destroy submit button to stop more submits
        submitButton.destroy()

        #Call function to ask if user wants to restart game
        restartGameOption()


def restartGameOption():

    global restartLabel
    restartLabel = tk.Label(root, text="Would you like to play again?", font="Arial", bd=4)
    restartLabel.place(relx=0.3, rely=0.6)

    global yesButton
    yesButton = tk.Button(root, text="Go on son!", font="Arial", command=lambda: restartGame())
    yesButton.place(relx=0.3, rely=0.7)

    global noButton
    noButton = tk.Button(root, text="I've had enough!", font="Arial", command=lambda: quit())
    noButton.place(relx=0.5, rely=0.7)

#Restarts the game
def restartGame():

    #Destroys all game elements/widgets
    destroyGameElements()
    #Calls the difficulty selection function
    selectDifficulty()

#Widget genocide occuring here
def destroyGameElements():

    textEntry.destroy()
    submitButton.destroy()
    livesLabel.destroy()
    errorLabel.destroy()
    guessLabel.destroy()
    restartLabel.destroy()
    yesButton.destroy()
    noButton.destroy()

def buildGameElements(game):

    #Enter letter widget
    global textEntry
    textEntry = tk.Entry(root, text="Enter a letter", font="Arial", bd=4)
    textEntry.place(relx=0.4,rely=0.5)

    #Submit guess widget
    global submitButton
    submitButton = tk.Button(root, text="Submit", font="Arial", bd=4, command=lambda: clickedSubmit(game, textEntry.get()))
    submitButton.place(relx=0.45,rely=0.6)

    #Display lives widget
    global livesLabel
    livesLabel = tk.Label(root, text="Lives: " + str(game.lives), font="Arial", bd=4)
    livesLabel.place(relx=0.4,rely=0.2)

    #Display error messages
    global errorLabel
    errorLabel = tk.Label(root, text="Enter a letter A-Z|a-z", font="Arial", bd=4)
    errorLabel.place(relx=0.4,rely=0.25)

    #Shows guessing progress
    global guessLabel
    guessLabel = tk.Label(root, font="Arial", bd=4, text=game.guessProgress)
    guessLabel.place(relx=0.5,rely=0.2)


def startButtonPress(lives):

    destroyDifficultyButtons()
    game = class_game.game(lives)
    print(game.gameWord)
    buildGameElements(game)

# Destroy difficulty buttons after difficulty is selected
def destroyDifficultyButtons():

    easyButton.destroy()
    mediumButton.destroy()
    hardButton.destroy()
    lolButton.destroy()       

# Variables for screen size
screen_width = 1280
screen_height = 720

#Create basic elements
root = tk.Tk()
root.resizable(False,False)
root.title("Hangman")
root.iconbitmap('assets\smiling-face-with-horns.ico')

#Background elements
canvas = tk.Canvas(root, height=screen_height, width=screen_width, bg="#616A6B")

bg_image = tk.PhotoImage(file='assets\Background_00000.png')
bg_label = tk.Label(image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    
canvas.pack()

#Difficulty mode buttons

def selectDifficulty():

    global easyButton
    easyButton = tk.Button(root, text='Easy', font="Arial", bd=4, command=lambda: startButtonPress(easyLives))
    easyButton.place(relx=0.3, rely=0.5)

    global mediumButton
    mediumButton = tk.Button(root, text='Medium', font="Arial", bd=4, command=lambda: startButtonPress(mediumLives))
    mediumButton.place(relx=0.4, rely=0.5)

    global hardButton
    hardButton = tk.Button(root, text='Hard', font="Arial", bd=4, command=lambda: startButtonPress(hardLives))
    hardButton.place(relx=0.5, rely=0.5)

    global lolButton
    lolButton = tk.Button(root, text='LOL', font="Arial", bd=4, command=lambda: startButtonPress(lolLives))
    lolButton.place(relx=0.6, rely=0.5)

selectDifficulty()
root.mainloop()
