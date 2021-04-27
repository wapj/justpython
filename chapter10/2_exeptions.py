def zerodivision():
    print("1")
    1 / 0


def name_error_test():
    print("2")
    a = 1
    print(b)


def type_error_test():
    print("3")
    '' + 1


if __name__ == '__main__':
    # zerodivision()
    # name_error_test()
    type_error_test()
