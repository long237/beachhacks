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
    pass

def print_menu():
    pass

def word_generator():
    word_bank = []
    for word in open("words_alpha.txt"):
        word = word.strip()
        word_bank.append(word)
    key_word = random.choice(word_bank)
    return key_word

def list_maker(key_word):
    underscore_list = []
    for character in range(len(key_word)):
        underscore_list.append("_")
    return underscore_list


def get_user_character():
    pass

def matching_word(user_input):

    pass

def list_modifier(index, user_input):

    pass

def hangman_menu():
    lives = 6
    key_word = word_generator()
    while lives > 0:
        character_list = list_maker(key_word)
        print_word(character_list)
        user_input = get_user_character()
        index = matching_word(user_input)
        if index == -1:
            lives = lives -1
        character_list = list_modifier(index, user_input)
        print_word(character_list)
    pass

def print_word():
    pass
        
        
print(list_maker("unoutlawed"))
