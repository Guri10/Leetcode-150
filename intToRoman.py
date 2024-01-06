def intToRoman(num):
    """
    :type num: int
    :rtype: str
    """
    # dic = {'M':1000,'CM':900,'D':500,'CD':400,
    #        'C':100,'XC':90,'L':50,'XL':40,'X':10,
    #        'IX':9,'V':5,'IV':4,'I':1
    #         }

    dic = [['M',1000],['CM',900],['D',500],['CD',400],
            ['C',100],['XC',90],['L',50],['XL',40],['X',10],
            ['IX',9],['V',5],['IV',4],['I',1]
            ]

    res = ""
    for key, item in dic:
        # print(item)
        # if num//item:
        c = num//item
        res += (key * c)
        num = num % item
    return res

# test cases:
print(intToRoman(3))
print(intToRoman(4))
print(intToRoman(7))