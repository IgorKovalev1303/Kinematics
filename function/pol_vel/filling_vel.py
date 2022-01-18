import matplotlib.pyplot as plt
from modules.modules import MaterialPoints, MaterialBody
from modules.modules import ROWS, COLUMNS  # константы


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
    plt.subplots_adjust(wspace=0.3, hspace=0.3)

    # заполнение координат точек твердого тела
    body.filling_coord()

    '''with open("log.txt", "a") as f:
        print('x:', x1, '\n', file=f)
        print('y:', x2, '\n', file=f)'''
    for i in range(ROWS):
        for j in range(COLUMNS):
            xi1[10] = x1[i][j][12]
            xi2[10] = x2[i][j][12]

            plt.subplot(2, 3, 1)
            plt.title(label='t=1,2', fontsize=8)
            point.build_lines(t[12], x1, x2)

            plt.plot(xi1, xi2)
            v1 = -1 * (1.2 ** 2) * x1[i][j][12]
            v2 = 1.2 * x2[i][j][12]

            plt.subplot(2, 3, 2)
            plt.title(label='t=1,2', fontsize=8)
            plt.quiver(x1[i][j][12], x2[i][j][12], (x1[i][j][12] + v1), (x2[i][j][12] + v2), angles='xy',
                       scale_units='xy', scale=1)
    plt.subplot(2, 3, 3)
    for i in range(ROWS):
        for j in range(COLUMNS):
            xi1[10] = x1[i][j][13]
            xi2[10] = x2[i][j][13]

            plt.subplot(2, 3, 3)
            plt.title(label='t=1,3', fontsize=8)
            point.build_lines(t[13], x1, x2)

            plt.plot(xi1, xi2)
            v1 = -1 * (1.3 ** 2) * x1[i][j][13]
            v2 = 1.3 * x2[i][j][13]

            plt.subplot(2, 3, 4)
            plt.title(label='t=1,3', fontsize=8)
            plt.quiver(x1[i][j][13], x2[i][j][13], (x1[i][j][13] + v1), (x2[i][j][13] + v2), angles='xy',
                       scale_units='xy', scale=1)
    plt.subplot(2, 3, 5)
    for i in range(ROWS):
        for j in range(COLUMNS):
            xi1[10] = x1[i][j][14]
            xi2[10] = x2[i][j][14]

            plt.subplot(2, 3, 5)
            plt.title(label='t=1,4', fontsize=8)
            point.build_lines(t[14], x1, x2)

            plt.plot(xi1, xi2)
            v1 = -1 * (1.4 ** 2) * x1[i][j][14]
            v2 = 1.4 * x2[i][j][14]

            plt.subplot(2, 3, 6)
            plt.title(label='t=1,4', fontsize=8)
            plt.quiver(x1[i][j][14], x2[i][j][14], (x1[i][j][14] + v1), (x2[i][j][14] + v2), angles='xy',
                       scale_units='xy', scale=1)

    return plt
