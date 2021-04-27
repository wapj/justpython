"""
사각형 컴퍼니는 다양한 사각형의 넓이를 구해주는 회사입니다.
클라이언트에게 사각형의 넓이를 구해달라는 요청이 왔습니다.
클라이언트에게 방문해보니 가로, 세로가 각각 10, 4라고 사각형 측량사에게 연락이 왔습니다.
우리에겐 `넓이 = 가로 x 세로` 라는 공식이 있으니 그 공식으로 넓이를 구해주면 될 것 같아요.
"""

def get_area(width, height):
    return width * height

"""
사업이 잘되서 갑자기 5군데의 클라이언트에게서 연락이 왔어요~! 
이제 5개의 사각형을 추가로 관리해야합니다.  
사각형 5개에 대한 데이터가 더 필요하겠군요!  
데이터는 각각 (3, 5), (5,7), (23, 4), (6,8), (9,10) 이었다고 합니다.  
추가로 5개의 데이터를 넣어봅시다. 
기존 데이터는 당연히 그대로 있어야합니다.  
"""
class Rectangle:

    def __init__(self, w, h):
        self.width = w
        self.height = h

    def get_area(self):
        return "사각형의넓이", self.width * self.height

    def get_perimeter(self):
        return (self.width + self.height) * 2


r1 = Rectangle(10, 4)
r2 = Rectangle(3, 5)
r3 = Rectangle(5,7)
r4 = Rectangle(23, 4)
r5 = Rectangle(6,8)
r6 = Rectangle(9,10)

print(r1.get_area(), r1.get_perimeter())
print(r2.get_area(), r2.get_perimeter())
print(r3.get_area(), r3.get_perimeter())
print(r4.get_area(), r4.get_perimeter())
print(r5.get_area(), r5.get_perimeter())
print(r6.get_area(), r6.get_perimeter())















