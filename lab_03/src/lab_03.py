EPS = 1e-2

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y  
        
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
        if i % 2 == 1:
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

def count_poly(arg_column, difs, points_num, value):
    result = 0
    multiplier = 1
    for i in range (points_num):
        result += (difs[i] * multiplier)
        multiplier *= (value - arg_column[i])
    return result

def form_points_arr(x_arr, y_arr):
    points = []
    for i in range(min(len(y_arr), len(x_arr))):
        points.append(Point(x_arr[i], y_arr[i]))
    return points

def Newton_interpolation(n, x, y, value):
    points = form_points_arr(x, y)
    points.sort(key=lambda point: point.x, reverse=False)
    p = build_configuration(points, value, n + 1)
    difs, arg_column = build_result_row_Newton(p, n + 1)
    res = count_poly(arg_column, difs, n + 1, value)
    return res


def spline(n, x, y, plot_x):
    n -= 1
    h = [0]
    for i in range(1, n + 1):
        h.append(x[i] - x[i - 1]) # 1 .. n
        

    ksi = [0, 0, 0]
    eta = [0, 0, 0]
    for i in range(2, n + 1):
        ksi.append(-(h[i]) / (h[i - 1] * ksi[i] + 2 * (h[i - 1] + h[i])))
        f = 3 * ((y[i] - y[i - 1]) / h[i] - (y[i - 1] - y[i - 2]) / h[i - 1])
        eta.append((f - h[i - 1] * eta[i]) / (h[i - 1] * ksi[i] + 2 * (h[i - 1] + h[i])))

    c = []
    for i in range (n + 2):
        c.append(0)
    for i in range (n + 1, 1, -1):
        c[i - 1] = c[i] * ksi[i] + eta[i]
        
    a = [0]
    b = [0]
    d = [0]
    for i in range(1, n + 1):
        a.append(y[i - 1])
        b.append((y[i] - y[i-1]) / h[i] - h[i] * (c[i+1] + 2 * c[i]) / 3)
        d.append((c[i+1] - c[i]) / (3 * h[i]))

    pos = -1
    for i in range(n):
        if x[i] <= plot_x and x[i + 1] > plot_x:
            pos = i + 1
            break
    return (a[pos] + b[pos] * (plot_x - x[pos-1]) + c[pos] * (plot_x - x[pos-1])**2 + d[pos] * (plot_x - x[pos-1])**3)

n = 11
x = []
y = []
for i in range(n):
    x.append(i)
    y.append(i * i)
print(spline(n, x, y, 5.5))
print(Newton_interpolation(3, x, y, 5.5))
