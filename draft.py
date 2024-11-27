try:
    x = 1 / 0
except TypeError:
    print('на ноль делить нельзя')
finally:
    print('все равно делим')