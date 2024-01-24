import random
class Area:
    area = [[0 for i in range(9)] for j in range(9)]
    def __print__(self):
        for i in range(9):
            for j in range(9):
                print(self.area[i][j], end="\t")
            print("\n\n")
    def __init__(self):
        count = 0
        while count < 10:
            boom_id = random.randint(0,80)
            boom_row, boom_col = divmod(boom_id,9)
            if self.area[boom_row][boom_col] == 0: # 如果该位置为0，就将该位置设为地雷X
                self.area[boom_row][boom_col] = 'X'
                count += 1
        self.__print__()
        # boom_row = random.randint(0,9)
        # boom_col = random.randint(0,9)
        # count = 0
        # if self.area[boom_row][boom_col] == 0: # 如果该位置为空，就将该位置设为地雷X
        #     self.area[boom_row][boom_col] = 'X'
        #     count += 1
area = Area()
area.__init__()
