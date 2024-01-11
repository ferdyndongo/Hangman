# Write your code here
import random

list_words = ['python', 'java', 'kotlin', 'javascript']

print("H A N G M A N")
while True:
    chosen_word = random.choice(list_words)
    guessed_letters = '-' * len(chosen_word)
    given_letters = ""
    lives = 8
    to_do = input('Type "play" to play the game, "exit" to quit:')
    if to_do == "play":
        while lives > 0:
            guessed_letter = ""
            while True:
                print()
                print(guessed_letters)
                letter = input("Input a letter:")
                if letter.isalpha() and letter.islower() and len(letter) == 1:
                    break
                elif len(letter) != 1:
                    print("You should input a single letter")
                elif not letter.isalpha() or not letter.islower():
                    print("Please enter a lowercase English letter")
            if letter in chosen_word:
                for c in range(len(chosen_word)):
                    if chosen_word[c] == letter and guessed_letters[c] == '-':
                        guessed_letter += chosen_word[c]
                    else:
                        guessed_letter += guessed_letters[c]
                if guessed_letter == guessed_letters:
                    print("You've already guessed this letter")
                guessed_letters = guessed_letter
            elif letter not in given_letters:
                print("That letter doesn't appear in the word")
                lives -= 1
            else:
                print("You've already guessed this letter")
            given_letters += letter
            if guessed_letters == chosen_word:
                print(f"You guessed the word {chosen_word}!")
                print("You survived!")
                break
        else:
            print("You lost!")
        print()
    if to_do == "exit":
        break
