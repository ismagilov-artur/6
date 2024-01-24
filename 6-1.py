one = set()
two = set()
three = input()
while three != '':
    one.add(three)
    three = input()
one.add(three)
c1 = input()
while c1 != '':
    two.add(c1)
    c1 = input()
intersection = one & two
if not intersection:
    print('EMPTY')
else:
    for i in intersection:
        print(i)