from Crypto.Cipher import AES
import Crypto.Random
import shareFunction
import argparse

################## encrypt functions ##################
#return encrypt(data + padding(None)) + padding(None) + padding(data position) + padding(encrypt position)
def encrypt(key: bytes, info: (int, int, bytes), mode = "ECB") -> (int, int, bytes):
    blockSize = 16
    height = info[0]
    width = info[1]
    blocks = shareFunction.clipBlocks(info[2], blockSize)
    cipher = AES.new(key, AES.MODE_ECB)

    #record data postion
    lastDataStreamPosition = (len(blocks)-1) * blockSize  + len(blocks[-1])

    if(len(blocks[-1]) < blockSize):
        print("do padding")
        blocks[-1] += bytes(blockSize - len(blocks[-1]))
        pass

    vi = ""
    counter = 0
    keyImgInfo = ""
    if(mode == "CTR" or mode == "Custom"):
        vi = shareFunction.readKey("./iv.bin")
        counter = 0
        if(mode == "Custom"):
            keyImgInfo = shareFunction.readGrayImage("./middle_finger.png")

    # encrypt
    encrpytData = bytes(0)
    for block in blocks:
        ci = []
        if(mode == "ECB"):
            ci = encrypt_ECBmode(block, cipher)
            pass
        elif(mode == "CTR"):
            vi = shareFunction.byteAddOne(vi)
            ci = encrypt_CTRmode(block, cipher, vi)
            pass
        elif(mode == "Custom"):
            counter += 1
            temp = shareFunction.getImgVal(vi, counter, keyImgInfo)
            ci = encrypt_CustomMode(block, cipher, temp)
            pass
        else:
            print("have no this mode")
            assert(False)
        encrpytData += ci
    pass

    #padding to image
    lastEncryptDataStreamPosition = len(encrpytData)
    positionInfo = "\n" + str(lastDataStreamPosition) + "\n" + str(lastEncryptDataStreamPosition) + "\n"
    positionInfo = positionInfo.encode()

    
    while((len(encrpytData) + len(positionInfo)) % (width * 3) != 0):
        positionInfo = bytes(1) + positionInfo
    image = encrpytData + positionInfo

    if(len(image) % (width * 3) != 0):
        print("image lens % width != 0,  image: ", len(image), "width * 3: ", (width * 3))
        assert(len(image) % (width * 3) == 0)

    height = len(image) / width
    print("lastDataStreamPosition:", lastDataStreamPosition, "lastEncryptDataStreamPosition:", lastEncryptDataStreamPosition)
    return (height, width, image)

# return ci
def encrypt_ECBmode(mi, ek):
    return ek.encrypt(mi)

# return ci
def encrypt_CTRmode(pi, ek, counter):
    temp = ek.encrypt(counter)
    ci = shareFunction.xor(temp, pi)
    return ci

# return ci
def encrypt_CustomMode(pi, ek, counter):
    temp = ek.encrypt(counter)
    ci = shareFunction.xor(temp, pi)
    return ci



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, default="./linux.jpg",
                        help="input image path, default: ./linux.jpg")
    parser.add_argument("--mode", type=str, default="ECB",
                        help="encrypt mode, ECB, CTR, Custom. default: ECB")
    parser.add_argument("--output", type=str, default="",
                        help="output image path, default: ./[mode].png")
    args = parser.parse_args()

    inputPath = args.input
    mode = args.mode
    outputPath = args.output

    if(outputPath == ""):
        outputPath = "./" + mode + ".png"
    key = shareFunction.readKey("./key.bin")
    info = shareFunction.readImage(inputPath)

    enInfo = encrypt(key, info, mode)
    print("encrypt finished.", "width:", enInfo[1], "height:", enInfo[0])
    print("output image...")
    shareFunction.writeJpge(enInfo, outputPath)
    print("Done")