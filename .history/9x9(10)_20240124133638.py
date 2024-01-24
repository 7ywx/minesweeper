class Area:
    area = [[0 for i in range(9)] for j in range(9)]
    def __print__(self):
        for i in range(9):
            for j in range(9):
                print(self.area[i][j], end=" ")
            print()
area = Area()
area.__print__()
