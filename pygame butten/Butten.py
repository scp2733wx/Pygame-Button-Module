import pygame

# 定义一些常用的颜色
COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_LIGHT_BLUE = (156, 220, 254)
COLOR_PINK = (218, 94, 152)
COLOR_ORANGE = (243, 133, 24)
COLOR_GREEN = (100, 115, 0)

class Button:
    """
    基础按钮类
    处理按钮的绘制、点击反馈、悬停反馈和状态切换。
    """
    def __init__(self, xy, size, frame_color=(COLOR_PINK, COLOR_LIGHT_BLUE)):
        """
        初始化按钮。
        xy: 按钮左上角的绘制坐标 (x, y)。
        size: 按钮的尺寸 (宽度, 高度)。
        frame_color: 一个元组，包含 (点击时边框颜色, 悬停/默认时边框颜色)。
        """
        self.x, self.y = xy
        self.width, self.height = size
        self.click_time_delay = 10  # 点击后延迟，防止连续触发
        self._current_time_delay = 0
        self.is_hovered = False  # 鼠标是否悬停在按钮上
        self.is_clicked = False  # 按钮是否被点击
        self.frame_colors = frame_color
        # 按钮状态，例如用于切换开关按钮
        # state[0] 是状态列表，state[1] 是当前状态的索引
        self.state = [[False, True], 0] # 默认状态为布尔值，已将外层元组改为列表，使其可变

    def _is_mouse_in_area(self, mx, my):
        """
        检查鼠标坐标是否在按钮区域内。
        mx: 鼠标X坐标。
        my: 鼠标Y坐标。
        返回: 如果鼠标在区域内则为True，否则为False。
        """
        return self.x < mx < self.x + self.width and self.y < my < self.y + self.height

    def draw_frame(self, screen):
        """
        绘制按钮的边框和背景。
        screen: Pygame 屏幕对象。
        """
        mx, my = pygame.mouse.get_pos()
        self.is_hovered = self._is_mouse_in_area(mx, my)

        # 处理点击延迟
        if self._current_time_delay > 0:
            self._current_time_delay -= 1
            
        mouse_clicked = pygame.mouse.get_pressed()[0] # 检查鼠标左键是否按下

        if mouse_clicked and self.is_hovered and self._current_time_delay == 0:
            # 鼠标在区域内且被点击
            pygame.draw.rect(screen, self.frame_colors[0], (self.x, self.y, self.width, self.height), 1) # 绘制边框
            self._current_time_delay = self.click_time_delay # 设置点击延迟
            self.is_clicked = True
        elif self.is_hovered:
            # 鼠标悬停但未点击
            pygame.draw.rect(screen, self.frame_colors[0], (self.x, self.y, self.width, self.height)) # 绘制填充矩形
            self.is_clicked = False
        else:
            # 鼠标不在区域内
            pygame.draw.rect(screen, self.frame_colors[1], (self.x, self.y, self.width, self.height)) # 绘制填充矩形
            self.is_clicked = False

    def draw(self, screen, custom_frame_draw_func=None):
        """
        绘制按钮。
        screen: Pygame 屏幕对象。
        custom_frame_draw_func: 可选参数，一个自定义的绘制边框函数。
                                 如果提供，将使用此函数而不是默认的 draw_frame。
                                 函数签名应为: custom_frame_draw_func(button_instance, screen)。
        """
        if custom_frame_draw_func:
            custom_frame_draw_func(self, screen)
        else:
            self.draw_frame(screen)
        
        # 如果按钮被点击，则切换状态
        if self.is_clicked:
            self.toggle_state()

        # 基础按钮不再绘制 'Y'/'X'，这应该由子类或外部逻辑处理
        # 可以在这里添加一些通用的视觉反馈，例如一个简单的圆点或方块来表示状态
        if self.get_state():
            pygame.draw.circle(screen, COLOR_GREEN, (self.x + self.width // 2, self.y + self.height // 2), min(self.width, self.height) // 4)
        else:
            pygame.draw.rect(screen, COLOR_BLACK, (self.x + self.width // 2 - min(self.width, self.height) // 4, self.y + self.height // 2 - min(self.width, self.height) // 4, min(self.width, self.height) // 2, min(self.width, self.height) // 2), 1)


    def get_state(self):
        """
        获取按钮的当前状态。
        返回: 当前状态值。
        """
        return self.state[0][self.state[1]]
    
    def toggle_state(self):
        """
        切换按钮的状态。
        """
        self.state[1] = (self.state[1] + 1) % len(self.state[0])


class TextButton(Button):
    """
    文本按钮类，继承自 Button。
    在按钮上显示文本。
    """
    def __init__(self, xy, size, texts, font_path, font_size, text_color=COLOR_BLACK, bg_color=None):
        """
        初始化文本按钮。
        texts: 要显示的文本列表（支持多个状态文本）。
        font_path: 字体文件路径。
        font_size: 字体尺寸。
        text_color: 字体颜色。
        bg_color: 文本背景颜色 (可选)。
        """
        super().__init__(xy, size)
        self.texts = texts[:] # 文本列表
        self.current_text_index = 0 # 当前显示的文本索引
        self.font_size = font_size
        self.text_color = text_color
        self.bg_color = bg_color

        try:
            self.font = pygame.font.Font(font_path, font_size)
        except FileNotFoundError:
            print(f"警告: 字体文件 '{font_path}' 未找到。将使用 Pygame 默认字体。")
            self.font = pygame.font.SysFont(None, font_size) # 使用系统默认字体

    def draw(self, screen, custom_frame_draw_func=None):
        """
        绘制文本按钮。
        screen: Pygame 屏幕对象。
        custom_frame_draw_func: 可选参数，自定义边框绘制函数。
        """
        # 调用父类的 draw_frame 方法来处理边框和点击逻辑
        if custom_frame_draw_func:
            custom_frame_draw_func(self, screen)
        else:
            self.draw_frame(screen)
        
        # 如果按钮被点击，则切换文本状态
        if self.is_clicked:
            self.current_text_index = (self.current_text_index + 1) % len(self.texts)
            self.is_clicked = False # 重置点击状态，防止连续触发

        # 渲染文本
        current_text = self.texts[self.current_text_index]
        if self.bg_color:
            rendered_text = self.font.render(current_text, True, self.text_color, self.bg_color)
        else:
            rendered_text = self.font.render(current_text, True, self.text_color)
        
        text_rect = rendered_text.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))
        screen.blit(rendered_text, text_rect)


class ImageButton(Button):
    """
    图片按钮类，继承自 Button。
    在按钮上显示图片。
    """
    def __init__(self, xy, size, image_paths, img_size):
        """
        初始化图片按钮。
        image_paths: 图片文件路径列表（支持多个状态图片）。
        img_size: 图片尺寸 (宽度, 高度)。
        """
        super().__init__(xy, size)
        self.image_paths = image_paths[:] # 图片路径列表
        self.current_image_index = 0 # 当前显示的图片索引
        self.img_width, self.img_height = img_size
        self.images = [] # 存储加载后的图片对象

        # 尝试加载所有图片
        for path in self.image_paths:
            try:
                img = pygame.image.load(path)
                img = pygame.transform.scale(img, img_size)
                self.images.append(img)
            except pygame.error as e:
                print(f"警告: 无法加载图片 '{path}'。错误: {e}")
                # 如果图片加载失败，添加一个占位符
                placeholder_surface = pygame.Surface(img_size)
                placeholder_surface.fill(COLOR_BLACK) # 黑色背景
                pygame.draw.line(placeholder_surface, COLOR_WHITE, (0, 0), img_size, 2)
                pygame.draw.line(placeholder_surface, COLOR_WHITE, (img_size[0], 0), (0, img_size[1]), 2)
                self.images.append(placeholder_surface)
        
        if not self.images: # 如果没有任何图片加载成功，添加一个默认占位符
            placeholder_surface = pygame.Surface(img_size)
            placeholder_surface.fill(COLOR_BLACK)
            self.images.append(placeholder_surface)


    def draw(self, screen, custom_frame_draw_func=None):
        """
        绘制图片按钮。
        screen: Pygame 屏幕对象。
        custom_frame_draw_func: 可选参数，自定义边框绘制函数。
        """
        # 调用父类的 draw_frame 方法来处理边框和点击逻辑
        if custom_frame_draw_func:
            custom_frame_draw_func(self, screen)
        else:
            self.draw_frame(screen)
        
        # 如果按钮被点击，则切换图片状态
        if self.is_clicked:
            self.current_image_index = (self.current_image_index + 1) % len(self.images)
            self.is_clicked = False # 重置点击状态

        # 绘制当前图片
        if self.images:
            current_img = self.images[self.current_image_index]
            img_rect = current_img.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))
            screen.blit(current_img, img_rect)


class InputButton(Button):
    """
    输入框按钮类，继承自 Button。
    提供一个可输入文本的输入框。
    """
    def __init__(self, xy, size, initial_text='', cursor_blink_rate=15):
        """
        初始化输入框按钮。
        initial_text: 初始显示的字符串。
        cursor_blink_rate: 光标闪烁频率 (帧数)。
        """
        super().__init__(xy, size, frame_color=(COLOR_BLACK, COLOR_ORANGE)) # 输入框默认边框颜色
        self.text_content = initial_text
        self.cursor_blink_rate = cursor_blink_rate
        self._cursor_timer = 0 # 光标闪烁计时器
        self.cursor_position = len(initial_text) # 光标在字符串中的位置 (正数索引)
        
        # 字体大小根据按钮高度调整
        self.font = pygame.font.Font(None, min(self.width, self.height) - 5) # 使用系统默认字体

        # 激活状态，True表示可以输入
        # self.state[1] 用于表示激活状态：0=未激活，1=激活
        self.state = [[False, True], 0] # 0: 非激活, 1: 激活

    def draw_frame(self, screen):
        """
        绘制输入框的边框。
        screen: Pygame 屏幕对象。
        """
        mx, my = pygame.mouse.get_pos()
        self.is_hovered = self._is_mouse_in_area(mx, my)

        # 处理点击延迟
        if self._current_time_delay > 0:
            self._current_time_delay -= 1
        
        mouse_clicked = pygame.mouse.get_pressed()[0]

        if mouse_clicked and self.is_hovered and self._current_time_delay == 0:
            # 鼠标在区域内且被点击，激活输入状态
            pygame.draw.rect(screen, self.frame_colors[0], (self.x, self.y, self.width, self.height), 2) # 绘制边框
            self._current_time_delay = self.click_time_delay
            self.state[1] = 1 # 激活输入状态
            self.is_clicked = True
        elif self.is_hovered:
            # 鼠标悬停
            pygame.draw.rect(screen, self.frame_colors[1], (self.x, self.y, self.width, self.height), 2) # 绘制边框
            self.is_clicked = False
        else:
            # 鼠标不在区域内
            pygame.draw.rect(screen, self.frame_colors[1], (self.x, self.y, self.width, self.height), 2) # 绘制边框
            self.state[1] = 0 # 非激活输入状态
            self.is_clicked = False

    def draw(self, screen, custom_frame_draw_func=None):
        """
        绘制输入框。
        screen: Pygame 屏幕对象。
        custom_frame_draw_func: 可选参数，自定义边框绘制函数。
        """
        if custom_frame_draw_func:
            custom_frame_draw_func(self, screen)
        else:
            self.draw_frame(screen)
        
        # 更新光标闪烁计时器
        if self.get_state(): # 只有在激活状态下才闪烁光标
            self._cursor_timer = (self._cursor_timer + 1) % (self.cursor_blink_rate * 2)

        display_text = self.text_content
        if self.get_state() and self._cursor_timer < self.cursor_blink_rate:
            # 在光标位置插入 '|' 进行显示，但不修改实际文本内容
            display_text = display_text[:self.cursor_position] + '|' + display_text[self.cursor_position:]

        rendered_text = self.font.render(display_text, True, COLOR_BLACK)
        text_rect = rendered_text.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))
        screen.blit(rendered_text, text_rect)

    def handle_input_event(self, event):
        """
        处理键盘输入事件。
        event: Pygame 事件对象。
        """
        if not self.get_state(): # 只有在激活状态下才处理输入
            return

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                if self.cursor_position > 0:
                    self.text_content = self.text_content[:self.cursor_position - 1] + self.text_content[self.cursor_position:]
                    self.cursor_position -= 1
            elif event.key == pygame.K_DELETE:
                if self.cursor_position < len(self.text_content):
                    self.text_content = self.text_content[:self.cursor_position] + self.text_content[self.cursor_position + 1:]
            elif event.key == pygame.K_LEFT:
                self.cursor_position = max(0, self.cursor_position - 1)
            elif event.key == pygame.K_RIGHT:
                self.cursor_position = min(len(self.text_content), self.cursor_position + 1)
            elif event.unicode: # 处理普通字符输入
                self.text_content = self.text_content[:self.cursor_position] + event.unicode + self.text_content[self.cursor_position:]
                self.cursor_position += len(event.unicode) # 移动光标到新字符之后
            
            # 每次输入后重置光标闪烁计时器
            self._cursor_timer = 0
    
    def get_text(self):
        """
        获取输入框中的当前文本。
        返回: 输入框中的字符串。
        """
        return self.text_content


