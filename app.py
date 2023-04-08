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
        self.end_game = ''
        self.full_phrase = phrase
        self.print_phrase()
    
    def inc_wrong_cnt(self):
        self.wrong_guess_cnt += 1

    def print_phrase(self):
        self.end_game = 'You won'
        for char in self.full_phrase:
            if char in self.list or char == ' ':
                print(char, end=' ')
            else:
                self.end_game = ''
                print('_', end=' ')
        print('')

    def phrase_update(self, guess):
        self.is_in_phrase = False
        if len(guess) > 1:
            if guess == self.full_phrase:
                    self.end_game = 'You won'
                    self.is_in_phrase = True
        elif len(guess) == 1:
            if guess in self.full_phrase:
                    self.is_in_phrase = True

        if not self.is_in_phrase:
            self.inc_wrong_cnt()
            if self.wrong_guess_cnt == len(hangman_elements)-1:
                self.end_game = 'You lost'
        print(hangman_elements[self.wrong_guess_cnt])
    
    def add_guess(self):
        guess = input('Guess the letter or phrase: ')
        while True:
            if not re.match(r'^[a-zA-Z]+$', guess):
                guess = input('Please use letter: ')
            elif len(guess) > 1:                
                self.list.append(guess.lower()) 
                self.phrase_update(guess.lower())
                break
            elif guess in self.list:                
                guess = input('Letter already used, use another: ')                    
            else:
                self.list.append(guess.lower())  
                self.phrase_update(guess.lower())
                break
        
        
        if self.end_game:
            print(self.full_phrase)
            print(self.end_game)
            return True
        else:
            self.print_phrase()
            if self.end_game:
                print(self.full_phrase)
                print(self.end_game)
                return True
            print(self.list)
            print(pause)
            return False


if __name__ == '__main__':
    phrase = getpass.getpass('Input phrase to guess (only letters) ')
    while not re.match(r'^[a-zA-Z ]+$', phrase):
        phrase = getpass.getpass('Input phrase to guess (only letters) ')
    game = Hangman(phrase.lower())
    while True:
        if game.add_guess():
            break