def my_func(x, y):
    if y > 0:
        y -= y * 2
    print(x ** y)
    x = abs(x)
    number = x
    z = 1
    while abs(y) != z:
        number *= x
        z += 1
    print(round((1 / number), 5))


my_func(8, -4)