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
    print('1. Play')
    print('2. Quit')

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
    choice = input('enter a letter: 
    pass

def matching_word(user_input):

    pass

def list_modifier(index, user_input):
                   
    
    length_list = len(list)

    for i in range(length_list - 1):
        underscore_list.insert(list[i], list[-1])
        underscore_list.pop(list[i] + 1)
                   
    return underscore_list

                   
def hangman_menu():
    key_word = word_generator()
    # add while loop count < 6:
    character_list = list_maker(key_word)
    print_word(character_list)
    user_input = get_user_character()
    matching_word(user_input)
    pass

def print_word():
    print(underscore_list)
    pass

    # prints out blanks and the letters that were found
        
print(list_maker("unoutlawed"))
