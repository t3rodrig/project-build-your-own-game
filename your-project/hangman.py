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

if __name__ == '__main__':
    word_list = load_words()
    secret_word = choose_word(word_list).lower()
    print(secret_word)