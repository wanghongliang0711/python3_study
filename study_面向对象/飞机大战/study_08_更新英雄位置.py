
import pygame, time

pygame.init()

# 创建游戏的窗口  480 * 700
screen = pygame.display.set_mode((480, 700))

# 绘制背景图像
# 1> 加载图像数据
bg = pygame.image.load("./images/background.png")
# 2> blit绘制图像
screen.blit(bg, (0, 0))
# 3> update 更新屏幕显示
# pygame.display.update()

# 绘制英雄的飞机
hero = pygame.image.load("./images/me1.png")
screen.blit(hero, (150, 300))

# 可以在所有绘制工作完成之后，统一调用update方法
pygame.display.update()

# 创建时钟对象
clock = pygame.time.Clock()

# 1. 定义rect记录飞机的初始位置
hero_rect = pygame.Rect(150, 300, 102, 126)

# 游戏循环 -> 意味着游戏正式开始
while True:
    # 可以指定循环内部的代码执行的频率
    clock.tick(60)

    # 2. 修改飞机的位置
    hero_rect.y -= 1

    # 3. 调用blit方法绘制图像
    screen.blit(bg, (0, 0))  # 先用背景覆盖之前的图片，不然会出现多个英雄飞机
    screen.blit(hero, hero_rect)

    # 4. 调用update方法更新显示
    pygame.display.update()


pygame.quit()