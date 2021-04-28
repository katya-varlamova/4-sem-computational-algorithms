def left(y, h, i):
    return (y[i] - y[i - 1]) / h if i > 0 else "-"

def right(y, h, i):
    return (y[i + 1] - y[i]) / h if i < len(y) - 1 else "-"

def center(y, h, i):
    return (y[i + 1] - y[i - 1]) / 2 / h if i < len(y) - 1 and i > 0 else "-"

def left_double(y, h, i):
    return (y[i] - y[i - 2]) / 2 / h if i > 1 else "-"
def runge_left(y, h, i):
    if i < 2:
        return "-"
    f1 = left(y, h, i)
    f2 = left_double(y, h, i)
    return f1 + (f1 - f2) 


def align_vars_right(y, h, i):
    if i > len(y) - 2:
        return "-"
    der = (1 / y[i + 1] - 1 / y[i]) / (1 / x[i + 1] - 1 / x[i])
    return der * y[i] * y[i] / x[i] / x[i]

def second_der(y, h, i):
    return (y[i - 1] - 2 * y[i] + y[i + 1]) / (h * h) if i < len(y) - 1 and i > 0 else "-"

x = [1, 2, 3, 4, 5, 6]
y = [0.571, 0.889, 1.091, 1.231, 1.333, 1.412]

methods = [left, center, runge_left, align_vars_right, second_der]
print("x---------x---------x---------x---------x---------x---------x---------x")
print("|    x    |    y    |   left  |  center |  runge  |  align  |  second |")
print("x---------x---------x---------x---------x---------x---------x---------x")
for i in range(len(x)):
    print("|{:9.3f}|".format(x[i]), end = "")
    print("{:9.3f}|".format(y[i]), end = "")
    for func in methods:
        res = func(y, 1, i)
        if res == '-':
            print("    -    |", end = "")
        else:
            print("{:9.4f}|".format(res), end = "")
    print()
print("x---------x---------x---------x---------x---------x---------x---------x")
