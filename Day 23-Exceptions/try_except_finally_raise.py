# test out with 'try' if you can open the file to read in json.load (the file doesn't exist)
# if that does not work use 'except' to create a file
# use 'else' to update the old data with new_data and open the file to write( to receive information inside)
import json
website = web_entry.get()
email = e_user_entry.get()
user_password = pass_entry.get()


new_data = {
        website: {
            "email": email,
            "password": user_password,

        }
    }

if len(website) == 0 or len(user_password) == 0:
    messagebox.showinfo(title="Opsss", message="Please make sure you haven't left any fields empty."
else:
    try:
        # will try to open the file that does not exist if fail use 'except'
        with open("data.json", "r") as data_file:
            json.load(data_file)
    except FileNotFoundError:
        # will create a file from
        with open("data.json", "w") as data_file:
            json.dump(new_data, data_file)
    else:
        json.load(data_file).update(data_file)
        with open("data.json", "w") as data_file:
            json.dump(new_data, data_file)
    finally:
        web_entry.delete(0, END)
        pass_entry.delete(0, END)


import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
#TODO 1. Create a dictionary in this format:
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

def generate_phonetics():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letter in the alphabet please.")
        generate_phonetics()
    else:
        print(output_list)


generate_phonetics()


facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]


total_likes = 0
for post in facebook_posts:
    try:
        total_likes = total_likes + post['Likes']
    except KeyError:
        pass
        #print("Comments are not count as likes")

print(total_likes)

# The raise statement allows the programmer to force a specified exception to occur
