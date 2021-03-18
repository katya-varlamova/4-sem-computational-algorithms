EPS = 1e-2

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
def form_points_arr(x_arr, y_arr):
    points = []
    for i in range(min(len(y_arr), len(x_arr))):
        points.append(Point(x_arr[i], y_arr[i]))
    return points         
        
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

def print_points(points):
    for point in points:
        print(point.x, point.y)
    print()
    
def Newton_interpolation(points, value, n):
    points.sort(key=lambda point: point.x, reverse=False)
    p = build_configuration(points, value, n + 1)
    difs, arg_column = build_result_row_Newton(p, n + 1)
    res = count_poly(arg_column, difs, n + 1, value)
    return res
        
def interp_of_two_dim_func(x_array, y_array, z_matrix, nx, ny, x_value, y_value):
    x_interp_res = []
    for i in range(ny + 1):
        points = form_points_arr(x_array, z_matrix[i])
        print_points(points)
        x_interp_res.append(Newton_interpolation(points, x_value, nx))
    points = form_points_arr(y_array, x_interp_res)
    print_points(points)
    res = Newton_interpolation(points, y_value, ny)
    print(res)
    return res
def print_table(x_array, y_array, z_matrix, x_val, y_val):
    print("x---------x---------x---------x---------x")
    print("|         |  nx = 1 |  nx = 2 |  nx = 3 |")
    print("x---------x---------x---------x---------x")
    print("| ny = 1  |", end = "")
    for nx in range(1, 4):
        res = interp_of_two_dim_func(x_array, y_array, z_matrix, nx, 1, x_val, y_val)
        print("{:9.6f}|".format(res), end = "")
    print()
    
    print("| ny = 2  |", end = "")
    for nx in range(1, 4):
        res = interp_of_two_dim_func(x_array, y_array, z_matrix, nx, 2, x_val, y_val)
        print("{:9.6f}|".format(res), end = "")
    print()

    print("| ny = 3  |", end = "")
    for nx in range(1, 4):
        res = interp_of_two_dim_func(x_array, y_array, z_matrix, nx, 3, x_val, y_val)
        print("{:9.6f}|".format(res), end = "")
    print()
    
    print("x---------x---------x---------x---------x")
if __name__ == "__main__":
    f = open("data.txt")
    x_array = list(map(float, f.readline().split()))
    y_array = list(map(float, f.readline().split()))
    z_matrix = []
    for line in f:
        z_array = list(map(float, line.split()))
        z_matrix.append(z_array)
    f.close()
    x_val = 1.5
    y_val = 1.5
    nx = 1
    ny = 1
    interp_of_two_dim_func(x_array, y_array, z_matrix, nx, ny, x_val, y_val)
    #print_table(x_array, y_array, z_matrix, x_val, y_val)
