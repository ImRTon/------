
def char2num(ch:str):
    return ord(ch.lower()) - 97

def num2char(num:int):
    return chr(num + 97)

if __name__ == '__main__':
    
    while True:

        try:

            encryed = input()
            key = 9
            decryed = ""

            for ch in encryed:
                if ord(ch.lower()) >= ord('a') and ord(ch.lower()) <= ord('z'):
                    decryedCh = char2num(ch) - 9
                    if decryedCh < 0:
                        decryedCh += 26
                    decryed += num2char(decryedCh)
                else:
                    decryed += ch
            print(decryed)

        except:
            break
