# 가장 간단한 클래스
class MyClass:
    pass

class Hello:
    """헬로우 클래스"""

    default_text = "안녕하세요~"

    def __init__(self, name):
        self.name = name

    def hello(self):
        print(self.name, self.default_text)

# print(Hello)
# print(Hello.__doc__)
# print(Hello.hello())
h1 = Hello("seungkyoo")
h2 = Hello("seungkyoo2")
h3 = Hello("seungkyoo3")

print(h1)
print(h2)
print(h3)

























