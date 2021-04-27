import traceback


def try_except_test():
    state = "시작"
    try:
        f = open("test.txt")
        print(f.read())
        f.close()
    except FileNotFoundError:
        print("해당하는 파일이 없습니다.")
    finally:
        state = "끝"
    print(state)



def excepts_test(a):
    try:
        if isinstance(a, str):
            a + 1
        elif isinstance(a, int):
            a / 0
        elif isinstance(a, list):
            a[0]
        elif isinstance(a, dict):
            a.isdict()
    except Exception as err:
        print(err)
        print(traceback.format_exc())



if __name__ == '__main__':
    # try_except_test()
    # print("111")
    excepts_test('a')
    excepts_test(1)
    excepts_test({})
    excepts_test([])
