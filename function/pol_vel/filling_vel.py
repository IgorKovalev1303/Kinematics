import matplotlib.pyplot as plt
from modules.modules import MaterialPoints, MaterialBody


def velocity():
    t = []
    body = MaterialBody()  # экземпляр класса MaterialBody
    point = MaterialPoints()  # экземпляр класса MaterialPoint
    x1 = body.material_points_x = []  # x
    x2 = body.material_points_y = []  # y
    n = 0
    xi1 = point.l_coord_x = []  # линии тока x
    xi2 = point.l_coord_y = []  # линии тока y
    for i in range(21):
        xi1.append(0)
        xi2.append(0)
    for i in range(71):
        t.append(i / 10)
    plt.subplot(2, 3, 1)
    # заполнение координат точек твердого тела
    body.filling_coord()

    '''with open("log.txt", "a") as f:
        print('x:', x1, '\n', file=f)
        print('y:', x2, '\n', file=f)'''
    for i in range(6):
        for j in range(6):
            xi1[10] = x1[i][j][12]
            xi2[10] = x2[i][j][12]
            for k in range(1, 11):
                k1 = -((t[12] * xi1[10 - k + 1]) / xi2[10 - k + 1])
                k2 = -((t[12] * (xi1[10 - k + 1] - 0.1 * 2 / 3 * k1)) / (xi2[10 - k + 1] - 2 / 3 * 0.1))
                k3 = -((t[12] * (xi1[10 - k + 1] - 0.1 * (-1 / 3 * k1 + k2))) / (xi2[10 - k + 1] - 2 / 3 * 0.1))
                xi1[10 - k] = xi1[10 - k + 1] - 0.1 * (0.25 * k1 + 0.5 * k2 + 0.25 * k3)
                xi2[10 - k] = xi2[10 - k + 1] - 0.1
                k1 = -((t[12] * xi1[10 + k - 1]) / xi2[10 + k - 1])
                k2 = -((t[12] * (xi1[10 + k - 1] + 0.1 * 2 / 3 * k1)) / (xi2[10 + k - 1] + 2 / 3 * 0.1))
                k3 = -((t[12] * (xi1[10 + k - 1] + 0.1 * (-1 / 3 * k1 + k2))) / (xi2[10 + k - 1] + 2 / 3 * 0.1))
                xi1[10 + k] = xi1[10 + k - 1] + 0.1 * (0.25 * k1 + 0.5 * k2 + 0.25 * k3)
                xi2[10 + k] = xi2[10 + k - 1] + 0.1
                for i1 in range(70):
                    for i2 in range(6):
                        for i3 in range(6):
                            if xi1[10 - k] == x1[i2][i3][i1] and xi2[10 - k] == x2[i2][i3][i1]:
                                print('xi1[', 10 - k, ']==x1[', i2, '][', i3, '][', i1, '], ', 'xi2[', 10 - k, ']==x2[',
                                      i2, '][', i3, '][', i1, ']')
                            if xi1[10 + k] == x1[i2][i3][i1] and xi2[10 + k] == x2[i2][i3][i1]:
                                print('xi1[', 10 + k, ']==x1[', i2, '][', i3, '][', i1, '], ', 'xi2[', 10 + k, ']==x2[',
                                      i2, '][', i3, '][', i1, ']')
            plt.plot(xi1, xi2)
            v1 = -1 * (1.2 ** 2) * x1[i][j][12]
            v2 = 1.2 * x2[i][j][12]
            plt.quiver(x1[i][j][12], x2[i][j][12], (x1[i][j][12] + v1), (x2[i][j][12] + v2), angles='xy',
                       scale_units='xy', scale=1)
    plt.subplot(2, 3, 2)
    for i in range(6):
        for j in range(6):
            xi1[10] = x1[i][j][13]
            xi2[10] = x2[i][j][13]
            for k in range(1, 11):
                k1 = -((t[13] * xi1[10 - k + 1]) / xi2[10 - k + 1])
                k2 = -((t[13] * (xi1[10 - k + 1] - 0.1 * 2 / 3 * k1)) / (xi2[10 - k + 1] - 2 / 3 * 0.1))
                k3 = -((t[13] * (xi1[10 - k + 1] - 0.1 * (-1 / 3 * k1 + k2))) / (xi2[10 - k + 1] - 2 / 3 * 0.1))
                xi1[10 - k] = xi1[10 - k + 1] - 0.1 * (0.25 * k1 + 0.5 * k2 + 0.25 * k3)
                xi2[10 - k] = xi2[10 - k + 1] - 0.1
                k1 = -((t[13] * xi1[10 + k - 1]) / xi2[10 + k - 1])
                k2 = -((t[13] * (xi1[10 + k - 1] + 0.1 * 2 / 3 * k1)) / (xi2[10 + k - 1] + 2 / 3 * 0.1))
                k3 = -((t[13] * (xi1[10 + k - 1] + 0.1 * (-1 / 3 * k1 + k2))) / (xi2[10 + k - 1] + 2 / 3 * 0.1))
                xi1[10 + k] = xi1[10 + k - 1] + 0.1 * (0.25 * k1 + 0.5 * k2 + 0.25 * k3)
                xi2[10 + k] = xi2[10 + k - 1] + 0.1
                for i1 in range(70):
                    for i2 in range(6):
                        for i3 in range(6):
                            if xi1[10 - k] == x1[i2][i3][i1] and xi2[10 - k] == x2[i2][i3][i1]:
                                print('xi1[', 10 - k, ']==x1[', i2, '][', i3, '][', i1, '], ', 'xi2[', 10 - k, ']==x2[',
                                      i2, '][', i3, '][', i1, ']')
                            if xi1[10 + k] == x1[i2][i3][i1] and xi2[10 + k] == x2[i2][i3][i1]:
                                print('xi1[', 10 + k, ']==x1[', i2, '][', i3, '][', i1, '], ', 'xi2[', 10 + k, ']==x2[',
                                      i2, '][', i3, '][', i1, ']')
            plt.plot(xi1, xi2)
            v1 = -1 * (1.3 ** 2) * x1[i][j][13]
            v2 = 1.3 * x2[i][j][13]
            plt.quiver(x1[i][j][13], x2[i][j][13], (x1[i][j][13] + v1), (x2[i][j][13] + v2), angles='xy',
                       scale_units='xy', scale=1)
    plt.subplot(2, 3, 3)
    for i in range(6):
        for j in range(6):
            xi1[10] = x1[i][j][14]
            xi2[10] = x2[i][j][14]
            for k in range(1, 11):
                k1 = -((t[14] * xi1[10 - k + 1]) / xi2[10 - k + 1])
                k2 = -((t[14] * (xi1[10 - k + 1] - 0.1 * 2 / 3 * k1)) / (xi2[10 - k + 1] - 2 / 3 * 0.1))
                k3 = -((t[14] * (xi1[10 - k + 1] - 0.1 * (-1 / 3 * k1 + k2))) / (xi2[10 - k + 1] - 2 / 3 * 0.1))
                xi1[10 - k] = xi1[10 - k + 1] - 0.1 * (0.25 * k1 + 0.5 * k2 + 0.25 * k3)
                xi2[10 - k] = xi2[10 - k + 1] - 0.1
                k1 = -((t[14] * xi1[10 + k - 1]) / xi2[10 + k - 1])
                k2 = -((t[14] * (xi1[10 + k - 1] + 0.1 * 2 / 3 * k1)) / (xi2[10 + k - 1] + 2 / 3 * 0.1))
                k3 = -((t[14] * (xi1[10 + k - 1] + 0.1 * (-1 / 3 * k1 + k2))) / (xi2[10 + k - 1] + 2 / 3 * 0.1))
                xi1[10 + k] = xi1[10 + k - 1] + 0.1 * (0.25 * k1 + 0.5 * k2 + 0.25 * k3)
                xi2[10 + k] = xi2[10 + k - 1] + 0.1
                for i1 in range(70):
                    for i2 in range(6):
                        for i3 in range(6):
                            if xi1[10 - k] == x1[i2][i3][i1] and xi2[10 - k] == x2[i2][i3][i1]:
                                print('xi1[', 10 - k, ']==x1[', i2, '][', i3, '][', i1, '], ', 'xi2[', 10 - k, ']==x2[',
                                      i2, '][', i3, '][', i1, ']')
                            if xi1[10 + k] == x1[i2][i3][i1] and xi2[10 + k] == x2[i2][i3][i1]:
                                print('xi1[', 10 + k, ']==x1[', i2, '][', i3, '][', i1, '], ', 'xi2[', 10 + k, ']==x2[',
                                      i2, '][', i3, '][', i1, ']')
            plt.plot(xi1, xi2)
            v1 = -1 * (1.4 ** 2) * x1[i][j][14]
            v2 = 1.4 * x2[i][j][14]
            plt.quiver(x1[i][j][14], x2[i][j][14], (x1[i][j][14] + v1), (x2[i][j][14] + v2), angles='xy',
                       scale_units='xy', scale=1)
    plt.subplot(2, 3, 4)
    for i in range(6):
        for j in range(6):
            xi1[10] = x1[i][j][15]
            xi2[10] = x2[i][j][15]
            for k in range(1, 11):
                k1 = -((t[15] * xi1[10 - k + 1]) / xi2[10 - k + 1])
                k2 = -((t[15] * (xi1[10 - k + 1] - 0.1 * 2 / 3 * k1)) / (xi2[10 - k + 1] - 2 / 3 * 0.1))
                k3 = -((t[15] * (xi1[10 - k + 1] - 0.1 * (-1 / 3 * k1 + k2))) / (xi2[10 - k + 1] - 2 / 3 * 0.1))
                xi1[10 - k] = xi1[10 - k + 1] - 0.1 * (0.25 * k1 + 0.5 * k2 + 0.25 * k3)
                xi2[10 - k] = xi2[10 - k + 1] - 0.1
                k1 = -((t[15] * xi1[10 + k - 1]) / xi2[10 + k - 1])
                k2 = -((t[15] * (xi1[10 + k - 1] + 0.1 * 2 / 3 * k1)) / (xi2[10 + k - 1] + 2 / 3 * 0.1))
                k3 = -((t[15] * (xi1[10 + k - 1] + 0.1 * (-1 / 3 * k1 + k2))) / (xi2[10 + k - 1] + 2 / 3 * 0.1))
                xi1[10 + k] = xi1[10 + k - 1] + 0.1 * (0.25 * k1 + 0.5 * k2 + 0.25 * k3)
                xi2[10 + k] = xi2[10 + k - 1] + 0.1
                for i1 in range(70):
                    for i2 in range(6):
                        for i3 in range(6):
                            if xi1[10 - k] == x1[i2][i3][i1] and xi2[10 - k] == x2[i2][i3][i1]:
                                print('xi1[', 10 - k, ']==x1[', i2, '][', i3, '][', i1, '], ', 'xi2[', 10 - k, ']==x2[',
                                      i2, '][', i3, '][', i1, ']')
                            if xi1[10 + k] == x1[i2][i3][i1] and xi2[10 + k] == x2[i2][i3][i1]:
                                print('xi1[', 10 + k, ']==x1[', i2, '][', i3, '][', i1, '], ', 'xi2[', 10 + k, ']==x2[',
                                      i2, '][', i3, '][', i1, ']')
            plt.plot(xi1, xi2)
            v1 = -1 * (1.5 ** 2) * x1[i][j][15]
            v2 = 1.5 * x2[i][j][15]
            plt.quiver(x1[i][j][15], x2[i][j][15], (x1[i][j][15] + v1), (x2[i][j][15] + v2), angles='xy',
                       scale_units='xy', scale=1)
    plt.subplot(2, 3, 5)
    for i in range(6):
        for j in range(6):
            xi1[10] = x1[i][j][16]
            xi2[10] = x2[i][j][16]
            for k in range(1, 11):
                k1 = -((t[16] * xi1[10 - k + 1]) / xi2[10 - k + 1])
                k2 = -((t[16] * (xi1[10 - k + 1] - 0.1 * 2 / 3 * k1)) / (xi2[10 - k + 1] - 2 / 3 * 0.1))
                k3 = -((t[16] * (xi1[10 - k + 1] - 0.1 * (-1 / 3 * k1 + k2))) / (xi2[10 - k + 1] - 2 / 3 * 0.1))
                xi1[10 - k] = xi1[10 - k + 1] - 0.1 * (0.25 * k1 + 0.5 * k2 + 0.25 * k3)
                xi2[10 - k] = xi2[10 - k + 1] - 0.1
                k1 = -((t[16] * xi1[10 + k - 1]) / xi2[10 + k - 1])
                k2 = -((t[16] * (xi1[10 + k - 1] + 0.1 * 2 / 3 * k1)) / (xi2[10 + k - 1] + 2 / 3 * 0.1))
                k3 = -((t[16] * (xi1[10 + k - 1] + 0.1 * (-1 / 3 * k1 + k2))) / (xi2[10 + k - 1] + 2 / 3 * 0.1))
                xi1[10 + k] = xi1[10 + k - 1] + 0.1 * (0.25 * k1 + 0.5 * k2 + 0.25 * k3)
                xi2[10 + k] = xi2[10 + k - 1] + 0.1
                for i1 in range(70):
                    for i2 in range(6):
                        for i3 in range(6):
                            if xi1[10 - k] == x1[i2][i3][i1] and xi2[10 - k] == x2[i2][i3][i1]:
                                print('xi1[', 10 - k, ']==x1[', i2, '][', i3, '][', i1, '], ', 'xi2[', 10 - k, ']==x2[',
                                      i2, '][', i3, '][', i1, ']')
                            if xi1[10 + k] == x1[i2][i3][i1] and xi2[10 + k] == x2[i2][i3][i1]:
                                print('xi1[', 10 + k, ']==x1[', i2, '][', i3, '][', i1, '], ', 'xi2[', 10 + k, ']==x2[',
                                      i2, '][', i3, '][', i1, ']')
            plt.plot(xi1, xi2)
            v1 = -1 * (1.6 ** 2) * x1[i][j][16]
            v2 = 1.6 * x2[i][j][16]
            plt.quiver(x1[i][j][16], x2[i][j][16], (x1[i][j][16] + v1), (x2[i][j][16] + v2), angles='xy',
                       scale_units='xy', scale=1)
    plt.subplot(2, 3, 6)
    for i in range(6):
        for j in range(6):
            xi1[10] = x1[i][j][17]
            xi2[10] = x2[i][j][17]
            for k in range(1, 11):
                k1 = -((t[17] * xi1[10 - k + 1]) / xi2[10 - k + 1])
                k2 = -((t[17] * (xi1[10 - k + 1] - 0.1 * 2 / 3 * k1)) / (xi2[10 - k + 1] - 2 / 3 * 0.1))
                k3 = -((t[17] * (xi1[10 - k + 1] - 0.1 * (-1 / 3 * k1 + k2))) / (xi2[10 - k + 1] - 2 / 3 * 0.1))
                xi1[10 - k] = xi1[10 - k + 1] - 0.1 * (0.25 * k1 + 0.5 * k2 + 0.25 * k3)
                xi2[10 - k] = xi2[10 - k + 1] - 0.1
                k1 = -((t[17] * xi1[10 + k - 1]) / xi2[10 + k - 1])
                k2 = -((t[17] * (xi1[10 + k - 1] + 0.1 * 2 / 3 * k1)) / (xi2[10 + k - 1] + 2 / 3 * 0.1))
                k3 = -((t[17] * (xi1[10 + k - 1] + 0.1 * (-1 / 3 * k1 + k2))) / (xi2[10 + k - 1] + 2 / 3 * 0.1))
                xi1[10 + k] = xi1[10 + k - 1] + 0.1 * (0.25 * k1 + 0.5 * k2 + 0.25 * k3)
                xi2[10 + k] = xi2[10 + k - 1] + 0.1
                for i1 in range(70):
                    for i2 in range(6):
                        for i3 in range(6):
                            if xi1[10 - k] == x1[i2][i3][i1] and xi2[10 - k] == x2[i2][i3][i1]:
                                print('xi1[', 10 - k, ']==x1[', i2, '][', i3, '][', i1, '], ', 'xi2[', 10 - k, ']==x2[',
                                      i2, '][', i3, '][', i1, ']')
                            if xi1[10 + k] == x1[i2][i3][i1] and xi2[10 + k] == x2[i2][i3][i1]:
                                print('xi1[', 10 + k, ']==x1[', i2, '][', i3, '][', i1, '], ', 'xi2[', 10 + k, ']==x2[',
                                      i2, '][', i3, '][', i1, ']')
            plt.plot(xi1, xi2)
            v1 = -1 * (1.7 ** 2) * x1[i][j][17]
            v2 = 1.7 * x2[i][j][17]
            plt.quiver(x1[i][j][17], x2[i][j][17], (x1[i][j][17] + v1), (x2[i][j][17] + v2), angles='xy',
                       scale_units='xy', scale=1)
    return plt
