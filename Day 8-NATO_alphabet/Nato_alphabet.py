import pandas

# TODO 1. First create a dictionary in pandas format:
data = pandas.read_csv("nato_phonetic_alphabet.csv")
data.to_dict()
#print(data)

# dictionary comprehension
phonetic_code = {row.letter: row.code for(index, row) in data.iterrows()}
#print(phonetic_code)

# TODO 2. Create a list comprehension from a word that the user inputs.


user = input("Enter a word: ").upper()
code_list = [phonetic_code[letter] for letter in user]
print(code_list)
