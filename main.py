# Top 100 Greatest Movies of All Time (The Ultimate List) - Web Scraping project using Beautiful Soup
# author : Pinak Mehta

import requests
from bs4 import BeautifulSoup


# make a get request if https://www.imdb.com/list/ls055592025/
response = requests.get(
    'https://www.imdb.com/list/ls055592025/')

soup = BeautifulSoup(response.text, 'html.parser')

movie_number = soup.find_all(
    name='span', class_="lister-item-index unbold text-primary")

movie_name = soup.find_all(name='h3', class_="lister-item-header")

# create a list of movies numbers
movie_number_list = [(movie_number[i].getText())
                     for i in range(len(movie_number))]

# create a list of movies names
movie_name_list = [(movie_name[i].a.getText()) for i in range(len(movie_name))]

# print(movie_number_list)
# print(movie_name_list)

# function to print .txt file


def list_100_movies():
    with open("Top 100 Greatest Movies of All Time.txt", 'w') as f:

        for i in range(len(movie_number)):
            f.write(f'{movie_number_list[i]}) {movie_name_list[i]}\n')


# call the funcrion
list_100_movies()
