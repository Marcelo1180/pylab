from __future__ import print_function

class Text2NumberES():

    spanish_numbers = {
        'cero': 0,
        'uno': 1,
        'dos': 2,
        'tres': 3,
        'cuatro': 4,
        'cinco': 5,
        'seis': 6,
        'siete': 7,
        'ocho': 8,
        'nueve': 9,
        'diez': 10,
        'once': 11,
        'doce': 12,
        'trece': 13,
        'catorce': 14,
        'quince': 15,
        'dieciseis': 16,
        'diecisiete': 17,
        'dieciocho': 18,
        'diecinueve': 19,
        'veinte': 20,
        'veintiuno':21,
        'veintidos':22,
        'veintitres':23,
        'veinticuatro':24,
        'veinticinco':25,
        'veintiseis':26,
        'veintisiete':27,
        'veintiocho':28,
        'veintinueve':29,
        'treinta': 30,
        'cuarenta': 40,
        'cincuenta': 50,
        'sesenta': 60,
        'setenta': 70,
        'ochenta': 80,
        'noventa': 90,
        'cien': 100,
        'ciento': 100,
        'doscientos':200,
        'trescientos':300,
        'cuatrocientos':400,
        'quinientos':500,
        'seiscientos':600,
        'setecientos':700,
        'ochocientos':800,
        'novecientos': 900,
        'mil': 1000,
        'millon': 1000000,
        'mil millones': 1000000000
    }

    
    decimal_words = ['cero', 'uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve']


    """
    function to form numeric multipliers for million, billion, thousand etc.
    input: list of strings
    return value: integer
    """

    def number_formation(self, number_words):
        numbers = []
        for number_word in number_words:
            numbers.append(self.spanish_numbers[number_word])
        if len(numbers) == 4:
            return (numbers[0] * numbers[1]) + numbers[2] + numbers[3]
        elif len(numbers) == 3:
            return numbers[0] * numbers[1] + numbers[2]
        elif len(numbers) == 2:
            if 100 in numbers:
                return numbers[0] * numbers[1]
            else:
                return numbers[0] + numbers[1]
        else:
            return numbers[0]


    """
    function to convert post decimal digit words to numerial digits
    input: list of strings
    output: double
    """

    def get_decimal_sum(self, decimal_digit_words):
        decimal_number_str = []
        for dec_word in decimal_digit_words:
            if(dec_word not in self.decimal_words):
                return 0
            else:
                decimal_number_str.append(self.spanish_numbers[dec_word])
        final_decimal_string = '0.' + ''.join(map(str,decimal_number_str))
        return float(final_decimal_string)


    """
    function to return integer for an input `number_sentence` string
    input: string
    output: int or double or None
    """

    def word_to_num(self, number_sentence):

        if type(number_sentence) is not str:
            return number_sentence

        number_sentence = number_sentence.replace('-', ' ')
        number_sentence = number_sentence.lower()  # converting input to lowercase

        if(number_sentence.isdigit()):  # return the number if user enters a number string
            return int(number_sentence)

        split_words = number_sentence.strip().split()  # strip extra spaces and split sentence into words

        clean_numbers = []
        clean_decimal_numbers = []

        # removing and, & etc.
        for word in split_words:
            if word in self.spanish_numbers:
                clean_numbers.append(word)

        # Error message if the user enters invalid input!
        if len(clean_numbers) == 0:
            return ''

        # Error if user enters million,billion, thousand or decimal point twice
        if clean_numbers.count('mil') > 1 or clean_numbers.count('million') > 1 or clean_numbers.count('billion') > 1 or clean_numbers.count('point')> 1:
            return number_sentence


        billion_index = clean_numbers.index('mil millones') if 'mil millones' in clean_numbers else -1
        million_index = clean_numbers.index('millon') if 'millon' in clean_numbers else -1
        thousand_index = clean_numbers.index('mil') if 'mil' in clean_numbers else -1

        if (thousand_index > -1 and (thousand_index < million_index or thousand_index < billion_index)) or (million_index>-1 and million_index < billion_index):
            return number_sentence

        total_sum = 0  # storing the number to be returned

        if len(clean_numbers) > 0:
            # hack for now, better way TODO
            if len(clean_numbers) == 1:
                    total_sum += self.spanish_numbers[clean_numbers[0]]

            else:
                if billion_index > -1:
                    billion_multiplier = self.number_formation(clean_numbers[0:billion_index])
                    total_sum += billion_multiplier * 1000000000

                if million_index > -1:
                    if billion_index > -1:
                        million_multiplier = self.number_formation(clean_numbers[billion_index+1:million_index])
                    else:
                        million_multiplier = self.number_formation(clean_numbers[0:million_index])
                    total_sum += million_multiplier * 1000000

                if thousand_index > -1:
                    if million_index > -1:
                        thousand_multiplier = self.number_formation(clean_numbers[million_index+1:thousand_index])
                    elif billion_index > -1 and million_index == -1:
                        thousand_multiplier = self.number_formation(clean_numbers[billion_index+1:thousand_index])
                    else:
                        thousand_multiplier = self.number_formation(clean_numbers[0:thousand_index])
                    total_sum += thousand_multiplier * 1000

                if thousand_index > -1 and thousand_index != len(clean_numbers)-1:
                    hundreds = self.number_formation(clean_numbers[thousand_index+1:])
                elif million_index > -1 and million_index != len(clean_numbers)-1:
                    hundreds = self.number_formation(clean_numbers[million_index+1:])
                elif billion_index > -1 and billion_index != len(clean_numbers)-1:
                    hundreds = self.number_formation(clean_numbers[billion_index+1:])
                elif thousand_index == -1 and million_index == -1 and billion_index == -1:
                    hundreds = self.number_formation(clean_numbers)
                else:
                    hundreds = 0
                total_sum += hundreds

        # adding decimal part to total_sum (if exists)
        if len(clean_decimal_numbers) > 0:
            decimal_sum = self.get_decimal_sum(clean_decimal_numbers)
            total_sum += decimal_sum

        return total_sum
    
    # Metodo Principal
    def convert(self, number_sentence):
        array = number_sentence.split(' ')
        return [str(self.word_to_num(item)) for item in array]
            

    