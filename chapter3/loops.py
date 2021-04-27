def loop1():
    # 무한반복
    while True:
        print("안녕하세요~?")


# loop1()

def loop2():
    x = 0
    while x < 10:
        print(f"x : {x}")
        x += 1


# loop2()

def loop3():
    while True:
        command = input("[exit] 종료 : ")
        print("안녕하세요~ ")

        if command == "exit":
            break


# loop3()
def list1():
    li = []
    print(type(li))


# list1()

def list2():
    basket = ["오렌지", "망고", "사과", "파인애플"]
    print(basket)


def list3():
    dice = [1, 2, 3, 4, 5, 6]
    print(dice)


def list4():
    lotto = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
             21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
             41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
             61, 62, 63, 64, 65]
    print(lotto)


def list5():
    # 트럼프 카드 덱
    spades = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
    clubs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
    diamonds = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
    hearts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]

    deck = [spades, clubs, diamonds, hearts]
    print(deck)


# list5()

def for1():
    for n in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
        print(n)


def for2():
    for n in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,
              18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31,
              32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45,
              46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59,
              60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73,
              74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87,
              88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]:
        if n % 10 == 1:
            print()
        print(n, end=" ")

# for2()


def range1():
    for n in range(100):
        # 0 ~ 99
        if n % 10 == 0:
            print()
        print(n + 1, end=" ")

# range1()

def gugudan(num):
    for n in range(9):
        print(f"{num} * {n + 1} = {num * (n+1)}")

# gugudan(3)

def gugudan2():
    # 1~9단 모두 출력
    for n in range(9):
        # n : 0 ~ 8
        print("==============")
        gugudan(n + 1)

gugudan2()










































