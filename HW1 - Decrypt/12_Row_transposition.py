
def get_col_count(encryed, key, row):
    not_full_count = len(encryed) % len(key)
    if row < not_full_count:
        return int(len(encryed) / len(key) + 0.99)
        # return math.ceil(len(encryed) / len(key))
    else:
        return int(len(encryed) / len(key))

if __name__ == '__main__':
    
    while True:

        try:

            key = input()
            encryed = input()

            # table = []
            # index = 0
            # line = ""
            # for ch in encryed:
            #     if (index + 1) % len(key) == 0 or index == len(encryed) - 1:
            #         line += ch
            #         table.append(line)
            #         line = ''
            #     else:
            #         line += ch
            #     index += 1

            # print(table)



            aEmptyStr = []
            for i in range(len(key)):
                aEmptyStr.append(' ')
            cryedArray = []
            for i in range(int(len(encryed) / len(key) + 0.99)):
                cryedArray.append(aEmptyStr.copy())

            text_index = 0
            index = 1
            current_col = 0
            while(text_index < len(encryed)):
                if int(key[current_col]) == index:
                    for i in range(get_col_count(encryed, key, current_col)):
                        cryedArray[i][current_col] = encryed[text_index]
                        text_index += 1
                    current_col = 0
                    index += 1
                else:
                    current_col += 1
            decryed = ""
            for cryedLine in cryedArray:
                for cryedCh in cryedLine:
                    if cryedCh != ' ':
                        decryed += cryedCh.lower()
            print(decryed)
        except EOFError:
            break
