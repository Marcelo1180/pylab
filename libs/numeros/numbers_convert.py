from .number_to_text import Number2Text
from .roman_to_number import Roman2Number
from .text_to_number_es import Text2NumberES


class Numbers:
    @staticmethod
    def convert(_number):
        romano_number =  Roman2Number()
        number_text = Number2Text()
        text_number = Text2NumberES()
        result = []
        try:
            if str(_number).isdigit():
                # ----------- digito
                result.append(_number)
                try:
                    tmp = number_text.convert(int(_number))
                    result.append(tmp)
                except:
                    result.append('')
                try:
                    tmp1 = romano_number.decimal_to_roman(int(_number))
                    result.append(tmp1.lower())
                except:
                    result.append('')
                # ----------- digito
            else:
                # ----------- es numero
                tmp3 = text_number.convert(_number)
                numero_2 = tmp3[0]
                if str(numero_2).isdigit():
                    result.append(numero_2)
                    try:
                        result.append(number_text.convert(int(numero_2)))
                    except:
                        result.append('')
                    try:
                        result.append( romano_number.decimal_to_roman(int(numero_2)).lower())
                    except:
                        result.append('')
                # -----------
                else:
                    numero_3 = romano_number.convert(_number)
                    #print(numero_3)
                    if str(numero_3).isdigit():
                        result.append(numero_3)
                        try:
                            result.append(number_text.convert(int(numero_3)))
                        except:
                            result.append('')

                        try:
                            result.append( romano_number.decimal_to_roman(int(numero_3)).lower())
                        except:
                            result.append('')
                    else:
                        print('no es posible')
        except:
             return result


        return result
