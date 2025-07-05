<h1 data-spm-anchor-id="5176.28103460.0.i3.3a2f1db8esF0tc">🎮 Pygame 按钮模块文档</h1>
<blockquote>
<p>作者：二七叁叁<br>
最后更新时间：2025年7月6日</p>
</blockquote>
<h2>🔧 模块简介</h2>
<p data-spm-anchor-id="5176.28103460.0.i5.3a2f1db8esF0tc">这是一个为 <strong>Pygame 游戏开发</strong> 设计的按钮模块，提供了以下几种按钮类型：</p>
<ul>
<li>基础按钮（<code node="[object Object]">Button</code>）</li>
<li data-spm-anchor-id="5176.28103460.0.i4.3a2f1db8esF0tc">文本按钮（<code node="[object Object]">TextButton</code>）</li>
<li>图片按钮（<code node="[object Object]">ImageButton</code>）</li>
<li>输入框按钮（<code node="[object Object]">InputButton</code>）</li>
</ul>
<p>每个按钮都支持点击反馈、状态切换以及视觉上的交互效果，适合用于游戏菜单、设置界面等场景。</p>
<hr>
<h2>📁 文件结构</h2>
<pre><div class="tongyi-design-highlighter global-dark-theme"><span class="tongyi-design-highlighter-header" style="background-color: rgb(44, 44, 54);"><span class="tongyi-design-highlighter-lang">bash</span><div class="tongyi-design-highlighter-right-actions"><div class="tongyi-design-highlighter-theme-changer"><div class="tongyi-design-highlighter-theme-changer-btn"><span>深色版本</span><span role="img" class="anticon"><svg width="1em" height="1em" fill="currentColor" aria-hidden="true" focusable="false" class=""><use xlink:href="#tongyi-down-line"></use></svg></span></div></div><svg width="12" height="12" viewBox="0 0 11.199999809265137 11.199999809265137" class="cursor-pointer flex items-center tongyi-design-highlighter-copy-btn"><g><path d="M11.2,1.6C11.2,0.716344,10.4837,0,9.6,0L4.8,0C3.91634,0,3.2,0.716344,3.2,1.6L4.16,1.6Q4.16,1.3349,4.34745,1.14745Q4.5349,0.96,4.8,0.96L9.6,0.96Q9.8651,0.96,10.0525,1.14745Q10.24,1.3349,10.24,1.6L10.24,6.4Q10.24,6.6651,10.0525,6.85255Q9.8651,7.04,9.6,7.04L9.6,8C10.4837,8,11.2,7.28366,11.2,6.4L11.2,1.6ZM0,4L0,9.6C0,10.4837,0.716344,11.2,1.6,11.2L7.2,11.2C8.08366,11.2,8.8,10.4837,8.8,9.6L8.8,4C8.8,3.11634,8.08366,2.4,7.2,2.4L1.6,2.4C0.716344,2.4,0,3.11634,0,4ZM1.14745,10.0525Q0.96,9.8651,0.96,9.6L0.96,4Q0.96,3.7349,1.14745,3.54745Q1.3349,3.36,1.6,3.36L7.2,3.36Q7.4651,3.36,7.65255,3.54745Q7.84,3.7349,7.84,4L7.84,9.6Q7.84,9.8651,7.65255,10.0525Q7.4651,10.24,7.2,10.24L1.6,10.24Q1.3349,10.24,1.14745,10.0525Z"></path></g></svg></div></span><div><pre style="display: block; overflow-x: auto; padding: 16px 8px; background: rgb(30, 30, 30); color: rgb(221, 221, 221); margin: 0px; font-size: 13px;"><code style="white-space: pre; background-color: transparent;"><span class="comment linenumber react-syntax-highlighter-line-number" style="display: inline-block; min-width: 1.25em; padding-right: 20px; text-align: right; user-select: none; color: rgb(133, 133, 133); font-size: 13px;">1</span><span>.
</span><span class="comment linenumber react-syntax-highlighter-line-number" style="display: inline-block; min-width: 1.25em; padding-right: 20px; text-align: right; user-select: none; color: rgb(133, 133, 133); font-size: 13px;">2</span><span>├── Button.py              </span><span style="color: rgb(119, 119, 119);"># 按钮类核心实现</span><span>
</span><span class="comment linenumber react-syntax-highlighter-line-number" style="display: inline-block; min-width: 1.25em; padding-right: 20px; text-align: right; user-select: none; color: rgb(133, 133, 133); font-size: 13px;">3</span><span>└── test_button.py         </span><span style="color: rgb(119, 119, 119);"># 示例代码演示</span></code></pre></div></div></pre>
<hr>
<h2>✨ 功能特性</h2>
<h3>1. 基础按钮 (<code node="[object Object]">Button</code>)</h3>
<ul>
<li>点击时边框颜色变化</li>
<li>鼠标悬停时背景颜色变化</li>
<li>支持布尔状态切换（如开关按钮）</li>
</ul>
<h3>2. 文本按钮 (<code node="[object Object]">TextButton</code>)</h3>
<ul>
<li>继承自 <code node="[object Object]">Button</code></li>
<li>显示文本，支持多状态文本切换</li>
<li>自定义字体、字体大小、文字颜色、背景颜色</li>
</ul>
<h3>3. 图片按钮 (<code node="[object Object]">ImageButton</code>)</h3>
<ul>
<li>继承自 <code node="[object Object]">Button</code></li>
<li>显示图片，支持多状态图片切换</li>
<li>自动处理图片加载失败情况，显示占位符</li>
</ul>
<h3>4. 输入框按钮 (<code node="[object Object]">InputButton</code>)</h3>
<ul>
<li>继承自 <code node="[object Object]">Button</code></li>
<li>提供可输入文本区域</li>
<li>支持键盘输入（退格、删除、光标移动）</li>
<li>光标闪烁动画</li>
<li>激活状态管理（仅激活状态下可输入）</li>
</ul>
<hr>
<h2>🛠️ 使用指南</h2>
<h3>1. 安装依赖</h3>
<p>确保你已安装 Pygame：</p>
<pre><div class="tongyi-design-highlighter global-dark-theme"><span class="tongyi-design-highlighter-header" style="background-color: rgb(44, 44, 54);"><span class="tongyi-design-highlighter-lang">bash</span><div class="tongyi-design-highlighter-right-actions"><div class="tongyi-design-highlighter-theme-changer"><div class="tongyi-design-highlighter-theme-changer-btn"><span>深色版本</span><span role="img" class="anticon"><svg width="1em" height="1em" fill="currentColor" aria-hidden="true" focusable="false" class=""><use xlink:href="#tongyi-down-line"></use></svg></span></div></div><svg width="12" height="12" viewBox="0 0 11.199999809265137 11.199999809265137" class="cursor-pointer flex items-center tongyi-design-highlighter-copy-btn"><g><path d="M11.2,1.6C11.2,0.716344,10.4837,0,9.6,0L4.8,0C3.91634,0,3.2,0.716344,3.2,1.6L4.16,1.6Q4.16,1.3349,4.34745,1.14745Q4.5349,0.96,4.8,0.96L9.6,0.96Q9.8651,0.96,10.0525,1.14745Q10.24,1.3349,10.24,1.6L10.24,6.4Q10.24,6.6651,10.0525,6.85255Q9.8651,7.04,9.6,7.04L9.6,8C10.4837,8,11.2,7.28366,11.2,6.4L11.2,1.6ZM0,4L0,9.6C0,10.4837,0.716344,11.2,1.6,11.2L7.2,11.2C8.08366,11.2,8.8,10.4837,8.8,9.6L8.8,4C8.8,3.11634,8.08366,2.4,7.2,2.4L1.6,2.4C0.716344,2.4,0,3.11634,0,4ZM1.14745,10.0525Q0.96,9.8651,0.96,9.6L0.96,4Q0.96,3.7349,1.14745,3.54745Q1.3349,3.36,1.6,3.36L7.2,3.36Q7.4651,3.36,7.65255,3.54745Q7.84,3.7349,7.84,4L7.84,9.6Q7.84,9.8651,7.65255,10.0525Q7.4651,10.24,7.2,10.24L1.6,10.24Q1.3349,10.24,1.14745,10.0525Z"></path></g></svg></div></span><div><pre style="display: block; overflow-x: auto; padding: 16px 8px; background: rgb(30, 30, 30); color: rgb(221, 221, 221); margin: 0px; font-size: 13px;"><code style="white-space: pre; background-color: transparent;"><span class="comment linenumber react-syntax-highlighter-line-number" style="display: inline-block; min-width: 1.25em; padding-right: 20px; text-align: right; user-select: none; color: rgb(133, 133, 133); font-size: 13px;">1</span><span>pip install pygame</span></code></pre></div></div></pre>
<h3>2. 运行示例</h3>
<p>运行示例程序查看按钮模块的实际效果：</p>
<pre><div class="tongyi-design-highlighter global-dark-theme"><span class="tongyi-design-highlighter-header" style="background-color: rgb(44, 44, 54);"><span class="tongyi-design-highlighter-lang">bash</span><div class="tongyi-design-highlighter-right-actions"><div class="tongyi-design-highlighter-theme-changer"><div class="tongyi-design-highlighter-theme-changer-btn"><span>深色版本</span><span role="img" class="anticon"><svg width="1em" height="1em" fill="currentColor" aria-hidden="true" focusable="false" class=""><use xlink:href="#tongyi-down-line"></use></svg></span></div></div><svg width="12" height="12" viewBox="0 0 11.199999809265137 11.199999809265137" class="cursor-pointer flex items-center tongyi-design-highlighter-copy-btn"><g><path d="M11.2,1.6C11.2,0.716344,10.4837,0,9.6,0L4.8,0C3.91634,0,3.2,0.716344,3.2,1.6L4.16,1.6Q4.16,1.3349,4.34745,1.14745Q4.5349,0.96,4.8,0.96L9.6,0.96Q9.8651,0.96,10.0525,1.14745Q10.24,1.3349,10.24,1.6L10.24,6.4Q10.24,6.6651,10.0525,6.85255Q9.8651,7.04,9.6,7.04L9.6,8C10.4837,8,11.2,7.28366,11.2,6.4L11.2,1.6ZM0,4L0,9.6C0,10.4837,0.716344,11.2,1.6,11.2L7.2,11.2C8.08366,11.2,8.8,10.4837,8.8,9.6L8.8,4C8.8,3.11634,8.08366,2.4,7.2,2.4L1.6,2.4C0.716344,2.4,0,3.11634,0,4ZM1.14745,10.0525Q0.96,9.8651,0.96,9.6L0.96,4Q0.96,3.7349,1.14745,3.54745Q1.3349,3.36,1.6,3.36L7.2,3.36Q7.4651,3.36,7.65255,3.54745Q7.84,3.7349,7.84,4L7.84,9.6Q7.84,9.8651,7.65255,10.0525Q7.4651,10.24,7.2,10.24L1.6,10.24Q1.3349,10.24,1.14745,10.0525Z"></path></g></svg></div></span><div><pre style="display: block; overflow-x: auto; padding: 16px 8px; background: rgb(30, 30, 30); color: rgb(221, 221, 221); margin: 0px; font-size: 13px;"><code style="white-space: pre; background-color: transparent;"><span class="comment linenumber react-syntax-highlighter-line-number" style="display: inline-block; min-width: 1.25em; padding-right: 20px; text-align: right; user-select: none; color: rgb(133, 133, 133); font-size: 13px;">1</span><span>python test_button.py</span></code></pre></div></div></pre>
<p>📌 注意：</p>
<ul>
<li>示例会检查是否存在 <code node="[object Object]">font.ttf</code> 和 <code node="[object Object]">test.png</code>。</li>
<li>如果文件不存在，会打印警告并尝试使用默认字体或创建占位图。</li>
<li>推荐提供真实资源以获得最佳效果。</li>
</ul>
<h3>3. 在项目中使用</h3>
<p>导入模块并创建按钮实例：</p>
<pre><div class="tongyi-design-highlighter global-dark-theme"><span class="tongyi-design-highlighter-header" style="background-color: rgb(44, 44, 54);"><span class="tongyi-design-highlighter-lang">python</span><div class="tongyi-design-highlighter-right-actions"><div class="tongyi-design-highlighter-theme-changer"><div class="tongyi-design-highlighter-theme-changer-btn"><span>深色版本</span><span role="img" class="anticon"><svg width="1em" height="1em" fill="currentColor" aria-hidden="true" focusable="false" class=""><use xlink:href="#tongyi-down-line"></use></svg></span></div></div><svg width="12" height="12" viewBox="0 0 11.199999809265137 11.199999809265137" class="cursor-pointer flex items-center tongyi-design-highlighter-copy-btn"><g><path d="M11.2,1.6C11.2,0.716344,10.4837,0,9.6,0L4.8,0C3.91634,0,3.2,0.716344,3.2,1.6L4.16,1.6Q4.16,1.3349,4.34745,1.14745Q4.5349,0.96,4.8,0.96L9.6,0.96Q9.8651,0.96,10.0525,1.14745Q10.24,1.3349,10.24,1.6L10.24,6.4Q10.24,6.6651,10.0525,6.85255Q9.8651,7.04,9.6,7.04L9.6,8C10.4837,8,11.2,7.28366,11.2,6.4L11.2,1.6ZM0,4L0,9.6C0,10.4837,0.716344,11.2,1.6,11.2L7.2,11.2C8.08366,11.2,8.8,10.4837,8.8,9.6L8.8,4C8.8,3.11634,8.08366,2.4,7.2,2.4L1.6,2.4C0.716344,2.4,0,3.11634,0,4ZM1.14745,10.0525Q0.96,9.8651,0.96,9.6L0.96,4Q0.96,3.7349,1.14745,3.54745Q1.3349,3.36,1.6,3.36L7.2,3.36Q7.4651,3.36,7.65255,3.54745Q7.84,3.7349,7.84,4L7.84,9.6Q7.84,9.8651,7.65255,10.0525Q7.4651,10.24,7.2,10.24L1.6,10.24Q1.3349,10.24,1.14745,10.0525Z"></path></g></svg></div></span><div><pre style="display: block; overflow-x: auto; padding: 16px 8px; background: rgb(30, 30, 30); color: rgb(221, 221, 221); margin: 0px; font-size: 13px;"><code style="white-space: pre; background-color: transparent;"><span class="comment linenumber react-syntax-highlighter-line-number" style="display: inline-block; min-width: 2.25em; padding-right: 20px; text-align: right; user-select: none; color: rgb(133, 133, 133); font-size: 13px;">1</span><span style="color: white; font-weight: bold;">import</span><span> pygame
</span><span class="comment linenumber react-syntax-highlighter-line-number" style="display: inline-block; min-width: 2.25em; padding-right: 20px; text-align: right; user-select: none; color: rgb(133, 133, 133); font-size: 13px;">2</span><span></span><span style="color: white; font-weight: bold;">from</span><span> Button </span><span style="color: white; font-weight: bold;">import</span><span> Button, TextButton, ImageButton, InputButton, COLOR_BLACK, COLOR_WHITE
</span><span class="comment linenumber react-syntax-highlighter-line-number" style="display: inline-block; min-width: 2.25em; padding-right: 20px; text-align: right; user-select: none; color: rgb(133, 133, 133); font-size: 13px;">3</span>
<span class="comment linenumber react-syntax-highlighter-line-number" style="display: inline-block; min-width: 2.25em; padding-right: 20px; text-align: right; user-select: none; color: rgb(133, 133, 133); font-size: 13px;">4</span>pygame.init()
<span class="comment linenumber react-syntax-highlighter-line-number" style="display: inline-block; min-width: 2.25em; padding-right: 20px; text-align: right; user-select: none; color: rgb(133, 133, 133); font-size: 13px;">5</span><span>screen = pygame.display.set_mode((</span><span class="hljs-number">800</span><span>, </span><span class="hljs-number">600</span><span>))
</span><span class="comment linenumber react-syntax-highlighter-line-number" style="display: inline-block; min-width: 2.25em; padding-right: 20px; text-align: right; user-select: none; color: rgb(133, 133, 133); font-size: 13px;">6</span><span>pygame.display.set_caption(</span><span style="color: rgb(221, 136, 136);">"我的 Pygame 应用"</span><span>)
</span><span class="comment linenumber react-syntax-highlighter-line-number" style="display: inline-block; min-width: 2.25em; padding-right: 20px; text-align: right; user-select: none; color: rgb(133, 133, 133); font-size: 13px;">7</span>
<span class="comment linenumber react-syntax-highlighter-line-number" style="display: inline-block; min-width: 2.25em; padding-right: 20px; text-align: right; user-select: none; color: rgb(133, 133, 133); font-size: 13px;">8</span><span></span><span style="color: rgb(119, 119, 119);"># 创建一个文本按钮</span><span>
</span><span class="comment linenumber react-syntax-highlighter-line-number" style="display: inline-block; min-width: 2.25em; padding-right: 20px; text-align: right; user-select: none; color: rgb(133, 133, 133); font-size: 13px;">9</span>my_text_button = TextButton(
<span class="comment linenumber react-syntax-highlighter-line-number" style="display: inline-block; min-width: 2.25em; padding-right: 20px; text-align: right; user-select: none; color: rgb(133, 133, 133); font-size: 13px;">10</span><span>    xy=[</span><span class="hljs-number">100</span><span>, </span><span class="hljs-number">100</span><span>],
</span><span class="comment linenumber react-syntax-highlighter-line-number" style="display: inline-block; min-width: 2.25em; padding-right: 20px; text-align: right; user-select: none; color: rgb(133, 133, 133); font-size: 13px;">11</span><span>    size=[</span><span class="hljs-number">150</span><span>, </span><span class="hljs-number">50</span><span>],
</span><span class="comment linenumber react-syntax-highlighter-line-number" style="display: inline-block; min-width: 2.25em; padding-right: 20px; text-align: right; user-select: none; color: rgb(133, 133, 133); font-size: 13px;">12</span><span>    texts=[</span><span style="color: rgb(221, 136, 136);">'开始游戏'</span><span>, </span><span style="color: rgb(221, 136, 136);">'游戏中...'</span><span>],
</span><span class="comment linenumber react-syntax-highlighter-line-number" style="display: inline-block; min-width: 2.25em; padding-right: 20px; text-align: right; user-select: none; color: rgb(133, 133, 133); font-size: 13px;">13</span><span>    font_path=</span><span style="color: rgb(221, 136, 136);">'font.ttf'</span><span>,
</span><span class="comment linenumber react-syntax-highlighter-line-number" style="display: inline-block; min-width: 2.25em; padding-right: 20px; text-align: right; user-select: none; color: rgb(133, 133, 133); font-size: 13px;">14</span><span>    font_size=</span><span class="hljs-number">30</span><span>,
</span><span class="comment linenumber react-syntax-highlighter-line-number" style="display: inline-block; min-width: 2.25em; padding-right: 20px; text-align: right; user-select: none; color: rgb(133, 133, 133); font-size: 13px;">15</span>    text_color=COLOR_BLACK,
<span class="comment linenumber react-syntax-highlighter-line-number" style="display: inline-block; min-width: 2.25em; padding-right: 20px; text-align: right; user-select: none; color: rgb(133, 133, 133); font-size: 13px;">16</span>    bg_color=COLOR_WHITE
<span class="comment linenumber react-syntax-highlighter-line-number" style="display: inline-block; min-width: 2.25em; padding-right: 20px; text-align: right; user-select: none; color: rgb(133, 133, 133); font-size: 13px;">17</span>)
<span class="comment linenumber react-syntax-highlighter-line-number" style="display: inline-block; min-width: 2.25em; padding-right: 20px; text-align: right; user-select: none; color: rgb(133, 133, 133); font-size: 13px;">18</span>
<span class="comment linenumber react-syntax-highlighter-line-number" style="display: inline-block; min-width: 2.25em; padding-right: 20px; text-align: right; user-select: none; color: rgb(133, 133, 133); font-size: 13px;">19</span><span></span><span style="color: rgb(119, 119, 119);"># 创建一个输入框按钮</span><span>
</span><span class="comment linenumber react-syntax-highlighter-line-number" style="display: inline-block; min-width: 2.25em; padding-right: 20px; text-align: right; user-select: none; color: rgb(133, 133, 133); font-size: 13px;">20</span>my_input_button = InputButton(
<span class="comment linenumber react-syntax-highlighter-line-number" style="display: inline-block; min-width: 2.25em; padding-right: 20px; text-align: right; user-select: none; color: rgb(133, 133, 133); font-size: 13px;">21</span><span>    xy=[</span><span class="hljs-number">100</span><span>, </span><span class="hljs-number">200</span><span>],
</span><span class="comment linenumber react-syntax-highlighter-line-number" style="display: inline-block; min-width: 2.25em; padding-right: 20px; text-align: right; user-select: none; color: rgb(133, 133, 133); font-size: 13px;">22</span><span>    size=[</span><span class="hljs-number">300</span><span>, </span><span class="hljs-number">50</span><span>],
</span><span class="comment linenumber react-syntax-highlighter-line-number" style="display: inline-block; min-width: 2.25em; padding-right: 20px; text-align: right; user-select: none; color: rgb(133, 133, 133); font-size: 13px;">23</span><span>    initial_text=</span><span style="color: rgb(221, 136, 136);">'输入您的名字'</span><span>
</span><span class="comment linenumber react-syntax-highlighter-line-number" style="display: inline-block; min-width: 2.25em; padding-right: 20px; text-align: right; user-select: none; color: rgb(133, 133, 133); font-size: 13px;">24</span>)
<span class="comment linenumber react-syntax-highlighter-line-number" style="display: inline-block; min-width: 2.25em; padding-right: 20px; text-align: right; user-select: none; color: rgb(133, 133, 133); font-size: 13px;">25</span>
<span class="comment linenumber react-syntax-highlighter-line-number" style="display: inline-block; min-width: 2.25em; padding-right: 20px; text-align: right; user-select: none; color: rgb(133, 133, 133); font-size: 13px;">26</span><span>running = </span><span style="color: white; font-weight: bold;">True</span><span>
</span><span class="comment linenumber react-syntax-highlighter-line-number" style="display: inline-block; min-width: 2.25em; padding-right: 20px; text-align: right; user-select: none; color: rgb(133, 133, 133); font-size: 13px;">27</span><span></span><span style="color: white; font-weight: bold;">while</span><span> running:
</span><span class="comment linenumber react-syntax-highlighter-line-number" style="display: inline-block; min-width: 2.25em; padding-right: 20px; text-align: right; user-select: none; color: rgb(133, 133, 133); font-size: 13px;">28</span><span>    </span><span style="color: white; font-weight: bold;">for</span><span> event </span><span style="color: white; font-weight: bold;">in</span><span> pygame.event.get():
</span><span class="comment linenumber react-syntax-highlighter-line-number" style="display: inline-block; min-width: 2.25em; padding-right: 20px; text-align: right; user-select: none; color: rgb(133, 133, 133); font-size: 13px;">29</span><span>        </span><span style="color: white; font-weight: bold;">if</span><span> event.</span><span style="color: rgb(221, 136, 136);">type</span><span> == pygame.QUIT:
</span><span class="comment linenumber react-syntax-highlighter-line-number" style="display: inline-block; min-width: 2.25em; padding-right: 20px; text-align: right; user-select: none; color: rgb(133, 133, 133); font-size: 13px;">30</span><span>            running = </span><span style="color: white; font-weight: bold;">False</span><span>
</span><span class="comment linenumber react-syntax-highlighter-line-number" style="display: inline-block; min-width: 2.25em; padding-right: 20px; text-align: right; user-select: none; color: rgb(133, 133, 133); font-size: 13px;">31</span>        my_input_button.handle_input_event(event)
<span class="comment linenumber react-syntax-highlighter-line-number" style="display: inline-block; min-width: 2.25em; padding-right: 20px; text-align: right; user-select: none; color: rgb(133, 133, 133); font-size: 13px;">32</span>
<span class="comment linenumber react-syntax-highlighter-line-number" style="display: inline-block; min-width: 2.25em; padding-right: 20px; text-align: right; user-select: none; color: rgb(133, 133, 133); font-size: 13px;">33</span><span>    screen.fill((</span><span class="hljs-number">200</span><span>, </span><span class="hljs-number">200</span><span>, </span><span class="hljs-number">200</span><span>))  </span><span style="color: rgb(119, 119, 119);"># 背景填充色</span><span>
</span><span class="comment linenumber react-syntax-highlighter-line-number" style="display: inline-block; min-width: 2.25em; padding-right: 20px; text-align: right; user-select: none; color: rgb(133, 133, 133); font-size: 13px;">34</span>
<span class="comment linenumber react-syntax-highlighter-line-number" style="display: inline-block; min-width: 2.25em; padding-right: 20px; text-align: right; user-select: none; color: rgb(133, 133, 133); font-size: 13px;">35</span>    my_text_button.draw(screen)
<span class="comment linenumber react-syntax-highlighter-line-number" style="display: inline-block; min-width: 2.25em; padding-right: 20px; text-align: right; user-select: none; color: rgb(133, 133, 133); font-size: 13px;">36</span>    my_input_button.draw(screen)
<span class="comment linenumber react-syntax-highlighter-line-number" style="display: inline-block; min-width: 2.25em; padding-right: 20px; text-align: right; user-select: none; color: rgb(133, 133, 133); font-size: 13px;">37</span>
<span class="comment linenumber react-syntax-highlighter-line-number" style="display: inline-block; min-width: 2.25em; padding-right: 20px; text-align: right; user-select: none; color: rgb(133, 133, 133); font-size: 13px;">38</span>    pygame.display.update()
<span class="comment linenumber react-syntax-highlighter-line-number" style="display: inline-block; min-width: 2.25em; padding-right: 20px; text-align: right; user-select: none; color: rgb(133, 133, 133); font-size: 13px;">39</span>
<span class="comment linenumber react-syntax-highlighter-line-number" style="display: inline-block; min-width: 2.25em; padding-right: 20px; text-align: right; user-select: none; color: rgb(133, 133, 133); font-size: 13px;">40</span>pygame.quit()</code></pre></div></div></pre>
<hr>
<h2>🧱 类与方法详解</h2>
<h3><code node="[object Object]">Button</code>（基础按钮）</h3>
<h4>初始化参数：</h4>
<pre><div class="tongyi-design-highlighter global-dark-theme"><span class="tongyi-design-highlighter-header" style="background-color: rgb(44, 44, 54);"><span class="tongyi-design-highlighter-lang">python</span><div class="tongyi-design-highlighter-right-actions"><div class="tongyi-design-highlighter-theme-changer"><div class="tongyi-design-highlighter-theme-changer-btn"><span>深色版本</span><span role="img" class="anticon"><svg width="1em" height="1em" fill="currentColor" aria-hidden="true" focusable="false" class=""><use xlink:href="#tongyi-down-line"></use></svg></span></div></div><svg width="12" height="12" viewBox="0 0 11.199999809265137 11.199999809265137" class="cursor-pointer flex items-center tongyi-design-highlighter-copy-btn"><g><path d="M11.2,1.6C11.2,0.716344,10.4837,0,9.6,0L4.8,0C3.91634,0,3.2,0.716344,3.2,1.6L4.16,1.6Q4.16,1.3349,4.34745,1.14745Q4.5349,0.96,4.8,0.96L9.6,0.96Q9.8651,0.96,10.0525,1.14745Q10.24,1.3349,10.24,1.6L10.24,6.4Q10.24,6.6651,10.0525,6.85255Q9.8651,7.04,9.6,7.04L9.6,8C10.4837,8,11.2,7.28366,11.2,6.4L11.2,1.6ZM0,4L0,9.6C0,10.4837,0.716344,11.2,1.6,11.2L7.2,11.2C8.08366,11.2,8.8,10.4837,8.8,9.6L8.8,4C8.8,3.11634,8.08366,2.4,7.2,2.4L1.6,2.4C0.716344,2.4,0,3.11634,0,4ZM1.14745,10.0525Q0.96,9.8651,0.96,9.6L0.96,4Q0.96,3.7349,1.14745,3.54745Q1.3349,3.36,1.6,3.36L7.2,3.36Q7.4651,3.36,7.65255,3.54745Q7.84,3.7349,7.84,4L7.84,9.6Q7.84,9.8651,7.65255,10.0525Q7.4651,10.24,7.2,10.24L1.6,10.24Q1.3349,10.24,1.14745,10.0525Z"></path></g></svg></div></span><div><pre style="display: block; overflow-x: auto; padding: 16px 8px; background: rgb(30, 30, 30); color: rgb(221, 221, 221); margin: 0px; font-size: 13px;"><code style="white-space: pre; background-color: transparent;"><span class="comment linenumber react-syntax-highlighter-line-number" style="display: inline-block; min-width: 1.25em; padding-right: 20px; text-align: right; user-select: none; color: rgb(133, 133, 133); font-size: 13px;">1</span><span>Button(xy, size, frame_color=(COLOR_PINK, COLOR_LIGHT_BLUE))</span></code></pre></div></div></pre>

























<table><thead><tr><th>参数名</th><th>类型</th><th>描述</th></tr></thead><tbody><tr><td><code node="[object Object]">xy</code></td><td><code node="[object Object]">(int, int)</code></td><td>按钮左上角坐标 (x, y)</td></tr><tr><td><code node="[object Object]">size</code></td><td><code node="[object Object]">(int, int)</code></td><td>按钮尺寸 (width, height)</td></tr><tr><td><code node="[object Object]">frame_color</code></td><td><code node="[object Object]">(color, color)</code></td><td>边框颜色：(点击时颜色, 默认/悬停颜色)</td></tr></tbody></table>
<h4>方法：</h4>





















<table><thead><tr><th>方法</th><th>描述</th></tr></thead><tbody><tr><td><code node="[object Object]">draw(screen, custom_frame_draw_func=None)</code></td><td>绘制按钮</td></tr><tr><td><code node="[object Object]">get_state()</code></td><td>获取当前状态（True/False）</td></tr><tr><td><code node="[object Object]">toggle_state()</code></td><td>切换状态</td></tr></tbody></table>
<hr>
<h3><code node="[object Object]">TextButton</code>（文本按钮）</h3>
<h4>初始化参数：</h4>
<pre><div class="tongyi-design-highlighter global-dark-theme"><span class="tongyi-design-highlighter-header" style="background-color: rgb(44, 44, 54);"><span class="tongyi-design-highlighter-lang">python</span><div class="tongyi-design-highlighter-right-actions"><div class="tongyi-design-highlighter-theme-changer"><div class="tongyi-design-highlighter-theme-changer-btn"><span>深色版本</span><span role="img" class="anticon"><svg width="1em" height="1em" fill="currentColor" aria-hidden="true" focusable="false" class=""><use xlink:href="#tongyi-down-line"></use></svg></span></div></div><svg width="12" height="12" viewBox="0 0 11.199999809265137 11.199999809265137" class="cursor-pointer flex items-center tongyi-design-highlighter-copy-btn"><g><path d="M11.2,1.6C11.2,0.716344,10.4837,0,9.6,0L4.8,0C3.91634,0,3.2,0.716344,3.2,1.6L4.16,1.6Q4.16,1.3349,4.34745,1.14745Q4.5349,0.96,4.8,0.96L9.6,0.96Q9.8651,0.96,10.0525,1.14745Q10.24,1.3349,10.24,1.6L10.24,6.4Q10.24,6.6651,10.0525,6.85255Q9.8651,7.04,9.6,7.04L9.6,8C10.4837,8,11.2,7.28366,11.2,6.4L11.2,1.6ZM0,4L0,9.6C0,10.4837,0.716344,11.2,1.6,11.2L7.2,11.2C8.08366,11.2,8.8,10.4837,8.8,9.6L8.8,4C8.8,3.11634,8.08366,2.4,7.2,2.4L1.6,2.4C0.716344,2.4,0,3.11634,0,4ZM1.14745,10.0525Q0.96,9.8651,0.96,9.6L0.96,4Q0.96,3.7349,1.14745,3.54745Q1.3349,3.36,1.6,3.36L7.2,3.36Q7.4651,3.36,7.65255,3.54745Q7.84,3.7349,7.84,4L7.84,9.6Q7.84,9.8651,7.65255,10.0525Q7.4651,10.24,7.2,10.24L1.6,10.24Q1.3349,10.24,1.14745,10.0525Z"></path></g></svg></div></span><div><pre style="display: block; overflow-x: auto; padding: 16px 8px; background: rgb(30, 30, 30); color: rgb(221, 221, 221); margin: 0px; font-size: 13px;"><code style="white-space: pre; background-color: transparent;"><span class="comment linenumber react-syntax-highlighter-line-number" style="display: inline-block; min-width: 1.25em; padding-right: 20px; text-align: right; user-select: none; color: rgb(133, 133, 133); font-size: 13px;">1</span><span>TextButton(xy, size, texts, font_path, font_size, text_color=COLOR_BLACK, bg_color=</span><span style="color: white; font-weight: bold;">None</span><span>)</span></code></pre></div></div></pre>



































<table><thead><tr><th>参数名</th><th>类型</th><th>描述</th></tr></thead><tbody><tr><td><code node="[object Object]">texts</code></td><td><code node="[object Object]">list[str]</code></td><td>多状态文本列表</td></tr><tr><td><code node="[object Object]">font_path</code></td><td><code node="[object Object]">str</code></td><td>字体文件路径</td></tr><tr><td><code node="[object Object]">font_size</code></td><td><code node="[object Object]">int</code></td><td>字号大小</td></tr><tr><td><code node="[object Object]">text_color</code></td><td><code node="[object Object]">color</code></td><td>文字颜色</td></tr><tr><td><code node="[object Object]">bg_color</code></td><td><code node="[object Object]">color or None</code></td><td>背景色（可选）</td></tr></tbody></table>
<hr>
<h3><code node="[object Object]">ImageButton</code>（图片按钮）</h3>
<h4>初始化参数：</h4>
<pre><div class="tongyi-design-highlighter global-dark-theme"><span class="tongyi-design-highlighter-header" style="background-color: rgb(44, 44, 54);"><span class="tongyi-design-highlighter-lang">python</span><div class="tongyi-design-highlighter-right-actions"><div class="tongyi-design-highlighter-theme-changer"><div class="tongyi-design-highlighter-theme-changer-btn"><span>深色版本</span><span role="img" class="anticon"><svg width="1em" height="1em" fill="currentColor" aria-hidden="true" focusable="false" class=""><use xlink:href="#tongyi-down-line"></use></svg></span></div></div><svg width="12" height="12" viewBox="0 0 11.199999809265137 11.199999809265137" class="cursor-pointer flex items-center tongyi-design-highlighter-copy-btn"><g><path d="M11.2,1.6C11.2,0.716344,10.4837,0,9.6,0L4.8,0C3.91634,0,3.2,0.716344,3.2,1.6L4.16,1.6Q4.16,1.3349,4.34745,1.14745Q4.5349,0.96,4.8,0.96L9.6,0.96Q9.8651,0.96,10.0525,1.14745Q10.24,1.3349,10.24,1.6L10.24,6.4Q10.24,6.6651,10.0525,6.85255Q9.8651,7.04,9.6,7.04L9.6,8C10.4837,8,11.2,7.28366,11.2,6.4L11.2,1.6ZM0,4L0,9.6C0,10.4837,0.716344,11.2,1.6,11.2L7.2,11.2C8.08366,11.2,8.8,10.4837,8.8,9.6L8.8,4C8.8,3.11634,8.08366,2.4,7.2,2.4L1.6,2.4C0.716344,2.4,0,3.11634,0,4ZM1.14745,10.0525Q0.96,9.8651,0.96,9.6L0.96,4Q0.96,3.7349,1.14745,3.54745Q1.3349,3.36,1.6,3.36L7.2,3.36Q7.4651,3.36,7.65255,3.54745Q7.84,3.7349,7.84,4L7.84,9.6Q7.84,9.8651,7.65255,10.0525Q7.4651,10.24,7.2,10.24L1.6,10.24Q1.3349,10.24,1.14745,10.0525Z"></path></g></svg></div></span><div><pre style="display: block; overflow-x: auto; padding: 16px 8px; background: rgb(30, 30, 30); color: rgb(221, 221, 221); margin: 0px; font-size: 13px;"><code style="white-space: pre; background-color: transparent;"><span class="comment linenumber react-syntax-highlighter-line-number" style="display: inline-block; min-width: 1.25em; padding-right: 20px; text-align: right; user-select: none; color: rgb(133, 133, 133); font-size: 13px;">1</span><span>ImageButton(xy, size, image_paths, img_size)</span></code></pre></div></div></pre>




















<table><thead><tr><th>参数名</th><th>类型</th><th>描述</th></tr></thead><tbody><tr><td><code node="[object Object]">image_paths</code></td><td><code node="[object Object]">list[str]</code></td><td>多状态图片路径列表</td></tr><tr><td><code node="[object Object]">img_size</code></td><td><code node="[object Object]">(int, int)</code></td><td>图片缩放尺寸</td></tr></tbody></table>
<hr>
<h3><code node="[object Object]">InputButton</code>（输入框按钮）</h3>
<h4>初始化参数：</h4>
<pre><div class="tongyi-design-highlighter global-dark-theme"><span class="tongyi-design-highlighter-header" style="background-color: rgb(44, 44, 54);"><span class="tongyi-design-highlighter-lang">python</span><div class="tongyi-design-highlighter-right-actions"><div class="tongyi-design-highlighter-theme-changer"><div class="tongyi-design-highlighter-theme-changer-btn"><span>深色版本</span><span role="img" class="anticon"><svg width="1em" height="1em" fill="currentColor" aria-hidden="true" focusable="false" class=""><use xlink:href="#tongyi-down-line"></use></svg></span></div></div><svg width="12" height="12" viewBox="0 0 11.199999809265137 11.199999809265137" class="cursor-pointer flex items-center tongyi-design-highlighter-copy-btn"><g><path d="M11.2,1.6C11.2,0.716344,10.4837,0,9.6,0L4.8,0C3.91634,0,3.2,0.716344,3.2,1.6L4.16,1.6Q4.16,1.3349,4.34745,1.14745Q4.5349,0.96,4.8,0.96L9.6,0.96Q9.8651,0.96,10.0525,1.14745Q10.24,1.3349,10.24,1.6L10.24,6.4Q10.24,6.6651,10.0525,6.85255Q9.8651,7.04,9.6,7.04L9.6,8C10.4837,8,11.2,7.28366,11.2,6.4L11.2,1.6ZM0,4L0,9.6C0,10.4837,0.716344,11.2,1.6,11.2L7.2,11.2C8.08366,11.2,8.8,10.4837,8.8,9.6L8.8,4C8.8,3.11634,8.08366,2.4,7.2,2.4L1.6,2.4C0.716344,2.4,0,3.11634,0,4ZM1.14745,10.0525Q0.96,9.8651,0.96,9.6L0.96,4Q0.96,3.7349,1.14745,3.54745Q1.3349,3.36,1.6,3.36L7.2,3.36Q7.4651,3.36,7.65255,3.54745Q7.84,3.7349,7.84,4L7.84,9.6Q7.84,9.8651,7.65255,10.0525Q7.4651,10.24,7.2,10.24L1.6,10.24Q1.3349,10.24,1.14745,10.0525Z"></path></g></svg></div></span><div><pre style="display: block; overflow-x: auto; padding: 16px 8px; background: rgb(30, 30, 30); color: rgb(221, 221, 221); margin: 0px; font-size: 13px;"><code style="white-space: pre; background-color: transparent;"><span class="comment linenumber react-syntax-highlighter-line-number" style="display: inline-block; min-width: 1.25em; padding-right: 20px; text-align: right; user-select: none; color: rgb(133, 133, 133); font-size: 13px;">1</span><span>InputButton(xy, size, initial_text=</span><span style="color: rgb(221, 136, 136);">''</span><span>, cursor_blink_rate=</span><span class="hljs-number">15</span><span>)</span></code></pre></div></div></pre>




















<table><thead><tr><th>参数名</th><th>类型</th><th>描述</th></tr></thead><tbody><tr><td><code node="[object Object]">initial_text</code></td><td><code node="[object Object]">str</code></td><td>初始文本</td></tr><tr><td><code node="[object Object]">cursor_blink_rate</code></td><td><code node="[object Object]">int</code></td><td>光标闪烁频率（帧数）</td></tr></tbody></table>
<h4>方法：</h4>

















<table><thead><tr><th>方法</th><th>描述</th></tr></thead><tbody><tr><td><code node="[object Object]">handle_input_event(event)</code></td><td>处理键盘事件</td></tr><tr><td><code node="[object Object]">get_text()</code></td><td>获取当前输入内容</td></tr></tbody></table>
<hr>
<h2>🎨 颜色常量定义</h2>
<p>在 <code node="[object Object]">Button.py</code> 中预设了一些常用颜色：</p>
<pre><div class="tongyi-design-highlighter global-dark-theme"><span class="tongyi-design-highlighter-header" style="background-color: rgb(44, 44, 54);"><span class="tongyi-design-highlighter-lang">python</span><div class="tongyi-design-highlighter-right-actions"><div class="tongyi-design-highlighter-theme-changer"><div class="tongyi-design-highlighter-theme-changer-btn"><span>深色版本</span><span role="img" class="anticon"><svg width="1em" height="1em" fill="currentColor" aria-hidden="true" focusable="false" class=""><use xlink:href="#tongyi-down-line"></use></svg></span></div></div><svg width="12" height="12" viewBox="0 0 11.199999809265137 11.199999809265137" class="cursor-pointer flex items-center tongyi-design-highlighter-copy-btn"><g><path d="M11.2,1.6C11.2,0.716344,10.4837,0,9.6,0L4.8,0C3.91634,0,3.2,0.716344,3.2,1.6L4.16,1.6Q4.16,1.3349,4.34745,1.14745Q4.5349,0.96,4.8,0.96L9.6,0.96Q9.8651,0.96,10.0525,1.14745Q10.24,1.3349,10.24,1.6L10.24,6.4Q10.24,6.6651,10.0525,6.85255Q9.8651,7.04,9.6,7.04L9.6,8C10.4837,8,11.2,7.28366,11.2,6.4L11.2,1.6ZM0,4L0,9.6C0,10.4837,0.716344,11.2,1.6,11.2L7.2,11.2C8.08366,11.2,8.8,10.4837,8.8,9.6L8.8,4C8.8,3.11634,8.08366,2.4,7.2,2.4L1.6,2.4C0.716344,2.4,0,3.11634,0,4ZM1.14745,10.0525Q0.96,9.8651,0.96,9.6L0.96,4Q0.96,3.7349,1.14745,3.54745Q1.3349,3.36,1.6,3.36L7.2,3.36Q7.4651,3.36,7.65255,3.54745Q7.84,3.7349,7.84,4L7.84,9.6Q7.84,9.8651,7.65255,10.0525Q7.4651,10.24,7.2,10.24L1.6,10.24Q1.3349,10.24,1.14745,10.0525Z"></path></g></svg></div></span><div><pre style="display: block; overflow-x: auto; padding: 16px 8px; background: rgb(30, 30, 30); color: rgb(221, 221, 221); margin: 0px; font-size: 13px;"><code style="white-space: pre; background-color: transparent;"><span class="comment linenumber react-syntax-highlighter-line-number" style="display: inline-block; min-width: 2.25em; padding-right: 20px; text-align: right; user-select: none; color: rgb(133, 133, 133); font-size: 13px;">1</span><span>COLOR_WHITE = (</span><span class="hljs-number">255</span><span>, </span><span class="hljs-number">255</span><span>, </span><span class="hljs-number">255</span><span>)
</span><span class="comment linenumber react-syntax-highlighter-line-number" style="display: inline-block; min-width: 2.25em; padding-right: 20px; text-align: right; user-select: none; color: rgb(133, 133, 133); font-size: 13px;">2</span><span>COLOR_BLACK = (</span><span class="hljs-number">0</span><span>, </span><span class="hljs-number">0</span><span>, </span><span class="hljs-number">0</span><span>)
</span><span class="comment linenumber react-syntax-highlighter-line-number" style="display: inline-block; min-width: 2.25em; padding-right: 20px; text-align: right; user-select: none; color: rgb(133, 133, 133); font-size: 13px;">3</span><span>COLOR_LIGHT_BLUE = (</span><span class="hljs-number">156</span><span>, </span><span class="hljs-number">220</span><span>, </span><span class="hljs-number">254</span><span>)
</span><span class="comment linenumber react-syntax-highlighter-line-number" style="display: inline-block; min-width: 2.25em; padding-right: 20px; text-align: right; user-select: none; color: rgb(133, 133, 133); font-size: 13px;">4</span><span>COLOR_PINK = (</span><span class="hljs-number">218</span><span>, </span><span class="hljs-number">94</span><span>, </span><span class="hljs-number">152</span><span>)
</span><span class="comment linenumber react-syntax-highlighter-line-number" style="display: inline-block; min-width: 2.25em; padding-right: 20px; text-align: right; user-select: none; color: rgb(133, 133, 133); font-size: 13px;">5</span><span>COLOR_ORANGE = (</span><span class="hljs-number">243</span><span>, </span><span class="hljs-number">133</span><span>, </span><span class="hljs-number">24</span><span>)
</span><span class="comment linenumber react-syntax-highlighter-line-number" style="display: inline-block; min-width: 2.25em; padding-right: 20px; text-align: right; user-select: none; color: rgb(133, 133, 133); font-size: 13px;">6</span><span>COLOR_GREEN = (</span><span class="hljs-number">100</span><span>, </span><span class="hljs-number">115</span><span>, </span><span class="hljs-number">0</span><span>)</span></code></pre></div></div></pre>
<hr>
<h2>🤝 贡献说明</h2>
<p>欢迎对该模块进行改进和扩展！如果您有任何建议或发现 Bug，请提交 Issues 或 Pull Request。</p>
<hr>
<h2>👤 作者信息</h2>
<p>👤 <strong>二七叁叁</strong></p>
