angl = int(input())
nemeckiy = int(input())
yazik = set()
surnames = set()
for i in range(angl + nemeckiy):
    surname = input()
    if surname in yazik:
        surnames.add(surname)
    else:
        yazik.add(surname)
difference = yazik - surnames
if not difference:
    print('NO')
else:
    print(len(difference))
