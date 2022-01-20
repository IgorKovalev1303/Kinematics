from modules.modules import MaterialPoints
import matplotlib.pyplot as plt


def kinem():
    lagrange = MaterialPoints()
    lagrange.l_coord_x = []
    lagrange.l_coord_y = []
    for i in range(3):
        for j in range(3):
            lagrange.l_coord_x.append(-2 + j / 2)
            lagrange.l_coord_y.append(-1 - i / 2)
            for n in range(15):
                a1 = -((0.1 * n) ** 2) * lagrange.l_coord_x[n]
                b1 = -((0.1 * n + 1 / 15) ** 2) * (lagrange.l_coord_x[n] + 1 / 15 * a1)
                c1 = -((0.1 * n + 1 / 15) ** 2) * (lagrange.l_coord_x[n] + 0.1 * (-1 / 3 * a1 + b1))
                lagrange.l_coord_x.append(lagrange.l_coord_x[n] + 0.1 * (0.25 * a1 + 0.5 * b1 + 0.25 * c1))
                a2 = 0.1 * n * lagrange.l_coord_y[n]
                b2 = (0.1 * n + 1 / 15) * (lagrange.l_coord_y[n] + 1 / 15 * a2)
                c2 = (0.1 * n + 1 / 15) * (lagrange.l_coord_y[n] + 0.1 * (-1 / 3 * a2 + b2))
                lagrange.l_coord_y.append(lagrange.l_coord_y[n] + 0.1 * (0.25 * a2 + 0.5 * b2 + 0.25 * c2))
            plt.plot(lagrange.l_coord_x, lagrange.l_coord_y)
            lagrange.l_coord_x = []
            lagrange.l_coord_y = []
    return plt
