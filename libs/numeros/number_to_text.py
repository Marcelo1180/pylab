#!/usr/bin/python
# -*- coding: utf-8 -*-

# NOTA: Requiere la instalacion de unidecode y num2words via pip install

from unidecode import unidecode
from num2words import num2words

class Number2Text():

    def convert(self, _number):
        result = unidecode(num2words(_number, lang='es'))
        return str(result.encode("ascii"))[2:-1]