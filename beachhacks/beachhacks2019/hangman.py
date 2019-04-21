#Hangman
import random

def main():
    user_input = -1
    while user_input != 2:
        while user_input < 1 or user_input > 2:
            print_menu()
            user_input = int(input('Enter a selection: '))
        if user_input == 1:
            hangman_menu()
        elif user_input == 2:
            print("Goodbye")
            break
        user_input = -1

def print_menu():
    print("Main Menu")
    print("1. Play Hangman")
    print("2. Quit")

def word_generator():
    word_bank = []
    for word in open("words_alpha.txt"):
        word = word.strip()
        word_bank.append(word)
    key_word = random.choice(word_bank)
    return key_word

def matching_word(user_input, key_word):
    # holds the index of found letter in a list
    index = []


    if user_input in key_word:
        for i in range(len(key_word)):
            if key_word[i] == user_input:
                index.append(i) 

        return index
    else:

        return -1

def list_maker(key_word):
    underscore_list = []
    for character in range(len(key_word)):
        underscore_list.append("_")
    return underscore_list

def get_user_character():
    used_letters = []
    user_guess = input("Please enter a single lowercase letter. (Ex: a): ")
    
    while len(user_guess) > 1 or (user_guess.isalpha() == False):
        user_guess = input("Please enter a single lowercase letter. (Ex: a): ")
        used_letters.append(user_guess)
        if user_guess in user_guess:
            print("This letter has been used already. Please try again.")
            continue
    print(used_letters)
    return user_guess.lower()


def list_modifier(underscore_list,list_index, user_input):
                   
    
    length_list = len(list_index)

    for i in range(length_list):
        underscore_list.insert(list_index[i], user_input)
        underscore_list.pop(list_index[i] + 1)
                   
    return underscore_list


def hangman_menu():
    lives = 6
    # get the key word
    key_word = word_generator()
    print(key_word)
    # As long as the user has more than 0 lives, keep running.
    character_list = list_maker(key_word)
    print_word(character_list)
    while lives > 0 and ("_"  in character_list):

        user_input = get_user_character()
        index = matching_word(user_input, key_word)

        if index == -1:
            lives = lives -1
            print("remaining lives:", lives)
        else:
            character_list = list_modifier(character_list,index, user_input)
            print_word(character_list)
    if lives == 0:
        print("You lost")
        print("The word was:",key_word)
        print('')
    else:
        print("You won")
        print('')
def print_word(underscore_list):
    for character in underscore_list:
        print(character, end= ' ')
    print('')

    # prints out blanks and the letters that were found
        
main()










