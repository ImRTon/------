
if __name__ == '__main__':

    while(True):

        try:

            key = input()
            encryed = input()
            key = int(key)

            railFence = []
            for i in range(key):
                railFence.append('')

            step = 1
            current_row = 0
            for ch in encryed:
                railFence[current_row] += ch
                if current_row == key - 1:
                    step = -1
                elif current_row == 0:
                    step = 1
                current_row += step

            rail_len = []
            for i in range(key):
                rail_len.append(len(railFence[i]))

            index = 0
            railFence = []
            for i in range(key):
                railFence.append(encryed[index:index + rail_len[i]])
                index += rail_len[i]

            decryed = ''
            fence_index = []
            dir_down: bool = 1
            for i in range(key):
                fence_index.append(0)
            current_row = 0
            for i in range(len(encryed)):
                decryed += railFence[current_row][fence_index[current_row]]
                fence_index[current_row] += 1
                if dir_down:
                    if current_row == key - 1:
                        # last row
                        dir_down = 0
                        current_row = current_row - 1
                    else:
                        current_row = current_row + 1
                else:
                    if current_row == 0:
                        # top row
                        dir_down = 1
                        current_row = current_row + 1
                    else:
                        current_row = current_row - 1
        


            print(decryed)
        except:
            break

    