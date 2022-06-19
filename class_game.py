import randomword

class game:

    def __init__(self, lives):

        self.lives = lives
        self.gameWord = randomword.chooseWord() #Using randonword.py to obtain a randomword.
        self.guessProgress = "_" * len(self.gameWord)
        self.guessedLetters = []

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

                self.guessedLetters.append(guess)
                self.loseLife()
                return ("Lives: " + str(self.lives)) , self.guessProgress, "Wrong guess!"

            else:

                self.guessedLetters.append(guess)

                #Treat as a list and perform list comprehension to gather all indices of a correct guess to update
                asList = list(self.guessProgress)
                indices = [i for i, letter in enumerate(self.gameWord) if letter == guess]

                for index in indices:
                    asList[index] = guess
                #Updates the guess progress
                guessProgress = "".join(asList)

                self.setGuessProgress(guessProgress)
                
                return ("Lives: " + str(self.lives)), self.guessProgress, "You guessed a letter correctly!"
        else:

            return ("Lives: " + str(self.lives)), self.guessProgress, "Input not valid, Enter a letter A-Z|a-z"

    #Check that the game is won/lost or still going returning an appropiate message
    def checkGameStatus(self):

        if (self.guessProgress == self.gameWord):

            return True, "You Won!, you have a use for something after all...."

        elif (self.lives <= 0):

            return True, ("You Lost, the word your feeble mind failed to compute was: " + self.gameWord)

        else:

            False, ""



#newgame = game(9)
#print("Gameword:  " + newgame.gameWord)
#print("Guess Progress: " + newgame.guessProgress)
#print("Lives: " + str(newgame.lives))

