one = int(input())
two = set()
three = 0
four = 0
while four == 0:
    if three == one:
        d = input()
        break
    else:
        a = input()
    three = three + 1
    two.add(a)
if d not in two:
    print('OK')
else:
    print('TRY ANOTHER')