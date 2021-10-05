
from abc import abstractproperty


def char2num(char: str):
    ch = char.upper()
    return int(ord(ch) - ord('A'))

def num2char(num: int):
    ch = chr(num + ord('A'))
    return ch

def buildList(y: int, x: int, fill = 0):
    arr = []
    for i in range(0, y):
        temp = []
        for j in range(0, x):
            temp.append(fill)
        arr.append(temp)
    return arr


# pre do j => i
def makePlayfairTable(dealKey: str):
    table = buildList(5, 5, -1) # 5 x 5 table
    tableIndexY = 0
    tableIndexX = 0

    used = list()
    for i in range(0, 26):
        used.append(False)
    
    used[char2num("J")] = True
    for ch in dealKey:
        if (used[char2num(ch)] == True):
            continue
        used[char2num(ch)] = True
        table[tableIndexY][tableIndexX] = char2num(ch)
        tableIndexX = tableIndexX + 1
        if (tableIndexX >= 5):
            tableIndexX = 0
            tableIndexY = tableIndexY + 1

    for num in range(0, 26):
        if (used[num] == True):
            continue
        used[num] = True
        table[tableIndexY][tableIndexX] = num
        tableIndexX = tableIndexX + 1
        if (tableIndexX >= 5):
            tableIndexX = 0
            tableIndexY = tableIndexY + 1

    return table

def findIndex(table, ch):
    for y in range(0, 5):
        for x in range(0, 5):
            if (table[y][x] == char2num(ch)):
                return (y, x)
    return (-1, -1)

#unit has been deal
def encryptUnit(table, unit: str):
    encryptInfo = ""
    y1, x1 = findIndex(table, unit[0])
    y2, x2 = findIndex(table, unit[1])
    if(y1 == y2 and x1 == x2):
        raise "duplicate word!!"

    if (y1 == y2):
        #in same row ==> find right   
        encryptInfo = encryptInfo + num2char(table[y1][(x1 + 1) % 5])
        encryptInfo = encryptInfo + num2char(table[y2][(x2 + 1) % 5])
    elif (x1 == x2):
        #in same col ==> find down
        encryptInfo = encryptInfo + num2char(table[(y1 + 1) % 5][x1])
        encryptInfo = encryptInfo + num2char(table[(y2 + 1) % 5][x2])
    else:
        encryptInfo = encryptInfo + num2char(table[y1][x2])
        encryptInfo = encryptInfo + num2char(table[y2][x1])

    return encryptInfo

# Playfair cipher
# j => i (i replace j)
# mult ll => lx lx (fill x)
# single a => az (fill z)
def encrypt(key: str, info: str):
    encryptInfo = ""
    key = key.replace("j", "i")
    info = info.replace("j", "i")
    table = makePlayfairTable(key)
    i = 0

    while (i < len(info)): 
        if (i + 1 < len(info)):
            if (info[i] == info[i + 1]):
                # insert X
                info = info[:(i+1)] + "X" + info[(i+1):]
        i = i + 1

    if (len(info) % 2 == 1):
        info = info + "Z"
    
    for i in range(0, len(info), 2):
        unit = info[i] + info[i + 1]
        encryptInfo = encryptInfo + encryptUnit(table, unit)

    return encryptInfo
        

if __name__ == "__main__":

    while True:
        try:
            key = input()
            info = input()
            print(encrypt(key, info))
        except EOFError:
            break
        except:
            break


