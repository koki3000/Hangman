import re
import getpass

hangmanElementsList = [
    '',
    """
     |
     |
    _|_
    """,
    """
     ___
     | /
     |/  
     |
     |
    _|_    
    """,
    """
     ______
     | /
     |/  
     |
     |
    _|_    
    """,
    """
     ______
     | /  |
     |/   O
     |  
     |   
     |
    _|_   
    """,
    """
     ______
     | /  |
     |/   O
     |    |
     | 
     | 
    _|_   
    """,
    """
     ______
     | /  |
     |/   O
     |   /|
     |   
     |   
    _|_   
    """,
    """
     ______
     | /  |
     |/   O
     |   /|\\
     |   
     |   
    _|_   
    """,
    """
     ______
     | /  |
     |/   O
     |   /|\\
     |    |
     |   
    _|_   
    """,
    """
     ______
     | /  |
     |/   O
     |   /|\\
     |    |
     |   /
    _|_   
    """,
    """
     ______
     | /  |
     |/   O
     |   /|\\
     |    |
     |   / \\
    _|_   
    """,

]

pause = '********************'

class Hangman:
    
    def __init__(self, phrase):
        self.list = []
        self.wrongGuessCnt = 0
        self.isInPhrase = False
        self.phraseGuess = ''
        self.phrase = phrase.split()
    
    def incWrongCnt(self):
        self.wrongGuessCnt += 1

    def phraseUpdate(self, newChar):
        self.isInPhrase = False
        self.phraseGuess = ''
        for word in self.phrase:
            if newChar in word:
                self.isInPhrase = True
            for char in word:
                if char in self.list:
                    self.phraseGuess += char + ' '
                else:
                    self.phraseGuess += '_ '
            self.phraseGuess += '  '
        
        
        if not self.isInPhrase:
            self.incWrongCnt()
        print(hangmanElementsList[self.wrongGuessCnt])
        print(self.phraseGuess)
    
    def checkGame(self):
        if not '_' in self.phraseGuess:            
            print('You won')
            return True
        elif self.wrongGuessCnt == len(hangmanElementsList)-1:
            print('You lost')
            return True

    def addLetter(self):
        print(pause)
        char = input('Guess the letter: ')
        while True:
            if not re.match(r'^[a-zA-Z]+$', char):
                char = input('Please use letter: ')
            elif len(char) > 1:
                char = input('Please use single letter: ')
            elif char in self.list:                
                char = input('Letter already used, use another: ')                    
            else:
                self.list.append(char)  
                self.phraseUpdate(char)
                print(self.list)
                break


if __name__ == '__main__':
    phrase = getpass.getpass('Input phrase to guess ')
    game = Hangman(phrase)
    while True:
        game.addLetter()
        if game.checkGame():
            break