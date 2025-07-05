<h1>Pygame 按钮模块</h1><p>这是一个为 Pygame 游戏开发设计的按钮模块，提供了基础按钮、文本按钮、图片按钮和输入框按钮等多种功能。</p><h2>文件结构</h2><ul><li><p><code>Butten.py</code>: 包含 <code>Button</code> 及其子类的核心实现。</p></li><li><p><code>test_butten.py</code>: 演示如何使用 <code>Butten.py</code> 中定义的按钮类的示例代码。</p></li></ul><h2>功能特性</h2><h3>1. 基础按钮 (<code>Button</code>)</h3><ul><li><p><strong>点击反馈</strong>: 鼠标点击时边框颜色变化。</p></li><li><p><strong>悬停反馈</strong>: 鼠标悬停时背景颜色变化。</p></li><li><p><strong>状态切换</strong>: 支持布尔状态的切换（例如，用于开关按钮）。</p></li></ul><h3>2. 文本按钮 (<code>TextButton</code>)</h3><ul><li><p>继承自 <code>Button</code>。</p></li><li><p>可以在按钮上显示文本。</p></li><li><p>支持多状态文本，点击后文本会切换。</p></li><li><p>可自定义字体、字体大小、文本颜色和背景颜色。</p></li></ul><h3>3. 图片按钮 (<code>ImageButton</code>)</h3><ul><li><p>继承自 <code>Button</code>。</p></li><li><p>可以在按钮上显示图片。</p></li><li><p>支持多状态图片，点击后图片会切换。</p></li><li><p>自动处理图片加载失败的情况，并显示占位符。</p></li></ul><h3>4. 输入框按钮 (<code>InputButton</code>)</h3><ul><li><p>继承自 <code>Button</code>。</p></li><li><p>提供一个可输入文本的区域。</p></li><li><p>支持键盘输入（包括退格、删除、左右箭头移动光标）。</p></li><li><p>光标闪烁效果。</p></li><li><p>激活状态管理，只有激活时才能输入。</p></li></ul><h2>如何使用</h2><h3>1. 环境准备</h3><p>确保您已安装 Pygame 库：</p><pre><code>pip install pygame
<br class="ProseMirror-trailingBreak"></code></pre><h3>2. 运行示例</h3><p>运行 <code>test_butten.py</code> 文件以查看按钮模块的实际效果：</p><pre><code>python test_butten.py
<br class="ProseMirror-trailingBreak"></code></pre><p><strong>注意</strong>:</p><ul><li><p><code>test_butten.py</code> 会检查 <code>font.ttf</code> 和 <code>test.png</code> 文件是否存在。如果不存在，它会打印警告并尝试使用 Pygame 默认字体或创建简单的占位符图片，以确保示例能够运行。为了获得最佳效果，建议您提供真实的字体文件和图片文件。</p></li></ul><h3>3. 在您的项目中使用</h3><p>您可以将 <code>Butten.py</code> 导入到您的 Pygame 项目中，然后创建并使用各种按钮实例：</p><pre><code>import pygame
from Butten import Button, TextButton, ImageButton, InputButton, COLOR_BLACK, COLOR_WHITE

# 初始化 Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("我的 Pygame 应用")

# 创建一个文本按钮
my_text_button = TextButton(
    xy=[100, 100],
    size=[150, 50],
    texts=['开始游戏', '游戏中...'],
    font_path='font.ttf', # 替换为您的字体路径
    font_size=30,
    text_color=COLOR_BLACK,
    bg_color=COLOR_WHITE
)

# 创建一个输入框按钮
my_input_button = InputButton(
    xy=[100, 200],
    size=[300, 50],
    initial_text='输入您的名字'
)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # 将事件传递给输入框按钮处理
        my_input_button.handle_input_event(event)

    screen.fill((200, 200, 200)) # 填充背景

    # 绘制按钮
    my_text_button.draw(screen)
    my_input_button.draw(screen)

    pygame.display.update()

pygame.quit()
<br class="ProseMirror-trailingBreak"></code></pre><h2>类和方法详解</h2><h3><code>Button</code> (基础按钮)</h3><p><strong>初始化</strong>:
<code>Button(xy, size, frame_color=(COLOR_PINK, COLOR_LIGHT_BLUE))</code></p><ul><li><p><code>xy</code>: 按钮左上角的坐标 <code>(x, y)</code>。</p></li><li><p><code>size</code>: 按钮的尺寸 <code>(宽度, 高度)</code>。</p></li><li><p><code>frame_color</code>: 一个元组 <code>(点击时边框颜色, 悬停/默认时边框颜色)</code>。</p></li></ul><p><strong>方法</strong>:</p><ul><li><p><code>draw(screen, custom_frame_draw_func=None)</code>: 绘制按钮。</p></li><li><p><code>get_state()</code>: 获取按钮的当前状态（布尔值）。</p></li><li><p><code>toggle_state()</code>: 切换按钮的状态。</p></li></ul><h3><code>TextButton</code> (文本按钮)</h3><p><strong>初始化</strong>:
<code>TextButton(xy, size, texts, font_path, font_size, text_color=COLOR_BLACK, bg_color=None)</code></p><ul><li><p><code>texts</code>: 要显示的文本列表（支持多个状态文本）。</p></li><li><p><code>font_path</code>: 字体文件路径。</p></li><li><p><code>font_size</code>: 字体尺寸。</p></li><li><p><code>text_color</code>: 字体颜色。</p></li><li><p><code>bg_color</code>: 文本背景颜色 (可选)。</p></li></ul><h3><code>ImageButton</code> (图片按钮)</h3><p><strong>初始化</strong>:
<code>ImageButton(xy, size, image_paths, img_size)</code></p><ul><li><p><code>image_paths</code>: 图片文件路径列表（支持多个状态图片）。</p></li><li><p><code>img_size</code>: 图片尺寸 <code>(宽度, 高度)</code>。</p></li></ul><h3><code>InputButton</code> (输入框按钮)</h3><p><strong>初始化</strong>:
<code>InputButton(xy, size, initial_text='', cursor_blink_rate=15)</code></p><ul><li><p><code>initial_text</code>: 初始显示的字符串。</p></li><li><p><code>cursor_blink_rate</code>: 光标闪烁频率 (帧数)。</p></li></ul><p><strong>方法</strong>:</p><ul><li><p><code>handle_input_event(event)</code>: 处理键盘输入事件。</p></li><li><p><code>get_text()</code>: 获取输入框中的当前文本。</p></li></ul><h2>颜色定义</h2><p><code>Butten.py</code> 中定义了一些常用的颜色常量：</p><ul><li><p><code>COLOR_WHITE = (255, 255, 255)</code></p></li><li><p><code>COLOR_BLACK = (0, 0, 0)</code></p></li><li><p><code>COLOR_LIGHT_BLUE = (156, 220, 254)</code></p></li><li><p><code>COLOR_PINK = (218, 94, 152)</code></p></li><li><p><code>COLOR_ORANGE = (243, 133, 24)</code></p></li><li><p><code>COLOR_GREEN = (100, 115, 0)</code></p></li></ul><h2>贡献</h2><p>欢迎对本项目进行贡献！如果您有任何建议或发现 Bug，请随时提出。</p><h2>作者</h2><p>二七叁叁</p>
