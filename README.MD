Check code
========
### Python 版本验证码生成工具

### 使用方法：

- python check_code.py 
- 会在当前目录下生成 code.gif
- 或者使用StringIO模块，用户web端验证码生成

### 参数说明：

字段名称    |       含义        | 默认值
------------|-------------------|-------
size        |图片大小           | 120x30
char        |所有可能的字符     | 除了i、l、o、z（大小写）、0、1、2的所有字母和数字
bg_color    |背景颜色 默认为白色| 白色(255,255,255)
font_size   |验证码字体大小     | 18
font_type   |字体文件           | ae_AlArabiya.ttf
length      |验证码字符长度     | 4
draw_lines  |是否有干扰线       | True
line_wdith  |干扰线宽度         | 1
n_line      |干扰线数目         | 1-2
draw_points |是否有干扰点       | True
point_chance|干扰点密集程度     | 2

