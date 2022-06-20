import json

#This class handles calculating winrates and saving it as well as loading them.
class win_rate_manager:

    def __init__(self, difficulty, wonGame):

        self.difficulty = difficulty
        self.wonGame = wonGame
        self.file = "winrate.json"

    #Called by other functions in class, not invoked otherwise
    def openFile(self):

        with open(self.file, 'r') as f:
            fileContents = json.load(f)
            return fileContents
    
    #Resets file to original format
    def resetFile(self):

        baseContents = {
            'Winrates' : [
                {
                    'difficulty' : 'easy',
                    'games' : 0,
                    'wins' : 0,
                    'winrate' : 0.0
                },
                {
                    'difficulty' : 'medium',
                    'games' : 0,
                    'wins' : 0,
                    'winrate' : 0.0
                },
                {
                    'difficulty' : 'hard',
                    'games' : 0,
                    'wins' : 0,
                    'winrate' : 0.0
                },
                {
                    'difficulty' : 'lol',
                    'games' : 0,
                    'wins' : 0,
                    'winrate' : 0.0
                }
            ]
        }
        
        with open(self.file, 'w') as f:
            json.dump(baseContents, f)

    #Updates the win rate given the difficulty played on and if the game was won.
    def updateWinRate(self, difficulty, won):

        contents = self.openFile()
        for i, k in contents.items():

            print(i, k + "\n")

        json.dumps(contents)

        


        

newJson = win_rate_manager(2, True)
newJson.resetFile()
newJson.updateWinRate('Easy', True)
#string = newJson.openFile()
#print(type(string))
#print(string)
        





