import requests
import random

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

    except ConnectionRefusedError:

        print("Make sure you have wifi connection")
    
    return randomWord