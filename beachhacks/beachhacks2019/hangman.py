#Hangman

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
    pass

def word_generator():
    pass

def get_user_character():
    pass

def matching_word(user_input):
    # holds the index of found letter in a list
    foundIndex = []
    found = []

    if user_input in word:
        for i in range(len(word)):
            if word[i] == user_input:
                foundIndex.append(i)
        for item in foundIndex:
            temp = foundIndex[item]
            found[temp] = user_input

        return found
    else:

        return user_input == -1


def hangman_menu():
    pass

def print_word():
    pass
        
        
