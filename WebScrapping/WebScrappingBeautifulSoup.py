#beautiful soup is the class in the library bs4 for html and xml parsing
from bs4 import BeautifulSoup
# import lxml (you can use it when you need it)

with open("website.html", mode = "r") as my_personal_webstie:
    contents = my_personal_webstie.read()
    # print(contents)

soup = BeautifulSoup(contents, "html.parser")
# print(soup.prettify())
# print(soup.p)

all_anchor_tags = soup.find_all(name = "a")
# print(all_anchor_tags)

# for tag in all_anchor_tags:
#     print(tag.getText())

heading = soup.find(name = "h1", id = "name")
# print(heading)

section_heading = soup.find(name = "h3", class_ = "heading")
# print(section_heading)


                                #Scrapping a live website
from bs4 import BeautifulSoup
from requests import *

response = get(url = "https://news.ycombinator.com/news")
y_combinator_website = response.text

soup = BeautifulSoup(y_combinator_website, "html.parser")
print(soup.find(name = "a", href = "newcomments"))