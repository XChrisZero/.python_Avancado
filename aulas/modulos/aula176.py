# json.dumps e json.loads com strings + typing.TypedDict
# dumps(jogar para fora) = converte para string JSON
# loads(carregar pra dentro) = converte de string JSON para Python
# Ao converter de Python para JSON:
# Python        JSON
# dict          object
# list, tuple   array
# str           string
# int, float    number
# True          true
# False         false
# None          null
import json
# from pprint import pprint
from typing import TypedDict # para definir o tipo do dicionário


class Movie(TypedDict): # define o tipo do dicionário
    title: str
    original_title: str
    is_movie: bool
    imdb_rating: float
    year: int
    characters: list[str]
    budget: None | float


string_json = '''
{
  "title": "O Senhor dos Anéis: A Sociedade do Anel",
  "original_title": "The Lord of the Rings: The Fellowship of the Ring",
  "is_movie": true,
  "imdb_rating": 8.8,
  "year": 2001,
  "characters": ["Frodo", "Sam", "Gandalf", "Legolas", "Boromir"],
  "budget": null
}
'''
filme: Movie = json.loads(string_json) # filme é do tipo Movie que foi tipado em cima e herda de TypedDict
# pprint(filme, width=40)
# print(filme['title'])
# print(filme['characters'][0])
# print(filme['year'] + 10)

json_string = json.dumps(filme, ensure_ascii=False, indent=2) # indent=2 para formatar a saída
print(json_string)