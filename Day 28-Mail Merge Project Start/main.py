PLACEHOLDER = "[name]"

# todo: usar os nomes da pasta names para automatizar a troca de nomes em outra pasta:
with open("Input/Names/invited_names.txt") as file_names:
    names = file_names.readlines()
    print(names)


# todo: automate the names in Letters_birth
with open("Input/Letters/starting_letter.txt") as file_letters:
    contents_letter = file_letters.read()

    # replace
    for name in names:
        stripped_name = name.strip()
        new_letter = contents_letter.replace(PLACEHOLDER, stripped_name )
        print(new_letter)

        # write
        with open(f"./Output/ReadyToSend/letter_for{stripped_name }.txt", mode="w") as letter_completed:
            final_letter = letter_completed.write(new_letter)



