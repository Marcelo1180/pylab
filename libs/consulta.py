#!/usr/bin/python
import sys
from libs.numeros.numbers_convert import Numbers


class BooleanSearch:
    wordList = open('biz.txt','r').read().split()
    _words = set(s.lower() for s in wordList)

    def _xrange(x,y):
        return iter(range(x,y))

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

    def _splitWords(w):
        wres = []
        for ws in w.split(" "):
            wdat = []
            # Comprobano si la palabra es numero,
            #  caso contrario enviar la palabra con fuzzy
            wnumero = Numbers.convert(ws)
            # wdat += [[n] for n in wnumero] if len(wnumero) > 0 else [[ws+"~"]]
            wdat += [[n] for n in wnumero] if len(wnumero) > 0\
             else [[ws[:-1] if "_" in ws else ws]]
            # Agregando Palabra Descompuesta en los elementos de splitString
            wdat += list(map(lambda x: [a+"~" for a in x],\
             BooleanSearch._splitString(ws)))
            wres.append(wdat)
        return wres

    def _combineWords(w):
        warr = w.split(" ")
        wlen = len(warr)
        wres = []
        wres.append([wa for wa in warr])
        print(warr)
        for i in range(2,wlen+1):
            for j in range(0,wlen+1-i):
                # TODO: aeromundo y mundoaereo si se puede
                wunion = warr[j:i+j]
                print(wunion)
                # Buscando los elementos menores depues de la palabra mas grande
                # por que en el fuzzy match se raya tiene que ser mayo a 2 siempre
                cwif = len("".join(sorted(wunion, key=len, reverse=True)[1:]))
                # print(cwif)
                # print("".join(list(filter(lambda l: len(l) <= 2,warr[j:i+j]))))
                # print(cwif)
                #
                cword = "".join(warr[j:i+j])
                # print(warr[j:i+j].sort(key = lambda s: len(s)))
                wres.append(warr[:j]+[cword+"_" if cwif > 2 else cword]+warr[i+j:])
        return wres


    def correctionWords(l):
        for e in l:
            print(eword.suggest(e))

    @staticmethod
    def query(uinput=""):
        cor = []
        for c in BooleanSearch._combineWords(uinput):
            cand = []
            print("=>",c)
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
