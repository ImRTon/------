import cv2
import numpy as np

#share functions
#(高, 寬, bytes)
def readImage(path: str):
    im = cv2.imread(path)
    if(type(im) == type(None)):
        print("Can't open picture.")
        exit(1)
    imFlat = im.flatten()
    return (im.shape[0], im.shape[1], bytes(imFlat))

#(高, 寬, bytes)
def readGrayImage(path: str):
    im = cv2.imread(path)
    if(type(im) == type(None)):
        print("Can't open picture.")
        exit(1)
    im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    imFlat = im.flatten()
    return (im.shape[0], im.shape[1], bytes(imFlat))

#(高, 寬, bytes)
def writeJpge(info: (int, int, bytes), path: str):
    aImg = fillPixels2Img(info[2], info[1])
    cv2.imwrite(path, np.array(aImg))
    pass

def xor(byteA : bytes, byteB : bytes):
    newBytes = bytes(0)
    for aByteA, aByteB in zip(byteA, byteB):
        newBytes += bytes([aByteA ^ aByteB])
    return newBytes

def readKey(path: str, lens: int = 16) -> bytes:
    f = open(path, "rb")
    byte = f.read(lens)
    f.close()
    return bytes(byte)

# Return 16 bytes
def getImgVal(IV: bytes, count: int, imgInfo: (int, int, bytes)) -> bytes:
    ivInt = int.from_bytes(IV[-30:], byteorder='big')
    XIndex = (ivInt + count) % imgInfo[1]
    YIndex = count % imgInfo[0]
    value = imgInfo[2][YIndex * imgInfo[1] + XIndex]
    newBytes = IV[0:15]
    newBytes += bytes([value])
    # [y * imgInfo[1] (image_x) + x]
    return newBytes
    


def byteAddOne(byteKey : bytes):
    isDone = False
    lastIndex = len(byteKey) - 1
    newBytes = bytes(0)
    for i in range(lastIndex, -1, -1):
        if isDone :
            newBytes = bytes([byteKey[i]]) + newBytes
        else:
            if int(byteKey[i]) == 255:
                newBytes = bytes([0]) + newBytes
            else:
                newBytes = bytes([(int(byteKey[i]) + 1)]) + newBytes
                isDone = True
    return newBytes

# char to ASCII
def char2Ascii(char):
    return ord(char)

# ASCII to int, return None if it's not a number
def ascii2Int(ascii : int):
    if ascii >=  ord('0') and ascii <= ord('9'):
        return ascii - ord('0')
    else:
        return None

# Fill pixels into a picture<list>
def fillPixels2Img(pixels : bytes, width : int):
    print("A", type(pixels))
    if (len(pixels) % (width * 3)) is not 0:
        print("ERROR! Pixels count can't fit in the picture!")
    aNewImg = []
    col_index = 0
    index = 0
    aRow = []
    for k in range(len(pixels) // (width * 3)):
        for i in range(width):
            rgbPixel = []
            for j in range(3):
                rgbPixel.append(pixels[index])
                index += 1
            aRow.append(rgbPixel)
            rgbPixel = []
        aNewImg.append(aRow)
        aRow = []
    return aNewImg

# return [BlockNum][blockSize]
def clipBlocks(bys: bytes, blockSize: int = 16) -> list:
    blocks = []
    block = []
    count = 0
    for byte in bys:
        block.append(byte)
        count += 1
        if(count == blockSize):
            blocks.append(bytes(block[0:]))
            block = []
            count = 0
            pass

    if(len(block) != 0):
        blocks.append(bytes(block[0:]))
        print("warnning[clipBlocks]: last block is not full.")

    return blocks
