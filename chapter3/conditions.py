import random

# num = random.randrange(1000, 20001)
# print(num)
#
# if num % 2 == 0:
#     print("짝")
# else:
#     print("홀")

# age 변수를 주고 19세 미만이면 "19세 미만은 시청하실 수 없습니다." 를 출력해보자

# age = random.randrange(1, 100)
#
# age = 18
# print(age)
# if age < 19:
#     print("19세 미만은 시청하실 수 없습니다.")

# score = random.randrange(55, 101)
#
# if score >= 95:
#     print(score, 'A+')
# elif score >= 90:
#     print(score, 'A')
# elif score >= 85:
#     print(score, 'B+')
# elif score >= 80:
#     print(score, 'B')
# elif score >= 75:
#     print(score, 'C+')
# elif score >= 70:
#     print(score, 'C')
# elif score >= 65:
#     print(score, 'D+')
# elif score >= 60:
#     print(score, 'D')
# else:
#     print(score, 'F')

"""
salary : ~1200 의 경우, 세금으로 6%를 뗀다.
salary : 1201~4600 의 경우, 세금으로 15%를 뗀다. 
salary : 4601~8800 의 경우, 세금으로 24%를 뗀다.
salary : 8801~15000 의 경우, 세금으로 35%를 뗀다.
salary : 15001~ 의 경우, 세금으로 40%를 뗀다. 
"""

# # 실수령액을 구하자.
# salary = random.randrange(1200, 20001, 10)
# # 1200 1210 1220 1230 ~ 20000
#
# tax = 0
# if salary <=1200:
#     tax = salary * 0.06
# elif salary > 1200 and salary <= 4600:
#     tax = salary * 0.15
# elif salary > 4600 and salary <= 8800:
#     tax = salary * 0.24
# elif salary > 8800 and salary <= 15000:
#     tax = salary * 0.35
# else:
#     tax = salary * 0.4
#
# real_salary = salary - tax
# print(f"salary : {salary} | tax : {tax} | real salary : {real_salary}")


# import random
# rsp = random.choice(["가위", "바위", "보"])
# print(rsp)
"""
랜덤하게 "가위", "바위", "보"를 리턴해주는 get_rsp() 라는 함수를 만들자. 
get_rsp() 를 두번호출하여 player1, player2 라는 변수에 각각 담자. 
result_rsp(player1, player2) 라는 함수를 만들고, 가위, 바위, 보 대결의 결과를 출력해주자. 
가위는 보에게 이기고, 바위는 가위에게 이기고 ,보는 바위에게 이긴다. 
같은 결과가 나오면 무승부를 출력하자. 
"""

import random


def get_rsp():
    return random.choice(["가위", "바위", "보"])


player1 = get_rsp()
player2 = get_rsp()


def result_rsp(p1, p2):
    if p1 == p2:
        print(f"p1 {p1} vs p2 {p2} |", "무승부입니다.")
    elif (
        (p1 == "가위" and p2 == "보")
        or (p1 == "바위" and p2 == "가위")
        or (p1 == "보" and p2 == "바위")
    ):
        print(f"p1 {p1} vs p2 {p2} |", "p1 승리")
    else:
        print(f"p1 {p1} vs p2 {p2} |", "p2 승리")


# result_rsp(player1, player2)

"""
1. 1에서 13사이의 랜덤한 수를 리턴해주는 함수 random_num() 함수를 만듭니다. 
2. random_num()을 사용해서 p1, p2 에 각각 랜덤한 수를 할당합니다. 
3. 두 수를 비교해서 큰 수가 나온 플레이어가 이기는 게임을 만들어 봅시다. 
4. 무승부인 경우 재시합을 하게 됩니다. 재시합에도 무승부인 경우에만 무승부로 표시를 해줍니다. 
"""

def random_num():
    return random.randrange(1, 14)

plr1 = random_num()
plr2 = random_num()

def game(p1, p2):
    print(f"p1 {p1} | p2 {p2} ")
    if p1 > p2:
        print("p1 win")
    elif p1 < p2:
        print("p2 win")
    else:
        p1 = random_num()
        p2 = random_num()
        p1 = 1
        p2 = 1
        print(f"rematch : p1 {p1} | p2 {p2} ")
        if p1 > p2:
            print("p1 win")
        elif p1 < p2:
            print("p2 win")
        else:
            print("draw")

game(plr1, plr2)

























