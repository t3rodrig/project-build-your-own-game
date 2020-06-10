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

def get_guessed_word():
    pass

def get_available_letters():
    pass

def hangman():
    pass

if __name__ == '__main__':
    #word_list = load_words()
    #secret_word = choose_word(word_list).lower()
    secret_word = 'thermodynamics'
    print(secret_word)