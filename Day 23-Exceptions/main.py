file does not exist
try:
    f = open("data.txt", "r")
except:
    print("File does not exist")


try:
    s = open("data.txt", "r") # does not exist
except:
    s = open("data.txt", "w")  # create an file
    s.write("Something")

key error
you can use how many 'except' you want it
if the 'try' does not exist or fail, the 'expect' is going be executed
try:
    file = open("data.txt") # does not exist
    dictionary = {"key": "value"}
    print(dictionary["key"])
except FileNotFoundError:
    file = open("data.txt", "w")  # create an file
    file.write("Something")
except KeyError as error_message:
    print(f"the key {error_message} does not exist")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("file was closed")
    raise TypeError("This is an error that I made up.")


#BMI Example
# the 'raise' can be used when something might seem wrong, and you can especified the error.
height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human Height should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)



fruits = ["Apple", "Pear", "Orange"]

#TODO: Catch the exception and make sure the code runs without crashing.

make_pie(4)



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



