import shareFunction
from Crypto.Cipher import AES
import Crypto.Random
import argparse

# decrypt functions
def decrypt(key:bytes, info: (int, int, bytes), mode = "ECB"):
    width = info[1]
    height = info[0]
    picture_data = info[2]
    # print("Pic : ", picture_data)
    print(picture_data[-1], picture_data[-2])
    
    # Get 2 X coordinate
    stage = 0
    # stage 0 : 等待最後的<\n> / 1 : 開始讀第一組 Ascii / 2 : 開始讀第二組 Ascii / 3 : 結束
    x_real_data = 0
    num_bits = 0
    x_cryed_data = 0
    byteLen = len(picture_data)
    for i in range(byteLen-1, -1, -1):
        if stage == 0:
            # Get last <\n>
            if picture_data[i] == shareFunction.char2Ascii('\n'):
                stage = 1
        elif stage == 1:
            # Get crypted data position
            if picture_data[i] == shareFunction.char2Ascii('\n'):
                stage = 2
                num_bits = 0
            else:
                deAsciiNum = shareFunction.ascii2Int(picture_data[i])
                x_cryed_data += deAsciiNum * (10**num_bits)
                num_bits += 1
        elif stage == 2:
            # Get real data position
            if picture_data[i] == shareFunction.char2Ascii('\n'):
                stage = 3
                # end the loop here
                break
            else:
                deAsciiNum = shareFunction.ascii2Int(picture_data[i])
                x_real_data += deAsciiNum * (10**num_bits)
                num_bits += 1
        elif i == 0:
            print("Something going wrong, this picture might not be a crypted picture!")
    print("X_pos : ", x_real_data, x_cryed_data)
    encryed = picture_data[0 : x_cryed_data]
    print("Len :", len(encryed))
    byteIterTime = len(encryed) // 16
    print("Iter :", byteIterTime)
    cipher = AES.new(key, AES.MODE_ECB)
    decryed = bytes(0)

    if mode == "ECB":
        for i in range(byteIterTime):
            decryed += cipher.decrypt(encryed[i * 16:(i + 1) * 16])
    elif mode == "CTR":
        initialVec = shareFunction.readKey('./iv.bin')
        for i in range(byteIterTime):
            # print("Round :", i)
            initialVec = shareFunction.byteAddOne(initialVec)
            decryed += cipher.encrypt(initialVec)
        decryed = shareFunction.xor(decryed, encryed)
    elif mode == "Custom":
        initialVec = shareFunction.readKey('./iv.bin')
        img = shareFunction.readGrayImage("./middle_finger.png")
        count = 0
        for i in range(byteIterTime):
            # print("Round :", i)
            count += 1
            newIV = shareFunction.getImgVal(initialVec, count, img)
            decryed += cipher.encrypt(newIV)
        decryed = shareFunction.xor(decryed, encryed)
    real_data = decryed[0 : x_real_data]

    # fill in the pixels
    decry_pic = shareFunction.fillPixels2Img(real_data, width)
    # cv2.imshow('decrpt img',np.array(decry_pic))
    return (height, width, real_data)


if __name__ == "__main__":
    
    # parser
    parser = argparse.ArgumentParser()
    parser.add_argument("-di", 
                        '--decInput',
                        type=str,
                        help="這是解密的輸入圖片",
                        default="./ecb.png")
    parser.add_argument("-mode", 
                        '--mode',
                        type=str,
                        help="這是解密的模式",
                        default="ECB")
    parser.add_argument("-o", 
                        '--outputName',
                        type=str,
                        help="這是解密的輸出檔名",
                        default="res.png")
    args = parser.parse_args()
    print(args)

    # Key
    key = shareFunction.readKey("./key.bin")
    inputPath = args.decInput
    mode = args.mode
    outputDecPath = args.outputName

    info = shareFunction.readImage(inputPath)
    deInfo = decrypt(key, info, mode=mode)
    print("dec finished")
    shareFunction.writeJpge((deInfo[0], deInfo[1], deInfo[2]), outputDecPath)
    