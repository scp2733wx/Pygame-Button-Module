import pygame, os
from Butten import *


if __name__ == '__main__':
    pygame.init()
    SIZE = 520, 520
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("按钮模块测试")
    screen.fill(COLOR_WHITE)

    # 创建一些测试文件，如果它们不存在的话
    if not os.path.exists('font.ttf'):
        # 简单创建，实际应用中应提供真实字体文件
        # 这里只是为了让示例代码能运行，不保证字体效果
        print("注意: 'font.ttf' 文件不存在，请提供一个真实的字体文件以获得最佳效果。")
        # Pygame.font.SysFont(None, ...) 会使用系统默认字体，所以这里不强制创建空文件

    if not os.path.exists('test.png'):
        print("注意: 'test.png' 文件不存在，将使用占位符图片。")
        # 创建一个简单的占位符图片
        temp_surface = pygame.Surface((50, 50), pygame.SRCALPHA)
        temp_surface.fill((255, 0, 0, 100)) # 半透明红色
        pygame.draw.circle(temp_surface, (255, 255, 255, 200), (25, 25), 20)
        pygame.image.save(temp_surface, 'test.png')

    # 按钮实例
    test_buttons = [
        Button([20, 20], [80, 40]), # 基础按钮
        TextButton([20, 80], [120, 40], ['点击我', '已点击'], 'font.ttf', 20, text_color=COLOR_BLACK, bg_color=COLOR_WHITE), # 文本按钮
        ImageButton([20, 140], [100, 60], ['test.png'], [50, 50]), # 图片按钮
        InputButton([20, 220], [200, 40], initial_text='请输入文本') # 输入框按钮
    ]
    
    running = True
    while running:
        screen.fill(COLOR_WHITE) # 每次循环填充背景

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            # 将事件传递给输入框按钮处理
            for button in test_buttons:
                if isinstance(button, InputButton):
                    button.handle_input_event(event)

        # 绘制所有按钮
        for button in test_buttons:
            button.draw(screen)
        
        pygame.display.update() # 更新屏幕显示
        pygame.time.Clock().tick(30) # 控制帧率

    pygame.quit()
    print('程序已退出。')
else:
    # 提示信息
    print('by 二七叁叁')
