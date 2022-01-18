from modules.modules import MaterialPoints
import matplotlib.pyplot as plt


def kinem():
    lagrange = MaterialPoints()
    lagrange.l_coord_x = []
    lagrange.l_coord_y = []
    for i in range(6):
        for j in range(6):
            lagrange.l_coord_x.append(-2 + j / 5)
            lagrange.l_coord_y.append(-1 - i / 5)
            for n in range(70):
                k11 = -((0.1 * n) ** 2) * lagrange.l_coord_x[n]
                k12 = -((0.1 * n + 1 / 15) ** 2) * (lagrange.l_coord_x[n] + 1 / 15 * k11)
                k13 = -((0.1 * n + 1 / 15) ** 2) * (lagrange.l_coord_x[n] + 0.1 * (-1 / 3 * k11 + k12))
                lagrange.l_coord_x.append(lagrange.l_coord_x[n] + 0.1 * (0.25 * k11 + 0.5 * k12 + 0.25 * k13))
                k21 = 0.1 * n * lagrange.l_coord_y[n]
                k22 = (0.1 * n + 1 / 15) * (lagrange.l_coord_y[n] + 1 / 15 * k21)
                k23 = (0.1 * n + 1 / 15) * (lagrange.l_coord_y[n] + 0.1 * (-1 / 3 * k21 + k22))
                lagrange.l_coord_y.append(lagrange.l_coord_y[n] + 0.1 * (0.25 * k21 + 0.5 * k22 + 0.25 * k23))
            plt.plot(lagrange.l_coord_x, lagrange.l_coord_y)
            lagrange.l_coord_x = []
            lagrange.l_coord_y = []
    return plt
