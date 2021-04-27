def write_one_line():
    # 한줄 쓰기
    print("안녕하세요~", file=open('test.txt', 'w'))


def write_multi_line():
    f = open("test2.txt", 'w')
    for num in range(10):
        f.write(f"안녕하세요~ {num}\n")
    f.close()


def write_multi_line_use_with():
    with open('test3.txt', 'w') as f:
        for num in range(5):
            f.write(f"5 X {num + 1} = {(num + 1) * 5} \n")


def append_write():
    with open("append_text.txt", "a") as f:
        f.write("하나면 하나지 둘이겠느냐\n")
        f.write("둘이면 둘이지 셋은 아니야\n")
        f.write("셋이면 셋이지 넷은 아니고\n")
        f.write("넷이면 넷이지 다섯 아니야\n")


if __name__ == '__main__':
    # write_one_line()
    # write_multi_line()
    # write_multi_line_use_with()
    # append_write()

    # f = open('test.txt', 'rt')
    # print(f.readline())
    # f.close()

    # with open('test2.txt') as f:
    #     for line in f.readlines():
    #         print(line, end="")

    with open("test3.txt") as f:
        for line in f:
            print(line, end="")
