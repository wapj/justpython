"""
반복문 연습1
주사위를 던져서 랜덤한 숫자가 출력되게 하는 함수 dice()를 만들어봅시다.
dice() 를 두번실행하여 더한 값을 리턴하는 double_dice() 함수를 만들어보고 값을 출력해 봅시다.
"""
import random


def dice():
    return random.randrange(1, 7)


def double_dice():
    sum = 0
    for n in range(2):
        sum += dice()
    return sum


def multiple_dice(num):
    sum = 0
    for n in range(num):
        sum += dice()
    return sum


"""
double_dice를 player1, player2 에게 각각 실행시켜서 
큰 숫자가 나오는 플레이어가 이기는 게임을 만들어 봅시다. 
"""


def dice_game():
    p1 = double_dice()
    p2 = double_dice()

    if p1 > p2:
        print(f"p1 {p1} vs p2 {p2} | p1 win")
        return 1
    elif p2 > p1:
        print(f"p1 {p1} vs p2 {p2} | p2 win")
        return 2
    else:
        print(f"p1 {p1} vs p2 {p2} | draw")
        return 0


# dice_game()

"""
while 을 사용하여 주사위게임을 여러판 할 수 있게 만들어 봅시다. 
가상의 플레이어 p1, p2가 게임을 하게됩니다.
exit 를 입력하면 도중에 게임에서 나가도록 합시다.
종료시에는 지금까지 몇판을 했는지와 p1승리횟수, p2승리횟수, 무승부를 화면에 출력해봅시다. 
"""

def dice_game2():
    round_num = 0
    p1_win = 0
    p2_win = 0
    draw = 0
    while True:
        round_num += 1
        result = dice_game()
        if result == 1:
            p1_win +=1
        elif result == 2:
            p2_win += 1
        elif result == 0:
            draw += 1
        command = input("종료 exit : ")
        if command == 'exit':
            break
    print(f"round : {round_num}, p1win : {p1_win}, p2win: {p2_win}, draw:{draw}")

# dice_game2()
"""
가위바위보 게임을 만들고, player1을 사용자가 직접 입력할 수 있게 해봅시다.
r은 바위, s는 가위, p는 보를 의미한다고 합시다. 
컴퓨터는 랜덤을 사용하여 r,s,p를 내게 됩니다. 
for loop 를 사용해서 10판을 컴퓨터와 하고 전적(승,무,패) 를 계산하여 넣어봅시다. 
r, s, p 대신 exit 를 입력하면 도중에 게임을 포기할 수 있도록 해봅시다. 
"""

def rsp(p1, p2):
    if p1 == p2:
        print(f"p1 : {p1} vs p2 : {p2} draw")
        return 0
    elif (
            (p1 =="r" and p2 =="s") or
            (p1 == "s" and p2 == "p") or
            (p1 == "p" and p2 == "r")
    ):
        # p1 win
        print(f"p1 : {p1} vs p2 : {p2} p1 win")
        return 1
    else:
        # p2 win
        print(f"p1 : {p1} vs p2 : {p2} p2 win")
        return 2

#print(rsp("r", "p"))

def rsp_game():
    rsp_list = ['r', 's', 'p']
    win = 0
    draw = 0
    lose = 0
    for x in range(10):
        user = input("[바위] r, [가위] s, [보] p, [종료] exit : ")
        if user == 'exit':
            break

        computer = random.choice(rsp_list)
        if user not in rsp_list:
            lose += 1
            continue
        result = rsp(user, computer)
        if result == 1:
            win += 1
        elif result == 2:
            lose += 1
        elif result == 0:
            draw += 1

    print(f"win : {win}, draw : {draw}, lose : {lose}")


rsp_game()




















