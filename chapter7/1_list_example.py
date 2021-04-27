li = []
li2 = [1, 2, 3, 4, 5]

# append
li.append(11)
# clear
li.clear()

# copy
li3 = li2.copy()
li3.append(11)
# count
li3.append(1)
print(li3.count(1))

# extend
li.extend([1, 2, 3, 4,5])
# index
print(li3.index(1))
print(li3.index(1, 1))
# insert
li3.insert(5, 6)
# pop
print(li3.pop())

# remove
li3.remove(11)


# reverse
li3.reverse()

# sort
li3.sort()
li3.sort(reverse=True)

if __name__ == '__main__':
    print("==================")
    print(li)
    print(li2)
    print(li3)
