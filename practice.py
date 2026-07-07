def count():
    for i in range(1,6):
        yield i

for num in count():
    print(num)