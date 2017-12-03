# https://stackoverflow.com/questions/2174093/detect-most-likely-words-from-text-without-spaces-combined-words
#!/usr/bin/python
import sys
from time import time as t
# import enchant

def fakeNumber(n):
    if n == "x":
        return ["diez~", "x","10"]
    elif n == "cien":
        return ["cien~", "xxx", "100"]
    elif n == "100":
        return ["cien~", "xxx", "100"]
    elif n == "doscientos":
        return ["doscientos~", "xlx", "200"]
    elif n == "200":
        return ["doscientos~", "xlx", "200"]
    else:
        return []


def xrange(x,y):
    return iter(range(x,y))

wordList = open('biz.txt','r').read().split()
words = set( s.lower() for s in wordList )
# eword = enchant.request_pwl_dict("biz.txt")

def splitString(s):
    found = []
    def rec(stringLeft, wordsSoFar):
        if not stringLeft:
            found.append(wordsSoFar)
        for pos in xrange(1, len(stringLeft)+1):
            if stringLeft[:pos] in words:
                rec(stringLeft[pos:], wordsSoFar + [stringLeft[:pos]])

    rec(s.lower(), [])
    return found

def splitWords(w):
    # return [splitString(ws) for ws in w.split(" ")
    wres = []
    for ws in w.split(" "):
        wdat = []
        # Comprobano si la palabra es numero, caso contrario enviar la palabra con fuzzy
        wnumero = fakeNumber(ws)
        wdat += [[n] for n in wnumero] if len(wnumero) > 0 else [[ws+"~"]]
        # wdat += [[ws+"~"]]

        # Agregando Palabra Descompuesta en los elementos de splitString
        wdat += list(map(lambda x: [a+"~" for a in x], splitString(ws)))
        
        # Agregando Palabra Similar
        # wdat += [[e] for e in eword.suggest(ws)]
        # Agregando Algoritmo de numeros

        # print("-->",ws)
        # print("-->",wdat)
        # print(eword.suggest(ws))
        # wres.append([[ws]]+splitString(ws))

        wres.append(wdat)

        # print("-->",[["produxion"]]+splitString(ws))
    return wres

def combineWords(w):
    # wset = set(w.split(" "))
    # return [ws for ws in w.split(" ")]
    # return [warr[ws:1] for ws in range(4)]
    warr = w.split(" ")
    wlen = len(warr)
    # print(warr)
    wres = []
    wres.append(warr)
    for i in range(2,wlen+1):
        for j in range(0,wlen+1-i):
            # TODO: aeromundo y mundoaereo si se puede
            wres.append(warr[:j]+["".join(warr[j:i+j])]+warr[i+j:])
    return wres


def correctionWords(l):
    for e in l:
        print(eword.suggest(e))

    # print(wset[1])
    # for i in range(0,wlen+1):
    #     print(i,i+2)
    #     # print(["".join(warr[0:i])]+warr[i:])
    #
    # return ["".join(warr[0:2])]+warr[2:]

# print(splitString('fastfoodlacomidarapidadelaregion'))
# print(splitWords('comida rapida region'))
if __name__ == "__main__":
    # for t in splitWords(" ".join(sys.argv[1:])):
    #     kor = []
    #     for kand in t:
    #         kor.append("(%s)" % " AND ".join(kand))
    #     print(" OR ".join(kor))
    uinput = " ".join(sys.argv[1:])
    # print(combineWords(uinput))
    cor = []
    for c in combineWords(uinput):
        # print(c)
        # correctionWords(c)
        cand = []
        for t in splitWords(" ".join(c)):
            # print("|¬",t)
            kor = []
            for kand in t:
                kor.append("(%s)" % " AND ".join(kand))
            cand.append("(%s)" % " OR ".join(kor))
        cand = list(filter(lambda l: l != "()",cand))
        # print(" AND ".join(cand))
        cor.append("(%s)" % " AND ".join(cand))
        cor = list(filter(lambda l: l != "()",cor))
    print(" OR ".join(cor))

    # print(splitWords(" ".join(sys.argv[1:])))
