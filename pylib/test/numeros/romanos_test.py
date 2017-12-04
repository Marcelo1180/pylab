import unittest
from libs.numeros.roman_to_number import Roman2Number


class TestRomanos(unittest.TestCase):

    romans = [
        'i',
        'ii',
        'iii',
        'iv',
        'v',
        'vi',
        'vii',
        'viii',
        'ix',
        'x',
        'xi',
        'xii',
        'xiii',
        'xiv',
        'xv',
        'xvi',
        'xvii',
        'xviii',
        'xix',
        'xx',
        'xxi',
        'xxii',
        'xxiii',
        'xxiv',
        'xxv',
        'xxvi',
        'xxvii',
        'xxviii',
        'xxix',
        'l',
        'li',
        'lii',
        'liii',
        'liv',
        'lv',
        'lvi',
        'lvii',
        'lviii',
        'lix',
        'lx',
        'c'
    ]

    salidas = [
        '11',
        '2',
        '3',
        '4',
        '5',
        '6',
        '7',
        '8',
        '9',
        '10',
        '11',
        '12',
        '13',
        '14',
        '15',
        '16',
        '17',
        '18',
        '19',
        '20',
        '21',
        '22',
        '23',
        '24',
        '25',
        '26',
        '27',
        '28',
        '29',
        '50',
        '51',
        '52',
        '53',
        '54',
        '55',
        '56',
        '57',
        '58',
        '59',
        '60',
        '100'
    ]


def test_romano_numero(self):
    obj = Roman2Number()
    for item, roman in enumerate(self.romans):
        resultado = obj.convert(roman)
        self.assertEqual(resultado, self.salidas[item])
    print('Finalizo...')


if __name__ == '__main__':
    unittest.main()
