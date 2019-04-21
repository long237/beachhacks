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

def matching_word(user_input, keyWord):
    # holds the index of found letter in a list
    index = []


    if user_input in keyWord:
        for i in range(len(keyWord)):
            if keyWord[i] == user_input:
                index.append(i)
        for item in foundIndex:
            temp = index[item]
            

        return index
    else:

        return user_input == -1


def hangman_menu():
    pass

def print_word():
    pass
        
        
