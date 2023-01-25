import requests
from bs4 import BeautifulSoup

response = requests.get(
    'https://www.imdb.com/list/ls055592025/')

soup = BeautifulSoup(response.text, 'html.parser')

movie_number = soup.find_all(
    name='span', class_="lister-item-index unbold text-primary")

movie_name = soup.find_all(name='h3', class_="lister-item-header")

movie_number_list = [(movie_number[i].getText())
                     for i in range(len(movie_number))]
movie_name_list = [(movie_name[i].a.getText()) for i in range(len(movie_name))]

# print(movie_number_list)
# print(movie_name_list)


def list_100_movies():
    with open("Top 100 Greatest Movies of All Time.txt", 'w') as f:

        for i in range(len(movie_number)):
            f.write(f'{movie_number_list[i]}) {movie_name_list[i]}\n')


list_100_movies()
