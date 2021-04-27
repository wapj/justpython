# 중복이 없고, 순서가 없는 자료구조 set
# 빈 set 만들기 set()

s = set()

# 값이 있는 set 만들기 {값, 값2, 값3..., 값n}
s = {1, 2, 3, 11, 22, 33, 1, 2, 3, 1, 2, 3}

# add(값) set 에 값을 추가
s.add(4)

# remove(값) set 에 값을 삭제 없는 요소를 삭제하라고 하면 에러
s.remove(4)
s.remove(33)

# discard(값) 값을 삭제 없으면 무시
s.discard(1)
s.discard(22)
s.discard(222)

# pop() 임의의 값을 리턴하고 삭제
# print(s.pop())
# print(s.pop())
# print(s.pop())
# print(s.pop())

# isdisjoint : 조인트(공통부분)이 없는지의 여부 확인
a = {1, 2, 3, 4, 5}
aa = {1, 2, 3}
b = {3, 4, 5, 6, 7}
c = {11, 22, 33}

# print(a.isdisjoint(b))
# print(a.isdisjoint(c))

# A.issubset(B) : A가 B의 부분집합인가
# print(b.issubset(a))

# A.issuperset(B) : A가 B의 상위집합인가
# print(aa.issuperset(a))

# A.union(B), A | B 합집합을 리턴
print(a | b)


# A.update(B), A |= B 원본을 합집합으로 업데이트
# a |= b
# a.update(b)
# print(a)
# A.difference(B), A - B 차집합을 리턴
print(a - b)

# A.difference_update(B), A -= B: A를 차집합으로 업데이트
# a -= b
# print(a)

# A.intersection(B), A & B 교집합을 리턴
print(a & b)


# A.intersection_update(B), A &= B : A를 교집합으로 업데이트
# a &= b
# print(a)

# A.symmetric_difference(B), A ^ B : 대칭차집합을 리턴
print(a ^ b)

# A.symmetric_difference_update(B), A ^= B : A를 대칭차집합으로 업데이트
a ^= b
print(a)

if __name__ == '__main__':
    # print(s)
    pass
