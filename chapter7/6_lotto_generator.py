# 로또 생성기 만들기
import random


def get_lotto():
    lotto = set()
    while len(lotto) < 6:
        num = random.randrange(1, 47)
        lotto.add(num)
    lotto_list = list(lotto)
    lotto_list.sort()
    return tuple(lotto_list)


if __name__ == '__main__':
    lotto_set = set()

    for x in range(5):
        lotto_set.add(get_lotto())

    for x in lotto_set:
        print(x)
