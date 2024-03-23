import tkinter as tk
import random
from tkinter import messagebox
from PIL import Image, ImageTk  # 需要导入PIL库的ImageTk模块来处理图像

image = None
im = None
class Snake:
    def __init__(self, master):
        self.master = master
        self.master.title("Snake")

        # 创建画布
        self.canvas = tk.Canvas(self.master, width=400, height=400, bg="black")
        self.canvas.pack()

        # 初始化游戏数据
        self.snake = [(0, 0), (0, 1), (0, 2)]
        self.food = (5, 5)
        self.direction = "Right"
        self.score = 0

        # 绑定键盘事件
        self.master.bind("<Key>", self.on_key_press)

        # 开始游戏
        self.start_game()

    def start_game(self):
        # 绘制贪吃蛇和食物
        self.draw_snake()
        self.draw_food()

        # 更新游戏状态
        self.update_game()

    def draw_snake(self):
        # 清空画布
        self.canvas.delete("all")

        global image
        global im

        # 绘制贪吃蛇
        for x, y in self.snake:
            x1 = x * 20
            y1 = y * 20
            x2 = x1 + 20
            y2 = y1 + 20
            self.canvas.create_rectangle(x1, y1, x2, y2, fill="green")

        # 绘制蛇头
        image = Image.open('resized_image.png') # 打开图片文件

        # 将PIL图像转换为tkinter的PhotoImage格式
        im = ImageTk.PhotoImage(image)

        snake_head = self.snake[-1]
        self.canvas.create_image(snake_head[0]*20, snake_head[1]*20, anchor='nw', image=im)

    def draw_food(self):
        # 绘制食物
        x1 = self.food[0] * 20
        y1 = self.food[1] * 20
        x2 = x1 + 20
        y2 = y1 + 20
        self.canvas.create_oval(x1, y1, x2, y2, fill="red")

    def update_game(self):
        # 更新贪吃蛇位置
        head_x, head_y = self.snake[-1]
        if self.direction == "Left":
            new_head = (head_x - 1, head_y)
        elif self.direction == "Right":
            new_head = (head_x + 1, head_y)
        elif self.direction == "Up":
            new_head = (head_x, head_y - 1)
        else:
            new_head = (head_x, head_y + 1)
        self.snake.append(new_head)
        del self.snake[0]

        # 检查游戏是否结束
        if new_head[0] < 0 or new_head[0] >= 20 or new_head[1] < 0 or new_head[1] >= 20 or new_head in self.snake[:-1]:
            messagebox.showinfo("Game Over", f"Score: {self.score}")
            return

        # 检查贪吃蛇是否吃掉食物
        if new_head == self.food:
            while True:
                food_x = random.randint(0, 19)
                food_y = random.randint(0, 19)
                if (food_x, food_y) not in self.snake:
                    break
            self.food = (food_x, food_y)
            tail_x, tail_y = self.snake[0]
            if self.direction == "Left":
                new_tail = (tail_x + 1, tail_y)
            elif self.direction == "Right":
                new_tail = (tail_x - 1, tail_y)
            elif self.direction == "Up":
                new_tail = (tail_x, tail_y + 1)
            else:
                new_tail = (tail_x, tail_y - 1)
            self.snake.insert(0, new_tail)
            self.score += 1

        # 绘制贪吃蛇和食物
        self.draw_snake()
        self.draw_food()

        # 定时更新游戏状态
        self.master.after(150, self.update_game)

    def on_key_press(self, event):
        # 使用字典映射来简化键盘事件到方向的映射，提高代码的可读性和可维护性
        key_map = {
            "Left": "Left",
            "Right": "Right",
            "Up": "Up",
            "Down": "Down",
            "w": "Up",
            "W": "Up",
            "a": "Left",
            "A": "Left",
            "s": "Down",
            "S": "Down",
            "d": "Right",
            "D": "Right",
        }

        # 使用字典的get方法来查询映射，如果事件按键不在映射中，则保持之前的direction值
        self.direction = key_map.get(event.keysym, self.direction)

if __name__ == "__main__":
    root = tk.Tk()
    snake = Snake(root)
    root.mainloop()
