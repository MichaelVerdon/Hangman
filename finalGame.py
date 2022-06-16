import tkinter as tk
import randomword

easyLives = 14
mediumLives = 10
hardLives = 7
lolLives= 4

def startButtonPress(lives):

    destroyDifficultyButtons()
    buildGameElements(lives)

def buildGameElements(lives):

    textEntry = tk.Entry(root, text="Enter a letter", font="Arial", bd=4)
    textEntry.place(relx=0.4,rely=0.5)
    submitButton = tk.Button(root, text="Submit", font="Arial", bd=4)
    submitButton.place(relx=0.45,rely=0.6)
    livesLabel = tk.Label(root, text="Lives: " + str(lives), font="Arial", bd=4)
    livesLabel.place(relx=0.4,rely=0.2)

def destroyDifficultyButtons():

    easyButton.destroy()
    mediumButton.destroy()
    hardButton.destroy()
    lolButton.destroy()        

screen_width = 1280
screen_height = 720

#Create basic elements
root = tk.Tk()
root.resizable(False,False)
root.title("Hangman")
root.iconbitmap('assets\smiling-face-with-horns.ico')

#Background elements
canvas = tk.Canvas(root, height=screen_height, width=screen_width, bg="#616A6B")
canvas.grid(columnspan=18, rowspan=32)
bg_image = tk.PhotoImage(file='assets\Background_00000.png')
bg_label = tk.Label(image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    
canvas.pack()

#Difficulty mode buttons
easyButton = tk.Button(root, text='Easy', font="Arial", bd=4, command=lambda: startButtonPress(easyLives))
easyButton.place(relx=0.3, rely=0.5)

mediumButton = tk.Button(root, text='Medium', font="Arial", bd=4, command=lambda: startButtonPress(mediumLives))
mediumButton.place(relx=0.4, rely=0.5)

hardButton = tk.Button(root, text='Hard', font="Arial", bd=4, command=lambda: startButtonPress(hardLives))
hardButton.place(relx=0.5, rely=0.5)

lolButton = tk.Button(root, text='LOL', font="Arial", bd=4, command=lambda: startButtonPress(lolLives))
lolButton.place(relx=0.6, rely=0.5)

#Create on screen elements
    

root.mainloop()