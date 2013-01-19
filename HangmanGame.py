# This is a simple hangman game. Simply load the file in python to play.

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    if secretWord == '':
        return True
    else:
        if secretWord[0] in lettersGuessed:
            return isWordGuessed(secretWord[1:],lettersGuessed)
        else:
            return False
     

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    final = ''
    for i in range(len(secretWord)):
        if secretWord[i] in lettersGuessed:
            final += secretWord[i]
        else:
            final += ' _'

    return final



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    alpha = string.ascii_lowercase
    final = ''
    for i in range(len(alpha)):
        if alpha[i] in lettersGuessed:
            ()
        else:
            final += alpha[i]

    return final

def welcome(secretWord):
    '''
    Loads the welcome text
    Requires secretWord
    '''
    text = 'Welcome to the game, Hangman!\n' + 'I am thinking of a word that is ' + str(len(secretWord)) + ' letters long.'
    return text

def setupText(lettersGuessed,numGuesses):
    '''
    Setup text for next guess
    Requires lettersGuessed,numGuesses
    '''
    text = '-------------\n' + 'You have ' + str(numGuesses) + ' guesses left.\n' + 'Available letters: ' + str(getAvailableLetters(lettersGuessed)) + '\n' + 'Please guess a letter: '
    return text

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.
    - Starts up an interactive game of Hangman.
    - Asks the user to supply one guess (i.e. letter) per round.
    - The user receives feedback immediately after each guess about whether their guess appears in the computers word.
    - After each round, displays to the user the partially guessed word so far, as well as letters that the user has not yet guessed.
    '''
    #setup for the game and first guess
    numGuesses = 8
    lettersGuessed = []
    print(welcome(secretWord))
    
    #loop of subsequent guesses
    while isWordGuessed(secretWord, lettersGuessed) != True:
        guess = raw_input(setupText(lettersGuessed,numGuesses))
        guess = guess.lower()
        if guess in secretWord:
            lettersGuessed += guess
            print('Good guess: ' + str(getGuessedWord(secretWord,lettersGuessed)))     
        elif guess in lettersGuessed:
            lettersGuessed += guess
            print("Oops! You've already guessed that letter: " + str(getGuessedWord(secretWord,lettersGuessed)))
        else:
            print("Oops! That letter is not in my word: " + str(getGuessedWord(secretWord,lettersGuessed)))
            if numGuesses == 1:
                break
            else:
                lettersGuessed += guess
                numGuesses -= 1
    if isWordGuessed(secretWord, lettersGuessed) == True:
        print('-------------\n' + 'Congratulations, you won!')
    else:
        print('-------------\n' + 'Sorry, you ran out of guesses. The word was ' + str(secretWord))



secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
