# Hangman.py
# Name: Rayan Bellahsni

# =============================================================================
#GAME RULES
# There are two versions of the game. You can choose to run Hangman with hints
# or without hints.
# You get 10 lives and each vowel you guess wrong is 2 lives off rather than 1.
# Consonants are just 1 life off.
# If you insert a character that is not a letter in the alphabet you get 3 warnings
# After the warnings are done, guesses are subtracted off.
# =============================================================================

import random
import string

WORDLIST_FILENAME = "wordsList.txt"


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



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

wordlist = load_words()






def is_word_guessed(secret_word, letters_guessed):
    for char in secret_word:
          if (char in letters_guessed) == False:
            guessed = False
            break
          else:
            guessed = True
        
    return guessed



def get_guessed_word(secret_word, letters_guessed):
    guessed_letters = []
    guessed = ""
    for letter in letters_guessed:
        if letter in secret_word:
            guessed_letters.append(letter)
    
    for char in secret_word:
        if char in guessed_letters:
          guessed += char
        else:
            guessed += "_ "
    
    return guessed

def get_available_letters(letters_guessed):

    
    letters = string.ascii_lowercase
    available = ""
    for char in letters:
        if char not in letters_guessed:
            available += char
    return available


"""
I figured out that it would be easier to make two new functions that will check warnings and guesses
since it will make it more simple for us in "def hangman"
this allows us to shorten the final code and make it more compact.
"""

def check_warnings(warnings_left, user_guess, same_guess, result):
  warnings_left -= 1
  
  
  if user_guess != user_guess.isalpha(): 
      
    print("That is not a letter. You have " , str(warnings_left), " warnings left: ", result)
    
  elif user_guess in same_guess:
      
    print("You have already guessed that letter. You have ", str(warnings_left) , " warnings left. ", result)
  print('-----------------')
  
  
  return warnings_left

"""
Same thing here. I made a function where it checks guesses.

"""
def check_guesses(guesses_left, user_guess, same_guess, result):
  guesses_left -= 1
  
  if not user_guess.isalpha():
    print("You have no warnings left so you lose one guess. " , result)
    
  elif user_guess in same_guess: 
    print("You've already guessed that letter. You have no warnings left so you lose one guess: ", result)
    
  else:
    print("That letter is not in the word: ", result)
    
  print("-----------------------")
  
  

  return guesses_left

    
# =============================================================================
#GAME EDITS
#For the game screen I added a list that shows all the characters that were chosen 
#along with the alphabet that shows up with the removed characters
#I also made the warning follow up with guesses left for a better experience for the user
#I also put some comments over the codes to explain better what I am doing.
# =============================================================================

def hangman(secret_word):
  
  letters_guessed = []
  same_guess = []
  warnings_left = 3
  guesses_remaining = 6
  unique_letters = ""
  result = "_ " * len(secret_word)
  
  
  
  for letter in secret_word:
      if letter not in unique_letters:
        
          unique_letters += letter
  
  print("Welcome to the game Hangman!")
  print("I'm thinking of a word that is " , str(len(secret_word)), " letter long.")
  print("-----------------------")

  """
  This is the most important part which lets the code runs while the game is not over. The game technically
  begins here since the "prints" on the top is just the introduction to the game.
  """
  while True: 
    letters_remain = get_available_letters(letters_guessed)
    
    print("You have ", str(guesses_remaining), " guesses left.")
    print("You have ", str(warnings_left), " warnings left.")
    print("Available letters: " , letters_remain)
    
    user_guess = (input("Please guess a letter: "))
    
    
    """
    .isalpha to make sure that user chose a letter. This is where the functions I create come in handy
    This part made it easier when I created those functions to check the lives left
    """
    
    if not user_guess.isalpha():

      if warnings_left > 0:
          warnings_left = check_warnings(warnings_left, user_guess, same_guess, result)
        
      elif guesses_remaining > 1: 
          guesses_remaining = check_guesses(guesses_remaining, user_guess, same_guess, result)
      else: 
          
          print("You have no more guesses. The word was " , secret_word)
          break
    
    else:

      if user_guess not in letters_guessed:
          letters_guessed.append(user_guess)
        
      game_is_done = is_word_guessed(secret_word, letters_guessed)
      
      
      
      """
      This make finishes the game as a victory printing the score at the end
      But it also has the elif and else functions to have different conditions
      of the game ending.
      """
      
      
      
      if game_is_done:
          print("Good guess: " , result)
          print("-----------------")
          print("Congrats, you won")
          total_score = guesses_remaining*len(unique_letters)
          print("Your total score for this game is: " , str(total_score))
          break
    
      elif user_guess in same_guess:
          
        if warnings_left > 0: 
            warnings_left = check_warnings(warnings_left, user_guess, same_guess, result)
          
        elif guesses_remaining > 1:
            guesses_remaining = check_guesses(guesses_remaining, user_guess, same_guess, result)
          
      elif (not(user_guess in same_guess)) and user_guess in secret_word:
          result = get_guessed_word(secret_word, letters_guessed)
          print("Good guess: " , result)
          print("-----------------")
        
      elif user_guess not in secret_word:
          
        if user_guess in ["a", "e", "i", "o", "u"] and guesses_remaining > 1:
            
            guesses_remaining = guesses_remaining - 1
            guesses_remaining = check_guesses(guesses_remaining, user_guess, same_guess, result)
          
        elif guesses_remaining > 1:
            guesses_remaining = check_guesses(guesses_remaining, user_guess, same_guess, result)
          
        else:
            print("That letter is not in the word: " , result)
            print("-----------------")
            print("Sorry, you ran out of guesses. The word was " , secret_word)
            break
        
    same_guess.append(user_guess)
    print(same_guess)




def match_with_gaps(my_word, other_word):
    """
    I used a zip down below to make it a tuple since that was my approach
    """
    my_word = my_word.replace(" ", "")
    if len(my_word) != len(other_word):
        return False
    for i, x in zip(my_word, other_word):
        if i == "_":
            continue
        if i != x:
            return False
    return True



def show_possible_matches(my_word):
    list1 = []
    for word in wordlist :
        if match_with_gaps(my_word, word) == True :
            list1.append(word)        

    return list1

"""
Seeing as the functions were no help and they didn't allow us to use "*" since isalpha() makes it that you cant use any 
other characters rather than alphabets. With that being said, we left the first one as it was with the newly defined functions
and decided to change this one completely so that the hints work.  This ended up being shorter anyways because we understood
how to make hangman better.
"""


def hangman_with_hints(secret_word):
    letters_guessed = []
    guesses_Left = 10
    warnings_Left = 3
    unique_letters = ""
    result = "_ " * len(secret_word)
    
    
    
    print("Welcome to the game Hangman!")
    print("I'm thinking of a word that is", len(secret_word), "letters long")
    print("-----------------------")


    

    while True:
        letters_remain =  get_available_letters(letters_guessed)
        print("You have ", str(guesses_Left), " guesses left.")
        print("You have ", str(warnings_Left), " warnings left")
        print("Available letters:", letters_remain) 

        user_guess = input("Please guess a letter: ")
        print("-----------------------")
       
        if user_guess.isalpha():
            if user_guess not in letters_guessed:   
                letters_guessed.append(user_guess)
                guessed_word = get_guessed_word(secret_word, letters_guessed)
                
                if user_guess in secret_word:
                    print("Good guess: ", guessed_word)
                else:
                    if user_guess in ["a", "e", "i", "o", "u"]:
                        guesses_Left -= 2
                    else:
                        guesses_Left -= 1  
                    print("That letter is not in the word:", guessed_word)
            else:
                if warnings_Left > 0:
                    warnings_Left -= 1
                    
                else:
                    guesses_Left -= 1
    
        elif user_guess == '*':
            print('Possible word matches are: ')
            print(show_possible_matches(guessed_word))
        
        else:
            if warnings_Left > 0:
                warnings_Left -= 1
            else:
                guesses_Left -= 1

        if is_word_guessed(secret_word, letters_guessed):
            unique_letters = []
            for char in secret_word:
                if char not in unique_letters:
                    unique_letters.append(char)

            print("Congrats, you won!")
            total_score = (guesses_Left * len(unique_letters))
            print("Your total score for this game is:", total_score)
            break

        if guesses_Left <= 0:
            print("Sorry, you ran out of guesses. The word was:", (secret_word))
            break


if __name__ == "__main__":
    #uncomment what version you want to play

     #secret_word = choose_word(wordlist)
     #hangman(secret_word)
     secret_word = choose_word(wordlist)
     hangman_with_hints(secret_word)
