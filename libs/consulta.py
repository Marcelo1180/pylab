#!/usr/bin/python
"""Este modulo genera consultas mediante operadores logicos."""

import sys
from .numeros.numbers_convert import Numbers


class BooleanSearch:
    """Es una clase estatica BooleanSearch."""

    wordList = open('biz.txt', 'r').read().split()
    _words = set(s.lower() for s in wordList)

    @staticmethod
    def _xrange(x, y):
        """Funcion Auxiliar _xrange.

        Parametros:
            :param x: inicio
            :param y: fin

        Respuesta:
            Retorna la iteracion en el rango x, y

        """
        return iter(range(x, y))

    @staticmethod
    def _splitString(s):
        """Funcion Auxiliar _splitString.

        Funcion que basado en un diccionario puede separar palabras

        Parametros:
            :param s: Palabra string

        Respuesta:
            Retorna la palabra en una lista descompuesta en subpalabras

        """
        found = []

        def rec(stringLeft, wordsSoFar):
            if not stringLeft:
                found.append(wordsSoFar)
            for pos in BooleanSearch._xrange(1, len(stringLeft)+1):
                if stringLeft[:pos] in BooleanSearch._words:
                    rec(stringLeft[pos:], wordsSoFar + [stringLeft[:pos]])
        rec(s.lower(), [])
        return found

    @staticmethod
    def _splitWords(w):
        """Funcion Auxiliar _splitWords.

        Funcion para recorrer las palabra de la cadena, haciendo sugerencias
        numericas y palabras descompuestas

        Parametros:
            :param w:

        Respuesta:
            Retorna la cadena descompuesta en una lista.

        """
        wres = []
        for words in w.split(' '):
            wdat = []
            # Convertir texto a numero o romano
            # si es correcto devolvera un array caso contrario [] falso
            wnumero = Numbers.convert(words)
            # Eliminando conectores numericos "y", y agrupando numero y AND
            if wnumero:
                wnumero[1] = '(%s)' % ' AND '.join(wnumero[1].
                                                   replace(' y ', ' ').
                                                   split(' '))
            # Comprobano si la palabra es numero,
            #  caso contrario enviar la palabra con fuzzy
            wdat += [['nombre:'+n] for n in wnumero] if wnumero else [[words +
                                                                       '~']]
            # Agregando Palabra Descompuesta en los elementos de splitString
            # si la palabra sugerida es numero se debe colocar nombre: para,
            # que sea exacto
            wdat += list(map(lambda x: ['nombre:'+a if a.isdigit()
                                        else a+'~' for a in x],
                             BooleanSearch._splitString(words)))
            wres.append(wdat)
        return wres

    @staticmethod
    def _combineWords(word):
        """Funcion Auxiliar _combineWords.

        Funcion para combinacion de palabras a b c, ab c, a bc, abc

        Parametros:
            :param word: String de palabras a combinar

        Respuesta:
            Devuelve una lista con las palabras combinadas

        """
        xwarr = word.split(' ')
        # Se extrae la lista de palabras que no contienen numeros
        warr = list(filter(lambda l: not l.isdigit(), xwarr))
        # Se extrae una lista de numeros
        warr_numbers = list(filter(lambda l: l.isdigit(), xwarr))
        wlen = len(warr)
        wres = []
        wres.append([wa for wa in xwarr])
        for i in range(2, wlen+1):
            for j in range(0, wlen+1-i):
                # Combinacion de elementos aero mundo => aereomundo
                cword = [''.join(warr[j:i+j])]
                wres.append(warr[:j]+cword+warr[i+j:]+warr_numbers)
        return wres

    @staticmethod
    def query(uinput=''):
        """Funcion Principal query.

        Funcion para la generacion de consultas con operadores logicos

        Parametros:
            :param uinput: Requiere la entrada de un texto para descomponerlo
                en atributos para busqueda con operadores logicos.

        Respuesta:
            Retorna la cadena descompuesta con operadores logicos.

        """
        cor = []
        for cword in BooleanSearch._combineWords(uinput):
            cand = []
            for sword in BooleanSearch._splitWords(' '.join(cword)):
                kor = []
                for kand in sword:
                    kor.append('(%s)' % ' AND '.join(kand))
                cand.append('(%s)' % ' OR '.join(kor))
            cand = list(filter(lambda item: item != '()', cand))
            cor.append('(%s)' % ' AND '.join(cand))
            cor = list(filter(lambda item: item != '()', cor))
        return ' OR '.join(cor)


if __name__ == '__main__':
    print(BooleanSearch.query(' '.join(sys.argv[1:])))
