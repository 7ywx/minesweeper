import random
class Area:
    area = [[0 for i in range(9)] for j in range(9)]
    def __print__(self):
        for i in range(9):
            for j in range(9):
                print(self.area[i][j], end="\t")
            print("\n\n")
    def __init__(self):
        # make 10 boom
        count = 0
        while count < 10:
            boom_id = random.randint(0,80)
            boom_row, boom_col = divmod(boom_id,9)
            if self.area[boom_row][boom_col] == 0: # 如果该位置为0，就将该位置设为地雷X
                self.area[boom_row][boom_col] = 'X'
                count += 1
        # 填上数字
        num = 0 # 记录周围的地雷X数
        rows = len(self.area)
        cols = len(self.area[0]) if rows > 0 else 0
        for i in range(9):
            for j in range(9):
                if self.area[i][j] == 'X':
                    continue
                else:
                    num = 0
                    # 上方元素（如果存在）
                    if i > 0 and self.area[i - 1][j] == 'X':
                        num += 1

                    # 下方元素（如果存在）
                    if i < rows - 1 and self.area[i + 1][j] == 'X':
                        num += 1

                    # 左侧元素（如果存在）
                    if j > 0 and self.area[i][j - 1] == 'X':
                        num += 1

                    # 右侧元素（如果存在）
                    if j < cols - 1 and self.area[i][j + 1] == 'X':
                        num += 1

                    # 对角线方向的元素（如果存在）
                    if i > 0 and j > 0 and self.area[i - 1][j - 1] == 'X':
                        num += 1

                    if i > 0 and j < cols - 1 and self.area[i - 1][j + 1] == 'X':
                        num += 1

                    if i < rows - 1 and j > 0 and self.area[i + 1][j - 1] == 'X':
                        num += 1

                    if i < rows - 1 and j < cols - 1 and self.area[i + 1][j + 1] == 'X':
                        num += 1
                    self.area[i][j] = num
        # self.__print__()
area = Area()
def print_grid_with_coordinates(grid):
    # 输出列坐标
    print("  ", " ".join(str(i) for i in range(1, 10)))

    # 输出行坐标和格子内容
    for i, row in enumerate(grid, start=1):
        print(i, " ".join(map(str, row)))

# 生成一个 9x9 的二维数组（格子）
grid = [[0] * 9 for _ in range(9)]

# 调用函数输出带有坐标的格子
print_grid_with_coordinates(grid)
