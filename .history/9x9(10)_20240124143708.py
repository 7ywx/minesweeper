import random
class Game:
    area = [[0 for i in range(9)] for j in range(9)]
    def print_grid_with_coordinates(self, grid):
        # 输出列坐标
        print(" ", " ".join(str(i) for i in range(1, 10)))

        # 输出行坐标和格子内容
        for i, row in enumerate(grid, start=1):
            print(i, " ".join(map(str, row)))

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
        self.print_grid_with_coordinates(self.area)
    def start(self):
        print("-----游戏开始!-----")

        flag = True # 游戏是否继续的标志

        # 生成一个 9x9 的二维数组（格子）
        grid = [[0] * 9 for _ in range(9)]

        # 调用函数输出带有坐标的格子
        self.print_grid_with_coordinates(grid)
        while flag:
            user_input = input("请输入坐标（以空格隔开）:")
            try:
                row, col = map(int, user_input.split())
                if row < 1 or col < 1:  # 假设行和列的值至少为1
                    print("输入的坐标不合法，请确保行和列都是正整数！")
                if row > 9 or col > 9:
                    print("输入的坐标不合法，请确保行和列都不超过9！")
                # else:
                #     print(row, col)
                #     # break
            except ValueError:
                print("输入格式不正确，请确保输入的是两个由空格隔开的整数！")
            if self.area[row - 1][col - 1] == 'X':
                print("你点击的格子是地雷X！游戏结束！")
                flag = False

            flag = False

game = Game()
game.start()
