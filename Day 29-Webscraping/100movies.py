import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
website_html = response.text

# Write your code below this line 👇

soup = BeautifulSoup(website_html, "html.parser")
all_movies = soup.find_all(name="h3", class_="title")

movies_titles = [movie.getText() for movie in all_movies]
movies = movies_titles[::-1] #reverse list

# for n in range(len(movies_titles) -1, -1, -1):
#     print(movies_titles[n])

with open("movies.txt", mode="w") as file:
    for movie in movies:
        print(file.write(f"{movie}\n"))
