# pip install pillow 를 먼저 해주어야 실습이 가능합니다.s
from PIL import Image, ImageFont, ImageDraw


def make_box(width, height, color):
    return Image.new(mode="RGB", size=(width, height), color=color)



if __name__ == '__main__':
    # 파란색 가로,세로 100px 이미지 만들기
    # RGB(red, green, blue) 각각 256개의 값으로 표현함
    box = make_box(100, 100, '#0000FF')
    box.save("test1.png")

    # https://drafts.csswg.org/css-color-4/#named-colors
    # 위 사이트에서 색상표를 얻을 수 있다.
    img = make_box(300, 100, 'dodgerblue')
    # font = ImageFont.truetype("Arial Unicode.ttf", size=18, encoding="utf8")

    font = ImageFont.load_default()
    draw = ImageDraw.Draw(img)

    # 폰트를 찾는 경로는 mac의 경우는 ~/Library/Fonts 윈도우의 경우는 "C:\Windows\Fonts"이다.
    # 기본적으로 설치되어 있는 폰트를 사용하면 큰 문제는 없음
    # 윈도우 'malgun.ttf', 맥 'AppleGothic.ttf'

    draw.text(xy=(10, 10), text="파이썬 그냥 재미로", font=ImageFont.truetype('AppleGothic.ttf', 20))
    img.save("test2.png", format="PNG")

    # 이미지 보여주기
    # img.show()

    # 바이너리 파일 읽기
    # 바이너리 파일을 스트림을 사용하여 쓰는 일은 거의 없다고 보면 된다.
    with open("test2.png", "rb") as img_file:
        print(img_file.read())
