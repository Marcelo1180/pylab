#!/usr/bin/python
import sys
from .numeros.numbers_convert import Numbers


class BooleanSearch:
    wordList = open('biz.txt','r').read().split()
    _words = set(s.lower() for s in wordList)

    def _xrange(x,y):
        return iter(range(x,y))

    # Funcion que basado en un diccionario puede separar palabras
    def _splitString(s):
        found = []
        def rec(stringLeft, wordsSoFar):
            if not stringLeft:
                found.append(wordsSoFar)
            for pos in BooleanSearch._xrange(1, len(stringLeft)+1):
                if stringLeft[:pos] in BooleanSearch._words:
                    rec(stringLeft[pos:], wordsSoFar + [stringLeft[:pos]])
        rec(s.lower(), [])
        return found

    # Funcion para recorrer las palabra de la cadena, haciendo sugerencias
    # numericas y palabras descompuestas
    def _splitWords(w):
        wres = []
        for ws in w.split(" "):
            wdat = []
            # Convertir texto a numero o romano
            # si es correcto devolvera un array caso contrario [] falso
            wnumero = Numbers.convert(ws)
            # Eliminando conectores numericos "y", y agrupando numero y AND
            if wnumero:
                wnumero[1] = "(%s)" % " AND ".join(wnumero[1].\
                 replace(" y ", " ").split(" "))
            # Comprobano si la palabra es numero,
            #  caso contrario enviar la palabra con fuzzy
            wdat += [["nombre:"+n] for n in wnumero] if wnumero\
             else [[ws+"~"]]
            # Agregando Palabra Descompuesta en los elementos de splitString
            # si la palabra sugerida es numero se debe colocar nombre: para,
            # que sea exacto
            wdat += list(map(lambda x: ["nombre:"+a if a.isdigit() else a+"~" for a in x],\
             BooleanSearch._splitString(ws)))
            wres.append(wdat)
        return wres

    # Funcion para combinacion de palabras a b c, ab c, a bc, abc
    def _combineWords(w):
        xwarr = w.split(" ")
        # Se extrae la lista de palabras que no contienen numeros
        warr = list(filter(lambda l: not l.isdigit(),xwarr))
        # Se extrae una lista de numeros
        warr_numbers = list(filter(lambda l: l.isdigit(),xwarr))
        wlen = len(warr)
        wres = []
        wres.append([wa for wa in xwarr])
        for i in range(2,wlen+1):
            for j in range(0,wlen+1-i):
                # Comibinacion de elementos aero mundo => aereomundo
                cword = ["".join(warr[j:i+j])]
                wres.append(warr[:j]+cword+warr[i+j:]+warr_numbers)
        return wres

    # Funcion principal para la generacion de consultas
    @staticmethod
    def query(uinput=""):
        cor = []
        for c in BooleanSearch._combineWords(uinput):
            cand = []
            for t in BooleanSearch._splitWords(" ".join(c)):
                kor = []
                for kand in t:
                    kor.append("(%s)" % " AND ".join(kand))
                cand.append("(%s)" % " OR ".join(kor))
            cand = list(filter(lambda l: l != "()",cand))
            cor.append("(%s)" % " AND ".join(cand))
            cor = list(filter(lambda l: l != "()",cor))
        return " OR ".join(cor)

if __name__ == "__main__":
    print(BooleanSearch.query(" ".join(sys.argv[1:])))
