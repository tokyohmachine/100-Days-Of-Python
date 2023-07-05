import requests
from bs4 import BeautifulSoup


response = requests.get(url='https://news.ycombinator.com/news')
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")


articles = soup.find_all(name="a", class_="titlelink")
article_texts = []
article_links = []

for article in articles:
    text = article.getText()
    article_texts.append(text)
    link = article.get("href")
    article_links.append(link)

article_upvote = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

largest_number = max(article_upvote)
n = article_upvote.index(largest_number)
print(n)

print(article_texts[n])
print(article_links[n])








#all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)
#
# for tag in all_anchor_tags:
#     print(tag.getText())
#     print(tag.get("href"))
#
#
# heading = soup.find(name="h1", id="name")
# print(heading)
#
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.get("class"))
#
# company_url = soup.select_one(selector="p a")
# print(company_url)
#
# name = soup.select_one("#name")
# print(name)












# from bs4 import BeautifulSoup
# #import lxml
# import codecs
#
# # with open("website.html") as file:
# #     contents = file.read()
# #
#
#
# file = codecs.open("website.html", "r", "utf-8")
# content = file.read()
#
# soup = BeautifulSoup(content, "html.parser")
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.prettify())
# print(soup.a)
# print(soup.p)
# print(soup.li)
#
# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)
#
# for tag in all_anchor_tags:
#     print(tag.getText())
#     print(tag.get("href"))
#
#
# heading = soup.find(name="h1", id="name")
# print(heading)
#
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.get("class"))
#
# company_url = soup.select_one(selector="p a")
# print(company_url)
#
# name = soup.select_one("#name")
# print(name)