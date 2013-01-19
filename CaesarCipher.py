# The code creates a "Caesar Cipher" which basically takes a message (message.txt) and 
# shifts the letters by a certain number of letters in the alphabet. This is determined
# by the "shift" argument in the buildCoder method.
# For more on Caesar Ciphers see: http://en.wikipedia.org/wiki/Caesar_cipher
#
# This code can also attempt to decode a message by matching the encoded message with a
# list of valid words (words.txt)

import string
import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    inFile = open(WORDLIST_FILENAME, 'r')
    wordList = inFile.read().split()
    print "  ", len(wordList), "words loaded."
    return wordList

def isWord(wordList, word):
    """
    Determines if word is a valid word.

    wordList: list of words in the dictionary.
    word: a possible word.
    returns True if word is in wordList.

    Example:
    >>> isWord(wordList, 'bat') returns
    True
    >>> isWord(wordList, 'asdf') returns
    False
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\\:;'<>?,./\"")
    return word in wordList

def randomWord(wordList):
    """
    Returns a random word.

    wordList: list of words  
    returns: a word from wordList at random
    """
    return random.choice(wordList)

def randomString(wordList, n):
    """
    Returns a string containing n random words from wordList

    wordList: list of words
    returns: a string of random words separated by spaces.
    """
    return " ".join([randomWord(wordList) for _ in range(n)])

def randomScrambled(wordList, n):
    """
    Generates a test string by generating an n-word random string
    and encrypting it with a sequence of random shifts.

    wordList: list of words
    n: number of random words to generate and scamble
    returns: a scrambled string of n random words

    NOTE:
    This function will ONLY work once you have completed your
    implementation of applyShifts!
    """
    s = randomString(wordList, n) + " "
    shifts = [(i, random.randint(0, 25)) for i in range(len(s)) if s[i-1] == ' ']
    return applyShifts(s, shifts)[:-1]

def getMessageString():
    """
    Returns a message in encrypted text.
    """
    return open("message.txt", "r").read()


#
# Encryption code
#
def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    coder = {}
    for i in range(26):
        coder[string.ascii_uppercase[i]] = string.ascii_uppercase[(shift + i) - 26]
    for i in range(26):
        coder[string.ascii_lowercase[i]] = string.ascii_lowercase[(shift + i) - 26]
    return coder

def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    codedword = ''
    for i in range(len(text)):
        if text[i] in string.ascii_letters:
            codedword += coder[text[i]]
        else:
            codedword += text[i]
    return codedword
    

def applyShift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. Lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.

    text: string to apply the shift to
    shift: amount to shift the text (0 <= int < 26)
    returns: text after being shifted by specified amount.
    """
    ### HINT: This is a wrapper function.
    return applyCoder(text, buildCoder(shift))
    

#
# Decryption code
#
def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.

    text: string
    returns: 0 <= int < 26
    """
    maxwordsfnd = 0
    bestshift = 0
    for i in range(26):
        testtext = applyShift(text, i)
        count = 0    
        for j in range(len(testtext.split(' '))):
            if isWord(wordList, (testtext.split(' '))[j]):
                count += 1
        if count > maxwordsfnd:
            maxwordsfnd = count
            bestshift = i
    return bestshift


def decryptMessage():
    """
    Using the methods you created in this problem set,
    decrypt the message given by the function getMessageString().
    Use the functions getMessageString and loadWords to get the
    raw data you need.

    returns: string - message in plain text
    """
    s = getMessageString()
    return applyShift(s, findBestShift(wordList, s))

    #return "Not yet implemented." # Remove this comment when you code the function

#
# Build data structures used for entire session and run encryption
#

if __name__ == '__main__':
    wordList = loadWords()
    decryptMessage()
