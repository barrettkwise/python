class Solution():
    
    def __init__ (self):
        pass
    
    def intToRoman(self, num):
        
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
        
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
        
        roman_num = ''
        i = 0
        while num > 0:
            for _ in range(num // val[i]):
                roman_num += syb[i]
                num -= val[i]
            i += 1
        return roman_num
        
    def romanToInt(self, roman):
        sum = 0
        ##basic symbols
        symbols = { "I" : 1, 
                    "V" : 5,
                    "X" : 10,
                    "L" : 50,
                    "C" : 100,
                    "D" : 500,
                    "M" : 1000 }
    
        ##exceptions
        if "IV" in roman:
            res = res - 2
        
        if "IX" in roman:
            res = res - 2
        
        if "XL" in roman:
            res = res - 20
        
        if "XC" in roman:
            res = res - 20
    
        if "CD" in roman:
            res = res - 200
        
        if "CM" in roman:
            res = res - 200
        
        for char in roman:
            res = res + symbols.get(char)
    
        return res
