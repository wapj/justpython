import random
import time


class BaseBall:
    """
    <베이스볼 게임 규칙>
    3자리 베이스볼 (4자리도 있으나 편의상 3자리로 합니다. 4자리도 해보세요.)
    사용되는 숫자는 0에서 9까지 서로 다른 숫자이다. [OK]
    숫자는 맞지만 위치가 틀렸을 때는 볼.
    숫자와 위치가 전부 맞으면 스트라이크.
    숫자와 위치가 전부 틀리면 아웃.
    물론 무엇이 볼이고 스트라이크인지는 알려주지 않는다.
    총 10라운드까지 진행 [OK]
    """

    @staticmethod
    def run():
        print("게임스타트")
        sample_size = 3
        arr = random.sample(range(10), sample_size)
        print(arr)
        cnt = 0
        rount_cnt = 10
        while cnt < rount_cnt:
            strike_cnt = 0
            ball_cnt = 0
            nums = input("숫자를 입력하세요 : ")
            if nums.isdigit() and len(nums) == sample_size:
                cnt += 1
                print(f"라운드 {cnt}")

                for i, num in enumerate(nums):
                    if arr[i] == int(num):
                        strike_cnt += 1
                    elif int(num) in arr:
                        ball_cnt += 1
                if strike_cnt == sample_size:
                    print(f"{sample_size} 스트라이크!! 승리하셨습니다!")
                    break
                else:
                    print(f"{strike_cnt} 스트라이크 | {ball_cnt} 볼")
        if cnt == rount_cnt:
            print(f"실패하였습니다. 숫자는 {arr}이었습니다.")


if __name__ == '__main__':
    try:
        BaseBall.run()
    except KeyboardInterrupt as err:
        msg = "\n프로그램을 종료하는 중입니다....\n"
        for c in msg:
            print(c, end="")
            time.sleep(.1)
        print("종료합니다.")
