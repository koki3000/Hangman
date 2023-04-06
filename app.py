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
        self.fullPhrase = phrase
        self.phrase = phrase.split()
    
    def incWrongCnt(self):
        self.wrongGuessCnt += 1

    def phraseUpdate(self, guess):
        self.isInPhrase = False
        if len(guess) > 1:
            if guess == self.fullPhrase:
                    self.phraseGuess = guess
                    self.isInPhrase = True
        elif len(guess) == 1:
            self.phraseGuess = ''
            for word in self.phrase:
                if guess in word:
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
        print(self.list)        
    
    def checkGame(self):
        if not '_' in self.phraseGuess:            
            print('You won')
            return True
        elif self.wrongGuessCnt == len(hangmanElementsList)-1:
            print('You lost')
            return True

    def addGuess(self):
        print(pause)
        guess = input('Guess the letter or phrase: ')
        while True:
            if not re.match(r'^[a-zA-Z]+$', guess):
                guess = input('Please use letter: ')
            elif len(guess) > 1:
                self.phraseUpdate(guess)
                break
            elif guess in self.list:                
                guess = input('Letter already used, use another: ')                    
            else:
                self.list.append(guess)  
                self.phraseUpdate(guess)
                break


if __name__ == '__main__':
    phrase = getpass.getpass('Input phrase to guess (only letters) ')
    while not re.match(r'^[a-zA-Z]+$', phrase):
        phrase = getpass.getpass('Input phrase to guess (only letters) ')
    game = Hangman(phrase)
    while True:
        game.addGuess()
        if game.checkGame():
            break