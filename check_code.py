# -*- coding: utf-8 -*-
import sys
import random
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageColor

_letter_cases =  "abcdefghjkmnpqrstuvwxy"   # 去除i l o z
_upper_cases = _letter_cases.upper()
_number_cases = ''.join(map(str, xrange(3,10)))     # 去除 0 1 2 
init_chars = ''.join((_letter_cases,_upper_cases,_number_cases))

def create_validate_code(size = (120,30),
                         char = init_chars,
                         mode = 'RGB',
                         bg_color = (255,255,255),
                         font_size = 18,
                         font_type = 'ae_AlArabiya.ttf',
                         length = 4,
                         line_width = 1,
                         draw_lines = True,
                         n_line = (1,2),
                         draw_points = True,
                         point_chance = 2):
    width, height = size
    img = Image.new(mode, size, bg_color)   # 创建图形
    draw = ImageDraw.Draw(img)  # 创建画笔

    def get_color():
        colors = ['Black','Orange','Red','Brown','DarkBlue','Purple','DarkCyan','DarkBlue']
        return ImageColor.getrgb(colors[random.randrange(1,9)-1])

    def get_chars():
        '''返回给定长度的字符串'''
        return random.sample(char, length)

    def create_lines():
        '''绘制干扰线'''
        line_num = random.randint(*n_line)

        for i in xrange(line_num):
            # 起始点
            begin = (random.randint(0, width), random.randint(0, height))
            # 结束点
            end = (random.randint(0, width), random.randint(0, height))
            draw.line([begin, end], fill=get_color(), width=line_width)

    def create_points():
        '''干扰点'''
        chance = min(100, max(0, int(point_chance)))
        for w in xrange(width):
            for h in xrange(height):
                temp = random.randint(0,100)
                if temp > 100 - chance:
                    draw.point((w,h), fill=(0,0,0))

    def create_strs():
        '''绘制验证码'''
        c_chars = get_chars()
        strs = ' %s ' % ' '.join(c_chars)
        font = ImageFont.truetype(font_type, font_size)
        font_width, font_height = font.getsize(strs)
        draw.text(((width - font_width) / 3, (height - font_height) / 3),
                    strs, font=font, fill=get_color())
        return ''.join(c_chars)

    if draw_lines:
        create_lines()
    if draw_points:
        create_points()
    strs = create_strs()

    img = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
    return img, strs

if __name__ == '__main__':
    code_img, str= create_validate_code()
    # 使用方法
    # 1、
    # import StringIO
    # buf = StringIO.StringIO()
    # code_img.save(buf, 'JPEG')
    # 2、
    code_img.save('./code/'+str+'.gif', 'GIF')