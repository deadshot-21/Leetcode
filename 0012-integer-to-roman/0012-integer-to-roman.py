class Solution:
    def intToRoman(self, num: int) -> str:
        roman_list = [["M",1000],["CM",900],["D",500], ["CD",400], ["C",100],
                ["XC",90], ["L",50], ["XL", 40], ["X",10], ["IX", 9], ["V", 5],
                ["IV",4], ["I",1]
            ]
        res=""
        for s, val in roman_list:
            if num // val:
                count = num // val
                res+= (s*count)
                num = num % val
        return res