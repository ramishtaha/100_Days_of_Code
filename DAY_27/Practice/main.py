def add(*args):
    print(sum(args))

add(1, 2, 3, 4)

def calculate(**kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(value, key)


calculate(add = 9, mul = 76)