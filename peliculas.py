# %matplotlib inline
from __future__ import print_function

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



pd.set_option('display.height', 1000)
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


EMPRESAS = [
    "Sociedad Boliviana cemento soboce",
    "Sociedad Alemana",
    "Sociedad Cemento",
    "Cemento Alemana",
    "Alemana sociedad miembro jose miembro",
    "Agencia de gobierno electronico agetic",
    "alojamiento jose pinto",
    "empresa mochila nueva",
    "jose pinto del siglo XXI",
    "mi la piz S.R.L",
    "refresco nube del cielo",
    "cielo elegante nube refresco",
    "farmacias veinti ocho",
    "jose siglo ocho lapiz",
    "gobierno nuve del cielo",
    "cavesa kabeza cabeza qabeza zillon cillon sillon siyon cavesakea cabesaqea callon kallon qallon"
]


if __name__ == '__main__':
    peliculas = pd.read_csv('data/peliculas.csv')
    type(peliculas)
    # resumen
    print(peliculas.head())
    # dimensiones
    print(peliculas.shape)
    # columnas
    print(peliculas.columns)
    # cantidad de filas
    print(peliculas.index)
    # mostrar columnda tipo select
    # print(peliculas["movie_title"])
    # mostrar columnda tipo select
    # print(peliculas.loc[:,"movie_title"])
    # mostrar una fila especifica con todos sus atributos
    # print(peliculas.loc[10,:])
    numcols = ['title_year', 'aspect_ratio', 'duration', 'duration.1', 'cast_total_facebook_likes', 'budget', 'imdb_score', 'gross']
    # filtrar por columnas
    peliculas_num = peliculas[numcols]
    # print(peliculas[numcols])
    # filtrar por columnas y mostrar una fila
    # print(peliculas.loc[10, numcols])
    # saca la media, desviacion estandar, min, max de las columnas dadas
    # print(peliculas_num.describe())
    HIST = peliculas_num['duration'].plot
    HIST.hist()
