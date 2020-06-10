# Hangman game

import random

WORDLIST_FILENAME = 'wordlist.txt'

def load_words():
    '''
    Returns a list of valid words.
    '''
    print('Loading word list from file...')
    input_File = open(WORDLIST_FILENAME, 'r')
    content = input_File.read()
    word_list = content.split('\n')
    try:
        word_list.remove('')
    except ValueError:
        print('There is no empty string')
    print(f'\t {len(word_list)} words loaded.') 
    return word_list

def choose_word(word_list):
    '''
    Returns a word from word_list at random
    '''
    return random.choice(word_list)

def is_word_guessed(secret_word, letters_guessed):
    '''
    This function returns True if secret_word has been guessed 
    (ie, all the letters of secret_word are in letters_guessed)
    and False otherwise.

    Args:
        secret_word (str): the word the user is guessing.
        letters_guessed ([str]): what letters have been guessed so far.

    Returns:
        bool: True for success, False otherwise.
    '''
    is_in = [each_letter in letters_guessed for each_letter in secret_word]
    return all(is_in)

def get_guessed_word(secret_word, letters_guessed):
    '''
    This function returns a string that is comprised of letters and
    underscores, based on what letters in letters_guessed are in
    secret_word.

    Args:
        secret_word (str): the word the user is guessing.
        letters_guessed ([str]): what letters have been guessed so far.

    Returns:
        str: letters and underscores.
    '''
    list_of_chars = [each_letter if each_letter in letters_guessed else '_ ' for each_letter in secret_word]
    return ''.join(list_of_chars)

def get_available_letters(letters_guessed):
    '''
     This function returns all lowercase English letters that are
     not in letters_guessed.

     Args:
        letters_guessed ([str]): what letters have been guessed so far.

    Returns:
        str: lowercase English letters.
    '''
    from string import ascii_lowercase
    available = list(set(ascii_lowercase) - set(letters_guessed))
    available = sorted(available)
    return ''.join(available)

def hangman(secret_word):
    '''
    Starts up an interactive game of Hangman between the user
    and the computer.

    Args:
        secret_word (str): the word the user is guessing.
    '''
    print('Welcome to the game, Hangman!')
    print(f'I am thinking of a word that is {len(secret_word)} letters long.')
    print('-------------')

    mistakes_made = 0
    max_guess = 8

    letters_guessed = []
    is_winner = False
    is_done = False

    while not is_done:
        print(f'You have {max_guess - mistakes_made} guesses left.')
        available_letters = get_available_letters(letters_guessed)
        print(f'Available letters: {available_letters}')
        guess = input('Please guess a letter: ').lower()

        if guess in letters_guessed:
            print("Oops! You've already guessed that letter:", end=' ')
            print(get_guessed_word(secret_word, letters_guessed))
        elif guess in secret_word:
            letters_guessed.append(guess)
            print('Good guess:', end=' ')
            print(get_guessed_word(secret_word, letters_guessed))
            if is_word_guessed(secret_word, letters_guessed):
                is_winner = True
                is_done = True
        else:
            letters_guessed.append(guess)
            print('Oops! That letter is not in my word:', end=' ')
            print(get_guessed_word(secret_word, letters_guessed))
            mistakes_made += 1
            if mistakes_made == max_guess:
                is_done = True
        
        print('-------------')
    
    if is_winner:
        print('Congratulations, you won!')
    else:
        print(f'Sorry, you ran out of guesses. The word was {secret_word}')

if __name__ == '__main__':
    word_list = load_words()
    secret_word = choose_word(word_list).lower()
    hangman(secret_word)