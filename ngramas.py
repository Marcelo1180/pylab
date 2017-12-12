from __future__ import print_function

import sys
import numpy as np
import pandas as pd


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
    pd_empresas = pd.DataFrame({'nombre': EMPRESAS })
    print(pd_empresas)
