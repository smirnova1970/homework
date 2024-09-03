def add_everything_up(a, b):
    try:
        c = round(a + b, 3)
        #round(c, 2)
    except TypeError:
        c = str(a) + str(b)
    return c



print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))

