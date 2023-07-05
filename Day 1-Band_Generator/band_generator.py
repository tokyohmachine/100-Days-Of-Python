#Band Generator

#1. will finish when is finished
def band_generator():
	print("Welcome to the Band Name Generator.")
	city_name = input("What's name of the city you grew up in?: ")
	pet_name = input("What's your pet's name?: ")
	concatenate = city_name + pet_name
	print("Your band name could be:", concatenate)


band_generator()