import pandas

nato_alphabet = pandas.read_csv('nato_phonetic_alphabet.csv')
nato_alphabet_dict = {row.letter:row.code for (index, row) in nato_alphabet.iterrows()}

user_input = input("Enter a Word\n").upper()

output_list = [nato_alphabet_dict[letter] for letter in user_input]

print(output_list)

