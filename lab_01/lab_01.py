import sys
EPS = 1e-2
class Point:
    def __init__(self, x, y, der = 0):
        self.x = x
        self.y = y
        self.der = der
        
def build_configuration(points, value, points_num):
    min_dif = abs(points[0].x - value)
    ind = 0
    for i in range(len(points)):
        if abs(points[i].x - value) < min_dif:
            min_dif = abs(points[i].x - value)
            ind = i
    left = ind
    right = ind
    for i in range(points_num - 1):
        if i % 2 == 0:
            if left == 0:
                right += 1
            else:
                left -= 1
        else:
            if right == len(points) - 1:
                left -= 1
            else:
                right += 1
    return points[left:right + 1]
            
def build_result_row_Newton(points, points_num):
    val_column = [p.y for p in points]
    arg_column = [p.x for p in points]
    result = [val_column[0]]
    col_num = len(val_column)
    for i in range(1, col_num):
        for j in range (col_num - 1):
            val_column[j] = ( val_column[j] - val_column[j + 1] ) / (arg_column[j] - arg_column[j + i])
        result.append(val_column[0])
        col_num -= 1
    return (result, arg_column)

def build_result_row_Hermite(points, points_num):
    val_column = []
    arg_column = []
    for i in range(points_num):
        arg_column.append(points[int(i / 2)].x)
        val_column.append(points[int(i / 2)].y)
    result = [val_column[0]]
    for j in range (points_num - 1):
        if j % 2 == 0:
            val_column[j] = points[int(j / 2)].der
        else:
            val_column[j] = ( val_column[j] - val_column[j + 1] ) / (arg_column[j] - arg_column[j + 1])
    result.append(val_column[0])
    points_num -= 1
    for i in range(2, points_num + 1):
        for j in range (points_num - 1):
            val_column[j] = ( val_column[j] - val_column[j + 1] ) / (arg_column[j] - arg_column[j + i])
        result.append(val_column[0])
        points_num -= 1
    return (result, arg_column)

def count_poly(arg_column, difs, points_num, value):
    result = 0
    multiplier = 1
    for i in range (points_num):
        result += (difs[i] * multiplier)
        multiplier *= (value - arg_column[i])
    return result

def print_results(points):
    points.sort(key=lambda point: point.x, reverse=False)
    value = 0.525
    print("x---------x---------x---------x---------x---------x")
    print("| method  |  n = 1  |  n = 2  |  n = 3  |  n = 4  |")
    print("x---------x---------x---------x---------x---------x")
    print("|  Newton |", end = "")
    for n in range(1, 5):
        p = build_configuration(points, value, n + 1)
        difs, arg_column = build_result_row_Newton(p, n + 1)
        res = count_poly(arg_column, difs, n + 1, value)
        print("{:9.6f}|".format(res), end = "")
    print()
    print("x---------x---------x---------x---------x---------x")
    print("| Hermite |", end = "")
    for n in range(1, 5):
        p = build_configuration(points, value, n + 1)
        difs, arg_column = build_result_row_Hermite(p, n + 1)
        res = count_poly(arg_column, difs, n + 1, value)
        print("{:9.6f}|".format(res), end = "")
    print()
    print("x---------x---------x---------x---------x---------x")
    print()
    print("x---------x---------x---------x---------x")
    print("|         |  n = 2  |  n = 3  |  n = 4  |")
    print("x---------x---------x---------x---------x")
    print("|  Root   |", end = "")
    for p in points:
        p.x, p.y = p.y, p.x
    points.sort(key=lambda point: point.x, reverse=False)
    value = 0
    for n in range(2, 5):
        p = build_configuration(points, value, n + 1)
        difs, arg_column = build_result_row_Newton(p, n + 1)
        res = count_poly(arg_column, difs, n + 1, value)
        print("{:9.6f}|".format(res), end = "")
    print()
    print("x---------x---------x---------x---------x")    

if __name__ == "__main__":
    f = open("data_02.txt")
    points = []
    for line in f:
        x_val, y_val, der = map(float, line.split())
        point = Point(x_val, y_val, der)
        points.append(point)
    f.close()
    #print_results(points)
    n = int(input())
    value = 0.525
    points.sort(key=lambda point: point.x, reverse=False)
    p = build_configuration(points, value, n + 1)
    difs, arg_column = build_result_row_Newton(p, n + 1)
    res = count_poly(arg_column, difs, n + 1, value)
    print("{:.6f}".format(res))


