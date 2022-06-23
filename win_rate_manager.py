import winrate_format
import pickle

#This class handles calculating winrates and saving it as well as loading them.
class win_rate_manager:

    def __init__(self, difficulty, wonGame):

        self.difficulty = difficulty
        self.wonGame = wonGame
        self.file = "winrate.pickle"

    def getWinRate(self):

        contents = self.openFile()

        for data in contents:

            if (data["difficulty"] == self.difficulty):

                return data["winrate"]

    #Called by other functions in class, not invoked otherwise
    def resetFile(self):

        with open(self.file,"wb") as file:

            dumpContents = (winrate_format.getFormat())
            pickle.dump(dumpContents, file)

    #Open file and view contents
    def openFile(self):

        with open(self.file,'rb') as file:

            contents = pickle.load(file)

            return contents

    #Opens file and updates the winrate
    def updateWinRate(self):

        winrateData = self.openFile()

        #Iterate through the list of dictionaries containing winrate data.
        for data in winrateData:

            if(data["difficulty"] == self.difficulty):

                data = self.calculateWinRate(data)

        with open(self.file,'wb') as file:
            pickle.dump(winrateData, file)

        testContents = self.openFile()
        print(testContents)

    def calculateWinRate(self, dict):

        #Increment games by 1 as game was played when this is called.
        dict["games"] += 1
        games = dict["games"]
        gamesWon = dict["wins"]
        
        #Increment wins by 1 is game is won
        if (self.wonGame):

            gamesWon += 1
            dict["wins"] = gamesWon

        #Update new winrate
        newWinrate = (gamesWon/games) * 100
        dict["winrate"] = newWinrate

        return dict



#newPickle = win_rate_manager("medium", True)
#newPickle.resetFile()
#pickleContents = newPickle.openFile()
#print(pickleContents)
    

        





