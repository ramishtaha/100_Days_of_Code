#Step 1 

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

import random
word = word_list[random.randint(0, len(word_list) - 1)]

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

letter = input("Enter a Letter").lower()

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

for i in word:
    print(letter == i)