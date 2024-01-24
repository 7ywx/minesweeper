class Area:
    area = [[0 for i in range(9)] for j in range(9)]
    def __print__(self):
        for i in range(9):
            for j in range(9):
                print(self.area[i][j], end="\t")
            print("\n\n")
    def __init__(self):
        boom_row = random.randint(0,9)
        boom_col = random.randint(0,9)
        print(boom_row, boom_col)
area = Area()
area.__print__()
