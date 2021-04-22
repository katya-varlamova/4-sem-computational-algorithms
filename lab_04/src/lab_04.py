import random
import matplotlib.pyplot as plt
def gauss(matrix, n):
    for k in range(n):
        for i in range(k + 1, n):
            coeff = -(matrix[i][k] / matrix[k][k])
            for j in range(k, n + 1):
                matrix[i][j] += coeff * matrix[k][j]

    a = [0 for i in range(n)]
    for i in range(n - 1, -1, -1):
        for j in range(n - 1, i, -1):
            matrix[i][n] -= a[j] * matrix[i][j]
        a[i] = matrix[i][n] / matrix[i][i]
    return a
def print_graph(x, y, ro):
    for i in range (len(x)):
        plt.scatter(x[i], y[i])
    mi = min(x)
    ma = max(x)
    lab = "same weight"
    for n in [1,1]:
        coefs = least_squares_method(x, y, ro, n)
        x_pr = []
        y_pr = []
        dx = (ma - mi) / 1000
        i = mi
        while i < ma:
            s = 0
            for j in range(len(coefs)):
                s += (i**j) * coefs[j]
            x_pr.append(i)
            y_pr.append(s)
            i += dx
        plt.plot(x_pr, y_pr, label=lab.format(n))
        ro[0] = 2
        ro[1] = 3
        ro[2] = 2
        ro[3] = 1
        ro[4] = 10
        lab = "different weight"

    plt.grid(True)
    plt.legend(loc='best')
    plt.show()
    return
def least_squares_method(x, y, ro, n):
    N = len(x)
    matrix = []
    for k in range(n + 1):
        array = []
        for m in range(n + 1):
            s = 0
            for i in range(N):
                s += ro[i] * (x[i])**(k + m)
            array.append(s)
        s = 0
        for i in range(N):
            s += ro[i] * y[i] * (x[i])**(k)
        array.append(s)
        matrix.append(array)
    res = gauss(matrix, n + 1)
    return res
    
def read_file():
    f = open("data.txt")
    x = []
    y = []
    ro = []
    
    for line in f:
        try:
            xp, yp, rop = map(float, line.split())
        except:
            return ()
        x.append(xp)
        y.append(yp)
        ro.append(rop)
    f.close()
    return (x, y, ro)
def generate_file():
    n = int(input("количество точек: "))
    flag = int (input("0 - разные веса\n1 - одинаковые веса\n"))
    same = True
    if flag == 0:
        same = False
    f = open("data.txt", "w")
    for i in range(n):
        x = random.randint(0, 30) / 10
        y = random.randint(0, 30) / 10
        ro = 1
        if same == False:
            ro = random.randint(0, 25)
        f.write("{} {} {}\n".format(x, y, ro))
    f.close()
               
choise = int(input("0 - использовать существующий файл\n\
1 - сгенерировать новый\n"))
t = ()
if choise == 0:
    t = read_file()
    if t == ():
        print("произошла ошибка чтения, сгенерируйте новый файл")
        generate_file()
        t = read_file()
if choise == 1:
    generate_file()
    t = read_file()
#n = int(input("степень полинома: "))
print_graph(t[0], t[1], t[2])
