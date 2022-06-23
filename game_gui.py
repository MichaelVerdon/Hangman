import tkinter as tk
import class_game
import win_rate_manager

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
    guessedLettersLabel["text"] = game.guessedLetters

    #gameStatus = game.checkGameStatus() None object errors :(
    #gameEnd, endMessage = gameStatus
    gameStatus = game.checkGameStatus()
    #Return true if game is over
    if (gameStatus):

        errorLabel["text"] = gameStatus[1] #Index game message, tuple unpacking worked too but kept giving none object errors.

        #Destroy submit button to stop more submits
        submitButton.destroy()

        #Call function to ask if user wants to restart game
        restartGameOption()


def restartGameOption():

    #Create restart options
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
    main()


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
    guessedLettersLabel.destroy()
    guessedLettersIndicator.destroy()
    difficultyLabel.destroy()
    winrateLabel.destroy()


def buildGameElements(game):

    #I probably shouldve made these widgets into another object instead of
    #having alot of global variables. grim.
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

    #Shows guessed letters
    global guessedLettersLabel
    guessedLettersLabel = tk.Label(root, font="Arial", bd=4, text=game.guessedLetters)
    guessedLettersLabel.place(relx=0.4,rely=0.4)

    #Shows label indicating guessed letters
    global guessedLettersIndicator
    guessedLettersIndicator = tk.Label(root, font="Arial", bd=4, text="Guessed Letters:")
    guessedLettersIndicator.place(relx=0.25,rely=0.4)

    #Create difficulty label
    global difficultyLabel
    difficultyLabel = tk.Label(root, font="Arial", bd=4, text=winrateDisplay.difficulty.upper() + " WINRATE %:")
    difficultyLabel.place(relx=0.03,rely=0.1)

    #Display winrate for current difficulty
    global winrateLabel
    winrateLabel = tk.Label(root, font="Arial", bd=4, text=winrateDisplay.getWinRate())
    winrateLabel.place(relx=0.2,rely=0.1)

def startButtonPress(lives, difficulty):

    destroyDifficultyButtons()
    global game
    game = class_game.game(lives, difficulty)

    #Get winrate assets
    global winrateDisplay
    winrateDisplay = win_rate_manager.win_rate_manager(difficulty, False)

    print(game.gameWord)
    buildGameElements(game)

# Destroy difficulty buttons after difficulty is selected
def destroyDifficultyButtons():

    easyButton.destroy()
    mediumButton.destroy()
    hardButton.destroy()
    lolButton.destroy()
    resetDataButton.destroy()       

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

    global resetDataButton
    resetDataButton = tk.Button(root, text='Reset Winrate Data', font="Arial", bd=4, command=lambda: resetData())
    resetDataButton.place(relx=0.3,rely=0.8)

    global easyButton
    easyButton = tk.Button(root, text='Easy', font="Arial", bd=4, command=lambda: startButtonPress(easyLives, "easy"))
    easyButton.place(relx=0.3, rely=0.5)

    global mediumButton
    mediumButton = tk.Button(root, text='Medium', font="Arial", bd=4, command=lambda: startButtonPress(mediumLives, "medium"))
    mediumButton.place(relx=0.4, rely=0.5)

    global hardButton
    hardButton = tk.Button(root, text='Hard', font="Arial", bd=4, command=lambda: startButtonPress(hardLives, "hard"))
    hardButton.place(relx=0.5, rely=0.5)

    global lolButton
    lolButton = tk.Button(root, text='LOL', font="Arial", bd=4, command=lambda: startButtonPress(lolLives, "lol"))
    lolButton.place(relx=0.6, rely=0.5)

def resetData():

    winrateManager = win_rate_manager.win_rate_manager(None, None)
    winrateManager.resetFile()

def main():

    selectDifficulty()

if __name__ == "__main__":

    main()

root.mainloop()
