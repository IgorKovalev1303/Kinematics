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

            point.build_lines(t[12], x1, x2)

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

            point.build_lines(t[13], x1, x2)

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

            point.build_lines(t[14], x1, x2)

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

            point.build_lines(t[15], x1, x2)

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

            point.build_lines(t[16], x1, x2)

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

            point.build_lines(t[17], x1, x2)

            plt.plot(xi1, xi2)
            v1 = -1 * (1.7 ** 2) * x1[i][j][17]
            v2 = 1.7 * x2[i][j][17]
            plt.quiver(x1[i][j][17], x2[i][j][17], (x1[i][j][17] + v1), (x2[i][j][17] + v2), angles='xy',
                       scale_units='xy', scale=1)
    return plt
