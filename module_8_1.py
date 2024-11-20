def add_everything_up(a, b):
    try:
        summ = a + b
    except TypeError as exc:
        return str(a) + str(b)
    else:
        return round(a + b, 3)
    # finally:
    #     print("финалочка")


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))