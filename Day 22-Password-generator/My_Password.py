from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    website1 = web_entry.get()
    email1 = e_user_entry.get()
    password2 = pass_entry.get()


    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # list comprehension
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    pass_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_pass():
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
        messagebox.showinfo(title="Opsss", message="Please make sure you haven't left any fields empty.")

# test out with 'try' if you can open the file to read in json.load (the file doesn't exist)
# if that does not work use 'except' to create a file
# use 'else' to update the old data with new_data and open the file to write( to receive information inside)
    else:
        try:
            with open("data.json", "r") as data_file:

                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)

            with open("data.json", "w") as data_file:

                json.dump(data, data_file, indent=4)
        finally:
            web_entry.delete(0, END)
            pass_entry.delete(0, END)

# ---------------------------- FIND PASSWORD ---------------------

# check if web's text entry matches an item in the data.json
# if yes, show a messagebox with the website's name and password
# catch an exception that might occur trying to access the data.json
# then show a messagebox with the text: "No Data File Found"
# if the user's website does not exist inside the data.json
# finally show a messagebox that reads "No details for the website exists".

def find_password():
    website = web_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("My Password")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
padlock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=padlock_image)
canvas.grid(row=0, column=1)

# __________________________________________________________________________________________________________ #
# labels web column 0
web_label = Label(text="Website:")
web_label.grid(row=1, column=0, sticky="W")

# labels user
e_user_label = Label(text="Email/Username:")
e_user_label.grid(row=2, column=0, sticky="W")

# labels password
pass_label = Label(text="Password:")
pass_label.grid(row=3, column=0, sticky="W")

# __________________________________________________________________________________________________________ #
# web entries
web_entry = Entry(width=35)
web_entry.grid(row=1, column=1, sticky="EW")
web_entry.focus()

# email/ user entry
e_user_entry = Entry(width=35)
e_user_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
e_user_entry.insert(0, "danielamedinna20@gmail.com")

# Password entry
pass_entry = Entry(width=21)
pass_entry.grid(row=3, column=1, sticky="EW")

# __________________________________________________________________________________________________________ #

# button generate password
generate_pass_button = Button(text="Generate Password", width=19, command=generate_password)
generate_pass_button.grid(row=3, column=2)

# search button
search_button = Button(text="Search", width=19, command=find_password)
search_button.grid(row=1, column=2)

# button add
add_button = Button(text="Add", width=36, command=save_pass)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")


window.mainloop()
