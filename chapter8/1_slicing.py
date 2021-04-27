# 슬라이스 표기법 [start:stop:step] 연습하기
# txt = "파이썬그냥재미로"
# print(txt[-1])
# print(txt[3:])
# print(txt[:3])
# print(txt[::2])
# print(txt[3:5])
# print(txt[1:7:2])

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
arr2 = arr[::]
# print(arr)
# print(arr2)
# print(arr == arr2)
# print(arr is arr2)
# print(id(arr) == id(arr2))
# print(id(arr))
# print(id(arr2))
# arr_reverse = arr[::-1]
# print(arr[-2:2:-1])

arr[:4] = [10, 20, 30, 40]
arr2[:4] = [10, 20, 30, 40, 50]
arr3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
arr3[::2] = [22, 22, 22, 22, 22]

# print(arr)
# print(arr2)
# print(arr3)

tp = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# tp[:4] = (10, 20, 30, 40)

print(tp[slice(3, 5, 1)])
