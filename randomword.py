import requests
import random
import tkinter as tk

def chooseWord():

    #Initialises a webpage that is a list of words
    words_src = "https://www.mit.edu/~ecprice/wordlist.10000"
    randomWord = ""

    try:
    #Only picks words with a length of at least 6
        while (len(randomWord) < 6):

            #request to get words from webpage
            response = requests.get(words_src)

            #Get the word list and parse by newlines
            wordsList = response.content.splitlines()
        
            #Pick a random word 
            randomWord = random.choice(wordsList).lower().decode("utf-8")

    except:

        raiseError()
        print("Make sure you have wifi connection")
    
    return randomWord

#Open an error window telling the user there is no internet connection
def raiseError():

    root = tk.Tk()
    root.resizable(False,False)
    root.title("Error")
    canvas = tk.Canvas(root, height=100, width=150)
    canvas.pack()
    errorLabel = tk.Label(root, text="Error: No WIFI")
    errorLabel.configure(font=("Arial", 12))
    errorLabel.place(relx=0.1,rely=0.1)
    exitButton = tk.Button(root, height=2, width=8, text="Exit", command=lambda: exit())
    exitButton.place(relx=0.2,rely=0.35)
    root.mainloop()
