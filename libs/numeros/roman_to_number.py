# TODO: Verificar que el orden del numero Romano sea el correcto
# TODO: Probar con casos extranios
# NOTA test: El archivo de test contiene casos correctos se debe probar con casos diferentes

class Roman2Number(str):

    romanos = {1:"I", 4:"IV", 5:"V", 9: "IX", 10:"X", 40:"XL", 50:"L",
                90:"XC", 100:"C", 400:"CD", 500:"D", 900:"CM", 1000:"M"}

    def convert(self, roman):
        
        roman = self.check_valid(roman)
        keys = ['IV', 'IX', 'XL', 'XC', 'CD', 'CM', 'I', 'V', 'X', 'L', 'C', 'D', 'M']
        to_arabic = {'IV': '4', 'IX': '9', 'XL': '40', 'XC': '90', 'CD': '400', 'CM': '900', 'I': '1', 'V': '5', 'X': '10', 'L': '50', 'C': '100', 'D': '500', 'M': '1000'}

        for key in keys:
            if key in roman:
                roman = roman.replace(key, ' {}'.format(to_arabic.get(key)))
        self.arabic = sum(int(num) for num in roman.split())
        
        return str(self.arabic)

    def check_valid(self, roman):
        
        roman = roman.upper()
        invalid = ['IIII', 'VV', 'XXXX', 'LL', 'CCCC', 'DD', 'MMMM']
        if any(sub in roman for sub in invalid):
            return roman
        
        return roman
    

    def decimal_to_roman(self, decimal):
        result = ""
        for value, numeral in sorted(self.romanos.items(), reverse=True):
            while decimal >= value:
                result += numeral
                decimal -= value
        
        return result
        