import random
import textwrap

from PIL import Image, ImageDraw, ImageFont, ImageColor

if __name__ == '__main__':
    text = "파이썬 그냥 재미로~! 썸네일을 만들어 봅시다."
    texts = textwrap.wrap(text, width=15)

    W, H = 480, 480
    random_color = random.choice(list(ImageColor.colormap.values()))
    img = Image.new("RGB", (W, H), random_color)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype('AppleGothic.ttf', 30)
    current_top, line_padding = 100, 30
    random_color = "#fffafa"

    """    
    https://stackoverflow.com/questions/9780632/how-do-i-determine-if-a-color-is-closer-to-white-or-black    
    """
    rgb_code = random_color[1:]
    R, G, B = int(rgb_code[0:2], 16), int(rgb_code[2:4], 16), int(rgb_code[4:], 16)
    Y = 0.2126 * R + 0.7152 * G + 0.0722 * B
    font_color = 'black' if Y > 128 else 'white'

    for line in texts:
        w, h = font.getsize(line)
        draw.text(((W - w) / 2, current_top), line, font=font, fill=font_color)
        current_top += h + line_padding
    img.save("thumbnail.png", "PNG")
    img.show()
