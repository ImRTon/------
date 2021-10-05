
def char2num(ch:str):
    return ord(ch.lower()) - 97

def num2char(num:int):
    return chr(num + 97)

if __name__ == '__main__':
    
    while True:

        try:

            key = input()
            encryed = input()


            full_key = ""
            for i in range(len(encryed)):
                full_key += key[i % len(key)]

            index = 0
            decryed = ""
            for ch in encryed:
                decryedChNum:int = char2num(ch) -char2num(full_key[index])
                if decryedChNum < 0:
                    decryedChNum += 26
                decryed += num2char(decryedChNum)
                index += 1
            print(decryed)

        except:
            break
