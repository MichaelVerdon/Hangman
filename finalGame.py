import tkinter as tk
import requests
import random

easyLives = 14
mediumLives = 10
hardLives = 7
lolLives= 4

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


def startButtonPress(button):

    button.destroy()
    buildGameElements()

def buildGameElements():

    textEntry = tk.Entry(root, text="Enter a letter", font="Arial")
    textEntry.place(relx=0.4,rely=0.5)
    submitButton = tk.Button(root, text="Submit", font="Arial", bd=4)        

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
easyButton = tk.Button(root, text='Easy', font="Arial", bd=4, command=lambda: startButtonPress())
easyButton.place(relx=0.4, rely=0.5)
mediumButton = tk.Button(root, text='Medium', font="Arial", bd=4, command=lambda: startButtonPress())
mediumButton.place(relx=0.5, rely=0.5)
hardButton = tk.Button(root, text='Hard', font="Arial", bd=4, command=lambda: startButtonPress())
hardButton.place(relx=0.6, rely=0.5)
lolButton = tk.Button(root, text='LOL', font="Arial", bd=4, command=lambda: startButtonPress())
lolButton.place(relx=0.7, rely=0.5)

#Create on screen elements
    

root.mainloop()