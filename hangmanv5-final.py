import random
from sys import exit

print('H A N G M A N')
def menu():
    print('Type "play" to play the game, "exit" to quit:')
    menu = input(">")
    valid_response = True
    while valid_response:
        if menu == 'play':
            game()
        elif menu == 'exit':
            exit()
        else:
            print("Please type a valid response ")
            menu = input(">")

def game():
    word_choice = ['python', 'java', 'kotlin', 'javascript']

    comp_choice = random.choice(word_choice)
    lst = list(comp_choice)
    guess_data = set(lst)
    input_set = set()
    count = 0
    while count < 8:
        print()
        line = ''
        for letter in comp_choice:
            if letter in input_set:
                line += letter
            else:
                line += '-'

        print(line)
        if line == comp_choice:
            break

        print("Input a letter:>")

        guess = input()
        if len(guess) != 1:
            print("You should input a single letter")
        elif guess.isupper():
            print("It is not an ASCII lowercase letter")
        elif not guess.isalpha():
            print("It is not an ASCII lowercase letter")
        elif guess in guess_data and guess not in input_set:
            input_set.add(guess)
        elif guess in input_set:
            print("You already typed this letter")
        else:
            print("No such letter in the word")
            input_set.add(guess)
            count += 1

    if line == comp_choice:
        print("You guessed the word!")
        print('You survived!')
    else:
        print("You are hanged!")
    menu()

menu()
