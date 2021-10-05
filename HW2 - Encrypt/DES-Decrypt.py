
# info is one Block (64 bit)
# IP
def initPermutation(info: str):
    IPtable = [ 58, 50, 42, 34, 26, 18, 10, 2,
                60, 52, 44, 36, 28, 20, 12, 4,
                62, 54, 46, 38, 30, 22, 14, 6,
                64, 56, 48, 40, 32, 24, 16, 8,
                57, 49, 41, 33, 25, 17, 9,  1,
                59, 51, 43, 35, 27, 19, 11, 3,
                61, 53, 45, 37, 29, 21, 13, 5,
                63, 55, 47, 39, 31, 23, 15, 7 ]
    
    return permutation(info, IPtable)

def finalPermutation(info: str):
    FPtable = [ 40, 8, 48, 16, 56, 24, 64, 32,
                39, 7, 47, 15, 55, 23, 63, 31,
                38, 6, 46, 14, 54, 22, 62, 30,
                37, 5, 45, 13, 53, 21, 61, 29,
                36, 4, 44, 12, 52, 20, 60, 28,
                35, 3, 43, 11, 51, 19, 59, 27,
                34, 2, 42, 10, 50, 18, 58, 26,
                33, 1, 41,  9, 49, 17, 57, 25]
    return permutation(info, FPtable)

def permutation(info: str, table: list):
    data = ""
    for i in range(0, len(table)):
        data = data + info[table[i] - 1]
    return data

# S-Box
def S_Box(data: str):
    S_table = [
                [#S1
                    [14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],  
                    [0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],  
                    [4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0], 
                    [15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13] 
                ],
                [#S2
                    [15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10],  
                    [3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5], 
                    [0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15],  
                    [13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]  
                ], 
                [#S3
                    [10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8],  
                    [13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1],  
                    [13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7],  
                    [1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]  
                ], 
                [#S4
                    [7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15],  
                    [13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9],  
                    [10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4],  
                    [3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14]  
                ],
                [#S5  
                    [2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9],  
                    [14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6],  
                    [4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14],  
                    [11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3]  
                ],
                [#S6  
                    [12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11],  
                    [10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8],  
                    [9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6],  
                    [4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13]  
                ], 
                [#S7  
                    [4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1],  
                    [13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6],  
                    [1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2],  
                    [6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12]  
                ], 
                [#S8  
                    [13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7],  
                    [1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2],  
                    [7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8],  
                    [2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]  
                ] 
            ]
    finalBits = ""
    for i in range(0, 8):
        block = data[(i*6):(i*6+6)]
        index1 = int(block[0] + block[-1], 2)
        index2 = int(block[1:-1], 2)
        value = S_table[i][index1][index2]
        bits = bin(value)
        bits = bits[2:] #abandon 0B
        finalBits = finalBits + fillBit(bits, 4)

    return finalBits

# P-Box
# data is 32-bit
def P_Box(data: str):
    P_table = [ 16,  7, 20, 21,
                29, 12, 28, 17,
                 1, 15, 23, 26,
                 5, 18, 31, 10,
                 2,  8, 24, 14,
                32, 27,  3,  9,
                19, 13, 30,  6,
                22, 11,  4, 25]
    
    return permutation(data, P_table)

# E-Extend
# data is 32-bit, it will be 48 bit
def E_Extend(data: str):
    E_table = [32,  1,  2,  3,  4,  5,
                4,  5,  6,  7,  8,  9,
                8,  9, 10, 11, 12, 13,
               12, 13, 14, 15, 16, 17,
               16, 17, 18, 19, 20, 21,
               20, 21, 22, 23, 24, 25,
               24, 25, 26, 27, 28, 29,
               28, 29, 30, 31, 32,  1]
    
    return permutation(data, E_table)

def XOR(a: str, b: str): 
    num = max(len(a), len(b))
    # a = fillBit(a, num)
    # b = fillBit(b, num)
    bits = ""
    for i in range(0, num):
        if(a[i] == b[i]):
            bits = bits + "0"
        else:
            bits = bits + "1"
    
    return bits

# F-Function
# data is 32-bit, subkey is 48-bit
def Feistel(data: str, subkey: str):
    #data is 32-bit
    data = E_Extend(data) # 32-bit => 48-bit
    data = XOR(data, subkey) # 48-bit
    data = S_Box(data) # 48-bits => 32-bits
    data = P_Box(data) # 32-bit
    return data

def hexByte2bit(byte: str):
    value = int(byte, 16)
    bits = bin(value)
    bits = bits[2:] # abandon 0B
    while (len(bits) < 8):
        bits = "0" + bits
    return bits

def hex2bit(byte: str):
    i = 0
    bits = ""
    while(i < len(byte)):
        bits = bits + hexByte2bit(byte[i] + byte[i+1])
        i = i + 2
    return bits

def fillBit(bits: str, num: int):
    while(len(bits) < num):
        bits = "0" + bits
    return bits


def leftCircleShift(bits: str, num: int):
    for i in range(0, num):
        bits =  bits[1:] + bits[0]
    return bits

# return [subkey1, subkey2... subkey16]
# subkey is 48 bit
def getSubkeys(key: str):
    # 56 bit
            #Left
    PC_1 = [57, 49, 41, 33, 25, 17,  9,
             1, 58, 50, 42, 34, 26, 18,
            10,  2, 59, 51, 43, 35, 27,
            19, 11,  3, 60, 52, 44, 36,
            #Right
            63, 55, 47, 39, 31, 23, 15,
             7, 62, 54, 46, 38, 30, 22,
            14,  6, 61, 53, 45, 37, 29,
            21, 13,  5, 28, 20, 12,  4]
    
    # 48 bit
    PC_2 = [14, 17, 11, 24,  1,  5,
             3, 28, 15,  6, 21, 10,
            23, 19, 12,  4, 26,  8,
            16,  7, 27, 20, 13,  2,
            41, 52, 31, 37, 47, 55,
            30, 40, 51, 45, 33, 48,
            44, 49, 39, 56, 34, 53,
            46, 42, 50, 36, 29, 32]
    shiftBit = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

    key = permutation(key, PC_1)
    C = key[ 0:28] #0~27
    D = key[28:56] #28~55
    subkeys = []
    for i in range(0, 16):
        C = leftCircleShift(C, shiftBit[i])
        D = leftCircleShift(D, shiftBit[i])
        subkey = C + D

        subkeys.append(permutation(subkey, PC_2))

    return subkeys

# clip Info to Block, every Block size is 8 Byte
# ?? Byte -> [8 Byte, 8 Byte, 8 Byte....]
# if < 8 byte, fill 0 to be 8 Byte
# info is hex string
def clipBlock(info: str, blockSize: int = 8, fillByte = "00"):
    blocks = []
    i = 0
    blockSize = blockSize * 2 # becasue one char is 1/2 Byte
    while ((len(info) % blockSize) != 0):
        info = info + fillByte # add one byte

    while (i < len(info)):
        block = info[i:i+blockSize]
        blocks.append(block)
        i = i + blockSize

    return blocks

def bin2chr(bits :str):
    i = 0
    string = ""
    len(bits)
    while(i < len(bits)):
        byte = bits[i : (i+8)]
        # print("byte: " + byte)
        string = string + chr(int(byte, 2))
        i = i + 8
    return string        


# DES-Decrypt  
def DES_decrypt(key: str, info: str):
    key = hex2bit(key)
    subkeys = getSubkeys(key)
    subkeys.reverse()

    blocks = clipBlock(info)

    decryptData = ""
    for block in blocks:
        bits = hex2bit(block)
        #IP
        bits = initPermutation(bits)
        left ,right =  bits[0:32], bits[32:64]

        for i in range(0, len(subkeys)):  
            temp = Feistel(right, subkeys[i])
            left = XOR(left ,temp)
            left, right = right, left #swap()

        temp = right + left
        temp = finalPermutation(temp)
        decryptData = decryptData + bin2chr(temp)
    
    i = len(decryptData) - 1
    while(i >= 0 and decryptData[i] == ' '):
        decryptData = decryptData[:-1]
        i = i - 1
    return decryptData

if __name__ == "__main__":
    while True:
        try:
            key = input()
            info = input()
            print(DES_decrypt(key, info))
        except EOFError:
            break
        except:
            break
