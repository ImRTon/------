def if_exist_in_list(element, list):
    for list_item in list:
        if list_item == element:
            return True
    return False

def get_cord(char, list):
    for i in range(5):
        for j in range(5):
            if list[i][j] == char:
                return i, j
            elif char == 'J' and list[i][j] == 'I':
                return i, j

if __name__ == '__main__':
    
    while True:

        try:
            key = input()
            key = key.upper()
            encryed = input()
            encryed = encryed.upper()

            alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'
                        , 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S'
                        , 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
            
            
            flat_table = []
            for ch in key:
                re_flag = False
                for table_ch in flat_table:
                    if table_ch == ch:
                        # 重複
                        re_flag = True
                        break
                if re_flag:
                    continue
                else:
                    flat_table.append(ch)
            for ch in alphabet:
                re_flag = False
                for table_ch in flat_table:
                    if table_ch == ch:
                        # 重複
                        re_flag = True
                        break
                if re_flag:
                    continue
                else:
                    flat_table.append(ch)

            table = []
            index = 0
            for i in range(5):
                row = []
                for j in range(5):
                    row.append(flat_table[index])
                    index += 1
                table.append(row)
            # print(table)
            decryed = ''
            for i in range(int(len(encryed) / 2)):
                letterA = encryed[i * 2]
                letterB = encryed[i * 2 + 1]
                # print(letterA, letterB)
                A_cord_i, A_cord_j = get_cord(letterA, table)
                B_cord_i, B_cord_j = get_cord(letterB, table)
                ori_A = ''
                ori_B = ''
                if A_cord_i == B_cord_i:
                    # same row
                    ori_A = table[A_cord_i][(A_cord_j + 4) % 5]
                    ori_B = table[B_cord_i][(B_cord_j + 4) % 5]
                elif A_cord_j == B_cord_j:
                    # same column
                    ori_A = table[(A_cord_i + 4) % 5][A_cord_j]
                    ori_B = table[(B_cord_i + 4) % 5][B_cord_j]
                else:
                    # rectangle
                    ori_A = table[A_cord_i][B_cord_j]
                    ori_B = table[B_cord_i][A_cord_j]
                if ori_A == '@':
                    ori_A = 'I'
                if ori_B == '@':
                    ori_B = 'I'
                decryed += ori_A.upper()
                decryed += ori_B.upper()
            print(decryed)
        except :
            break
