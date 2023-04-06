import re
import getpass

hangman_elements = [
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
        self.wrong_guess_cnt = 0
        self.is_in_phrase = False
        self.phrase_guess = ''
        self.full_phrase = phrase
        self.phrase = phrase.split()
        self.set_up()
    
    def inc_wrong_cnt(self):
        self.wrong_guess_cnt += 1

    def set_up(self):
        for word in self.phrase:
            for char in word:
                self.phrase_guess += '_ '
            self.phrase_guess += '  '
        print(self.phrase_guess)

    def phrase_update(self, guess):
        self.is_in_phrase = False
        if len(guess) > 1:
            if guess == self.full_phrase:
                    self.phrase_guess = guess
                    self.is_in_phrase = True
        elif len(guess) == 1:
            self.phrase_guess = ''
            for word in self.phrase:
                if guess in word:
                    self.is_in_phrase = True
                for char in word:
                    if char in self.list:
                        self.phrase_guess += char + ' '
                    else:
                        self.phrase_guess += '_ '
                self.phrase_guess += '  '
        
        
        if not self.is_in_phrase:
            self.inc_wrong_cnt()
        print(hangman_elements[self.wrong_guess_cnt]) #todo
        print(self.phrase_guess)
        print(self.list)
        print(pause)        
    
    def check_game(self):
        if not '_' in self.phrase_guess:            
            print('You won')
            return True
        elif self.wrong_guess_cnt == len(hangman_elements)-1:
            print('You lost')
            return True

    def add_guess(self):
        guess = input('Guess the letter or phrase: ')
        while True:
            if not re.match(r'^[a-zA-Z]+$', guess):
                guess = input('Please use letter: ')
            elif len(guess) > 1:
                self.phrase_update(guess.lower())
                break
            elif guess in self.list:                
                guess = input('Letter already used, use another: ')                    
            else:
                self.list.append(guess.lower())  
                self.phrase_update(guess.lower())
                break


if __name__ == '__main__':
    phrase = getpass.getpass('Input phrase to guess (only letters) ')
    while not re.match(r'^[a-zA-Z ]+$', phrase):
        phrase = getpass.getpass('Input phrase to guess (only letters) ')
    game = Hangman(phrase.lower())
    while True:
        game.add_guess()
        if game.check_game():
            break