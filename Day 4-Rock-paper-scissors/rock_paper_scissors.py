import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___) 
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________) 
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
# store the user's input

while True:
    images_game = [rock, paper, scissors]
    user_choice = int(input("Enter your choice: Type 0 for rock, 1 for paper or 2 for scissors): \n"))
    print(f"User choice: ")
    print(images_game[user_choice])

    computer_choice = random.randint(0, 2)
    print(f"Computer chose: ")
    print(images_game[computer_choice])

    if user_choice == computer_choice:
        print("No one win this time!")
    elif user_choice == "0":
        if computer_choice == "2":
            print("You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_choice == "1":
        if computer_choice == "0":
            print("You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_choice == "2":
        if computer_choice == "1":0
            print("You win!")
        else:
            print("Rock smashes scissors! You lose.")

    play_again = input("Do you want to play again? Type 'y' or 'n': \n").lower()
    if play_again != "y":
        break
