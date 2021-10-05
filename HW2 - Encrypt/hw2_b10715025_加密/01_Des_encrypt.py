def bin2Hex(bin : str):
    hex = ''
    for i in range((4 - (len(bin) % 4)) % 4):
        bin = '0' + bin
    for i in range(len(bin) // 4):
        dec = int(bin[i * 4 : (i + 1) * 4], 2)
        if dec < 10:
            hex += str(dec)
        elif dec == 10:
            hex +=  'a'
        elif dec == 11:
            hex +=  'b'
        elif dec == 12:
            hex +=  'c'
        elif dec == 13:
            hex +=  'd'
        elif dec == 14:
            hex +=  'e'
        elif dec == 15:
            hex +=  'f'
    return hex

def hex2Bin(hex : str):
    bin = ''
    for ch in hex:
        num = int(ch, 16)
        bin += dec2Bin(num, 4)
    return bin

def dec2Bin(dec : int, bit_count : int):
    aBin = ''
    for i in range(bit_count):
        aBin = str(dec % 2) + aBin
        dec = dec // 2
    return aBin   

def text2Bin(text : str):
    bin = ''
    for ch in text:
        ascii_dec = ord(ch)
        bin += dec2Bin(ascii_dec, 8)
    return bin


def splitInHalf(data64b : str):
    return data64b[0:32], data64b[32:64]

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

def shiftLeft(data : str, iter : int):
    newData = data[iter:]
    newData += data[0 : iter]
    return newData

def initialPermutation(data : str):
    ip = [ 58, 50, 42, 34, 26, 18, 10, 2,
           60, 52, 44, 36, 28, 20, 12, 4,
           62, 54, 46, 38, 30, 22, 14, 6,
           64, 56, 48, 40, 32, 24, 16, 8,
           57, 49, 41, 33, 25, 17,  9, 1,
           59, 51, 43, 35, 27, 19, 11, 3,
           61, 53, 45, 37, 29, 21, 13, 5,
           63, 55, 47, 39, 31, 23, 15, 7  ]
    return permutation(data, ip)

def fianlPermutation(data : str):
    fp = [ 40, 8, 48, 16, 56, 24, 64, 32,
           39, 7, 47, 15, 55, 23, 63, 31,
           38, 6, 46, 14, 54, 22, 62, 30,
           37, 5, 45, 13, 53, 21, 61, 29,
           36, 4, 44, 12, 52, 20, 60, 28,
           35, 3, 43, 11, 51, 19, 59, 27,
           34, 2, 42, 10, 50, 18, 58, 26,
           33, 1, 41,  9, 49, 17, 57, 25 ]
    return permutation(data, fp)

def expansion(data : str):
    ep = [ 32,  1,  2,  3,  4,  5,
            4,  5,  6,  7,  8,  9,
            8,  9, 10, 11, 12, 13,
           12, 13, 14, 15, 16, 17,
           16, 17, 18, 19, 20, 21,
           20, 21, 22, 23, 24, 25,
           24, 25, 26, 27, 28, 29,
           28, 29, 30, 31, 32,  1  ]
    return permutation(data, ep)

def permutation(data : str, table : list):
    newData = ''
    for index in table:
        newData += data[index - 1]
    return newData

def sBox(data48):
    s_box = [
                [#1
                    [14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],  
                    [0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],  
                    [4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0], 
                    [15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]
                ],
                [#2
                    [15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10],  
                    [3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5], 
                    [0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15],  
                    [13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]  
                ], 
                [#3
                    [10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8],  
                    [13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1],  
                    [13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7],  
                    [1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]  
                ], 
                [#4
                    [7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15],  
                    [13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9],  
                    [10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4],  
                    [3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14]  
                ],
                [#5  
                    [2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9],  
                    [14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6],  
                    [4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14],  
                    [11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3]  
                ],
                [#6  
                    [12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11],  
                    [10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8],  
                    [9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6],  
                    [4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13]  
                ], 
                [#7  
                    [4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1],  
                    [13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6],  
                    [1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2],  
                    [6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12]  
                ], 
                [#8  
                    [13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7],  
                    [1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2],  
                    [7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8],  
                    [2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]  
                ] 
            ]
    boxed = ''
    for i in range(8):
        data6 = data48[i * 6 : (i + 1) * 6]
        row_index = int(data6[0] + data6[-1], 2)
        col_index = int(data6[1:5], 2)
        value = s_box[i][row_index][col_index]
        boxed += dec2Bin(value, 4)
    return boxed

def p_shift(data32: str):
    pt = [ 16,  7, 20, 21,
           29, 12, 28, 17,
            1, 15, 23, 26,
            5, 18, 31, 10,
            2,  8, 24, 14,
           32, 27,  3,  9,
           19, 13, 30,  6,
           22, 11,  4, 25 ]
    
    return permutation(data32, pt)

def feistel(data32 : str, key48 : str):
    data48 = expansion(data32)
    # print('expand', len(data48), data48)
    xored = xor(data48, key48)
    # print('xor', len(xored), xored)
    boxed = sBox(xored)
    # print('sbox', len(boxed), boxed)
    ps = p_shift(boxed)
    # print('p-shift', len(ps), ps)
    return ps


def subkey(key64 : str):
    shift_num = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
    # 64 to 56 bit
    pc_1 = [ #L
             57, 49, 41, 33, 25, 17,  9,
              1, 58, 50, 42, 34, 26, 18,
             10,  2, 59, 51, 43, 35, 27,
             19, 11,  3, 60, 52, 44, 36,
             #R
             63, 55, 47, 39, 31, 23, 15,
              7, 62, 54, 46, 38, 30, 22,
             14,  6, 61, 53, 45, 37, 29,
             21, 13,  5, 28, 20, 12,  4 ]
    
    # 48 bit
    pc_2 = [ 14, 17, 11, 24,  1,  5,
              3, 28, 15,  6, 21, 10,
             23, 19, 12,  4, 26,  8,
             16,  7, 27, 20, 13,  2,
             41, 52, 31, 37, 47, 55,
             30, 40, 51, 45, 33, 48,
             44, 49, 39, 56, 34, 53,
             46, 42, 50, 36, 29, 32 ]

    pc1_key = permutation(key64, pc_1)
    c = pc1_key[0:28]
    d = pc1_key[28:56]
    pc2_keys = []
    for i in range(16):
        # print('subkey ', i)
        c = shiftLeft(c, shift_num[i])
        d = shiftLeft(d, shift_num[i])
        # print('L : ')
        # print(c)
        # print('R : ')
        # print(d)
        cd_key = c + d
        pc2_key = permutation(cd_key, pc_2)
        # print('PC2 : ')
        # print(pc2_key)
        pc2_keys.append(pc2_key)
    return pc2_keys

if __name__ == "__main__":

    while True:

        try:

            key = input()
            uncryed = input()
            
            data = []
            data.append('')
            index = 0
            for ch in uncryed:
                if index >= 8:
                    data.append('')
                    index = 0
                data[-1] += ch
                index += 1

            # Fill in blanks
            if len(data[-1]) != 8:
                for i in range(8 - len(data[-1])):
                    data[-1] += ' '

            # print(data)
            cryed = ''
            for uncryedStr in data:
                BinData = text2Bin(uncryedStr)
                sortedUncryedStr = initialPermutation(BinData)
                l_block, r_block = splitInHalf(sortedUncryedStr)
                keys = subkey(hex2Bin(key))
                for i in range(16):
                    pre_r_block = r_block
                    r_block = xor(l_block, feistel(pre_r_block, keys[i]))
                    l_block = pre_r_block
                whole_block = r_block + l_block
                cryed += fianlPermutation(whole_block)
            # print(len(cryed), cryed)
            print(bin2Hex(cryed))

        except EOFError:
            break