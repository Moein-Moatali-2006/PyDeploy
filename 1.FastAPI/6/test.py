# def justforfun():
#     yield 1
#     yield 2
#     yield 3


# for value in justforfun():
#     print(value)


# ------------------------------------------------------------------

def square():
    i = 1
    while True:
        yield i * i
        i += 1

for number in square():
    print(number)
    if number > 100:
        break
