# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


#
def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

## end of helper code
#
## -----------------------------------
#
## Load the list of words into the variable wordlist
## so that it can be accessed from anywhere in the program
#wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    ctr=0
    for e in secret_word:
        for j in letters_guessed:
            if e==j:
                ctr+=1
    if ctr==len(secret_word):
        return True
    else:
        return False
    
        


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guessed_word=[]
    flag=0
    for e in secret_word:
        for f in letters_guessed:
            if f==e:
                flag=1
                guessed_word.append(e)
        if flag==0:
            guessed_word.append('_ ')
        flag=0
    return guessed_word        
                    


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    ctr=0
    available=[]
    for e in string.ascii_lowercase:
        available+=e
    for e in string.ascii_lowercase:
        for f in letters_guessed:
            if e==f:
                try:
                    available.remove(e)
                except:
                    pass
    return available
    
def is_guess_letter(guess):
    for e in string.ascii_lowercase:
        if guess==e:
            return True
    return False

def is_previous_guess(guess,letters_guessed):
    if len(letters_guessed)==1:
        return False
    for e in range(len(letters_guessed)-1):
        if letters_guessed[e]==guess:
            return True
    return False
def is_vowel(guess):
    if guess=='a' or guess=='e' or guess=='i' or guess=='o' or guess=='u':
        return True
    return False
def unique_count(secret_word):
    unique=[]
    unique_c=0
    flag=0
    for e in secret_word:
        for f in unique:
            if e==f:
                flag=1
        if flag==0:
            unique_c+=1
            unique.append(e)
        flag=0
    return unique_c
    
def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    letters_guessed=[]
    guess_left=6
    warning_left=3
    ctr=0
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is',str(len(secret_word)),'letter long')
    print('-------------')
    
    while guess_left>0 and warning_left>0: 
        print('You have',str(guess_left),' guess and',warning_left,'waning left')
        print('Available letters:',''.join(get_available_letters(letters_guessed)))
        guess=str(input('Please guess a letter: '))
        if guess.isalpha():
            letters_guessed+=guess
            for e in secret_word:
                if guess==e:
                    ctr=1
                    break
            if(is_previous_guess(guess,letters_guessed)):
                    warning_left-=1
            elif ctr==1:
                print('Good guess:',''.join(get_guessed_word(secret_word,letters_guessed)))
            
            else:
                if(is_vowel(guess)):
                    guess_left-=2
                    print('Oops that letter is not in my word:',''.join(get_guessed_word(secret_word,letters_guessed)))
                else:
                    guess_left-=1
                    print('Oops that letter is not in my word:',''.join(get_guessed_word(secret_word,letters_guessed)))
            ctr=0
            if is_word_guessed(secret_word,letters_guessed):
                print('Congratulations you won!')
                print('Your Score:',str(guess_left*unique_count(secret_word)))
                break
#        elif guess=='*':
#            reveal_word=''.join(get_guessed_word(secret_word,letters_guessed))
#            match_with_gaps(reveal_word)
        else:
            warning_left-=1
            print('Invalid entry, you have',str(warning_left),'warnings left')
    if guess_left<=0 or warning_left<=0:
        print('Sorry you loose! The word is:',secret_word)
# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



#def match_with_gaps(reveal_word):
#    '''
#    my_word: string with _ characters, current guess of secret word
#    other_word: string, regular English word
#    returns: boolean, True if all the actual letters of my_word match the 
#        corresponding letters of other_word, or the letter is the special symbol
#        _ , and my_word and other_word are of the same length;
#        False otherwise: 
#    '''
#    # FILL IN YOUR CODE HERE AND DELETE "pass"
#    inFile= open(WORDLIST_FILENAME,'r')
#    line=inFile.readline()    
#    wordlist=line.split()
#    for e in wordlist:
#       if len(e)==len(reveal_word) and  
#    new_word=reveal_word.strip('_ ')
#    
    



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



#def hangman_with_hints(secret_word):
#    '''
#    secret_word: string, the secret word to guess.
#    
#    Starts up an interactive game of Hangman.
#    
#    * At the start of the game, let the user know how many 
#      letters the secret_word contains and how many guesses s/he starts with.
#      
#    * The user should start with 6 guesses
#    
#    * Before each round, you should display to the user how many guesses
#      s/he has left and the letters that the user has not yet guessed.
#    
#    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
#      
#    * The user should receive feedback immediately after each guess 
#      about whether their guess appears in the computer's word.
#
#    * After each guess, you should display to the user the 
#      partially guessed word so far.
#      
#    * If the guess is the symbol *, print out all words in wordlist that
#      matches the current guessed word. 
#    
#    Follows the other limitations detailed in the problem write-up.
#    '''
#    # FILL IN YOUR CODE HERE AND DELETE "pass"
#    pass
#


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
#    # pass
#
#    # To test part 2, comment out the pass line above and
#    # uncomment the following two lines.
    wordlist=load_words()    
    secret_word = choose_word(wordlist)
    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
