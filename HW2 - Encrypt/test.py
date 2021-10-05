def num2Hex(num : int):
    if num < 10:
        return str(num)
    elif num == 10:
        return 'a'
    elif num == 11:
        return 'b'
    elif num == 12:
        return 'c'
    elif num == 13:
        return 'd'
    elif num == 14:
        return 'e'
    elif num == 15:
        return 'f'

def dec2Bin(dec : int):
    aBin = ''
    for i in range(8):
        aBin = num2Hex(dec % 2) + aBin
        dec = dec // 2
    return aBin   

def dec2Hex(dec : int):
    aHex = ''
    for i in range(4):
        aHex = num2Hex(dec % 16) + aHex
        dec = dec // 16
    return aHex

def text2Hex(text : str):
    hex = []
    for ch in text:
        ascii_dec = ord(ch)
        hex.append(dec2Hex(ascii_dec))
        
    return hex

def text2Bin(text : str):
    bin = ''
    for ch in text:
        ascii_dec = ord(ch)
        bin += dec2Bin(ascii_dec)
    return bin


def splitInHalf(data64b : str):
    return data64b[0:3], data64b[4:7]

def xor_HEX(dataA : list, dataB : list):
    lenA = len(dataA)
    lenB = len(dataB)
    if lenA != lenB:
        print("xor op : list is not the same length, dataA : {lenA}, dataB : {lenB}")
    res = []
    for i in range(lenA):
        numA = int(dataA[i], 16)
        numB = int(dataB[i], 16)
        resInt = numA ^ numB
        res.append(dec2Hex(resInt)  ) 
        
    return res  

def xor(dataA : str, dataB : str):
    lenA = len(dataA)
    lenB = len(dataB)
    if lenA != lenB:
        print("xor op : list is not the same length, dataA : {lenA}, dataB : {lenB}")
    res = ''
    for i in range(lenA):
        numA = dataA[i]
        numB = dataB[i]
        if numA == numB:
            res += '0'
        else:
            res += '1'
    return res  


if __name__ == "__main__":
    while(1):
        aStr = input()
        bStr = input()
        print(aStr[1:-1])
        aHex = text2Bin(aStr)
        bHex = text2Bin(bStr)
        print(text2Bin(aStr), text2Bin(bStr))
        print(xor(aHex, bHex))