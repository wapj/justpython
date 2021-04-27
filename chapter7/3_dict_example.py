# 딕셔너리 만들기
d = {"키": "값", 'a': 1, 'b': 2, (1, 2): (1, 2, 3), 3: 33}

# 키,값을 추가하기
d["c"] = 3
d[4] = 44
d[(3, 4)] = 34

# 값을 가져오기
# print(d["0"])

# get 키에서 값을 가져오기
# print(d.get("aaaa", "기본값"))

# clear : 값 지우기
# d.clear()

# copy : 딕셔너리 복사
dd = d.copy()
dd["test"] = "테스트"
dd[(1, 2)] = 123
# print(dd)

# fromkeys : 키들로 새로운 딕셔너리를 만들기
ddd = {}.fromkeys(["a", "b", "z"], "newvalue")
# print(ddd)

# items : 딕셔너리 순회하기

# for k, v in d.items():
#     print(k, v)

# keys :딕셔너리의 키들만 가져오기

# for k in d.keys():
#     print(k)

# values :딕셔너리의 값들만 가져오기
# for v in d.values():
#     print(v)


# pop : 키가 있으면 값을 리턴하고 삭제

# print(d.pop("a"))
# print(d.pop("b"))
# print(d.pop((1, 2)))
# print(d.pop("z"))

# popitem() :  (키, 값) 의 튜플을 꺼냄.
# 가장 마지막에 넣은 것을 가장 먼저 꺼냄 LIFO : last in first out
# print(d.popitem())
# print(d.popitem())
# print(d.popitem())
# print(d.popitem())
# print(d.popitem())
# print(d.popitem())
# print(d.popitem())
# print(d.popitem())
# print(d.popitem())

# setdefault("key", 기본값) : 딕셔너리에 키가 있으면 해당 키의 값을 가져옴.
# 없으면 기본 값을 할당 후에 값을 가져옴.
print(d.setdefault("a", "111"))
print(d.setdefault("z", "999"))

# update 딕셔너리의 키/값을 다른 딕셔너리나 리스트를 사용하여 업데이트
d.update({"a": 11, "b": 22, "c": 33})
d.update([("z", "99"), (3, 333), (4, 444)])

if __name__ == '__main__':
    print(d)
