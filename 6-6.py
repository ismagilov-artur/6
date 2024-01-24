home_book = set()
home_book_1 = int(input())
home_task = set()
home_task_M = int(input())
for i in range(home_book_1):
    book = input()
    home_book.add(book)
for i in range(home_task_M):
    book = input()
    home_task.add(book)
    if book in home_book:
        print('YES')
    else:
        print('NO')