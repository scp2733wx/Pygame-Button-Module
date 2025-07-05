Pygame 按钮模块这是一个为 Pygame 应用程序设计的通用按钮模块，提供了基础按钮、文本按钮、图片按钮和输入框按钮的功能。文件结构Butten.py: 包含 Button 及其子类的核心实现。test_butten.py: 演示如何使用 Butten.py 中定义的各种按钮类。特性基础按钮 (Button):支持点击和悬停反馈。可自定义边框颜色。内置状态切换功能（例如用于开关按钮）。点击后有短暂的延迟，防止连续触发。文本按钮 (TextButton):继承自 Button。可在按钮上显示文本。支持多状态文本显示（点击后切换文本）。可自定义字体、字号、文本颜色和背景颜色。图片按钮 (ImageButton):继承自 Button。可在按钮上显示图片。支持多状态图片显示（点击后切换图片）。图片加载失败时提供占位符。输入框按钮 (InputButton):继承自 Button。提供一个可输入文本的区域。支持光标闪烁。支持键盘输入（退格、删除、左右移动光标、字符输入）。激活/非激活状态管理。如何使用1. 准备环境确保您已安装 Pygame 库。如果您尚未安装，可以使用 pip 进行安装：pip install pygame
2. 运行示例要查看按钮的实际效果，可以运行 test_butten.py 文件：python test_butten.py
运行前，请注意 test_butten.py 会尝试加载 font.ttf 和 test.png。如果这些文件不存在，它会打印警告并使用系统默认字体或生成一个简单的占位符图片。为了获得最佳效果，建议您提供真实的字体文件和图片文件。3. 在您的项目中使用您可以将 Butten.py 导入到您的 Pygame 项目中，然后创建各种按钮实例：import pygame
from Butten import Button, TextButton, ImageButton, InputButton, COLOR_BLACK, COLOR_WHITE

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("我的 Pygame 应用")

# 创建一个基础按钮
my_button = Button([100, 100], [150, 50])

# 创建一个文本按钮
my_text_button = TextButton([100, 200], [200, 60], ['开始', '暂停'], 'font.ttf', 30, text_color=COLOR_WHITE, bg_color=COLOR_BLACK)

# 创建一个图片按钮
# 确保 'my_image.png' 存在
my_image_button = ImageButton([100, 300], [100, 100], ['my_image.png'], [80, 80])

# 创建一个输入框按钮
my_input_button = InputButton([100, 400], [300, 50], initial_text='输入您的名字')

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # 将事件传递给输入框按钮处理
        my_input_button.handle_input_event(event)

    screen.fill((200, 200, 200)) # 填充背景

    # 绘制所有按钮
    my_button.draw(screen)
    my_text_button.draw(screen)
    my_image_button.draw(screen)
    my_input_button.draw(screen)

    # 获取输入框文本
    # print(my_input_button.get_text())

    pygame.display.flip()

pygame.quit()
颜色定义Butten.py 中定义了一些常用的颜色常量，方便使用：COLOR_WHITE = (255, 255, 255)COLOR_BLACK = (0, 0, 0)COLOR_LIGHT_BLUE = (156, 220, 254)COLOR_PINK = (218, 94, 152)COLOR_ORANGE = (243, 133, 24)COLOR_GREEN = (100, 115, 0)作者二七叁叁
