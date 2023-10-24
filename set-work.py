list1 = input('type some numbers with spaces')
liststr = list1.split(' ')
listfin = list(liststr)
print(listfin)

previous = set()
print(previous)

for num in listfin:
    if num in previous:
        print('YES')
        print(num)
    else:
        previous.add(num)
        print('NO')
        print(num)
        
print(previous)
