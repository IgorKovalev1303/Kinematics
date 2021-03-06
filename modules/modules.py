COLUMNS = 3  # СТОЛБЦЫ
ROWS = 3  # СТРОКИ


class SpacePoints:
    def __int__(self, coord_x, coord_y, velocity_x, velocity_y):
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y

    def build_lines(self, t, x1, x2):
        xi1 = self.coord_x
        xi2 = self.coord_y
        for k in range(1, 11):
            k1 = -((t * xi1[10 - k + 1]) / xi2[10 - k + 1])
            k2 = -((t * (xi1[10 - k + 1] - 0.1 * 2 / 3 * k1)) / (xi2[10 - k + 1] - 2 / 3 * 0.1))
            k3 = -((t * (xi1[10 - k + 1] - 0.1 * (-1 / 3 * k1 + k2))) / (xi2[10 - k + 1] - 2 / 3 * 0.1))
            xi1[10 - k] = xi1[10 - k + 1] - 0.1 * (0.25 * k1 + 0.5 * k2 + 0.25 * k3)
            xi2[10 - k] = xi2[10 - k + 1] - 0.1
            k1 = -((t * xi1[10 + k - 1]) / xi2[10 + k - 1])
            k2 = -((t * (xi1[10 + k - 1] + 0.1 * 2 / 3 * k1)) / (xi2[10 + k - 1] + 2 / 3 * 0.1))
            k3 = -((t * (xi1[10 + k - 1] + 0.1 * (-1 / 3 * k1 + k2))) / (xi2[10 + k - 1] + 2 / 3 * 0.1))
            xi1[10 + k] = xi1[10 + k - 1] + 0.1 * (0.25 * k1 + 0.5 * k2 + 0.25 * k3)
            xi2[10 + k] = xi2[10 + k - 1] + 0.1
            for i1 in range(70):
                for i2 in range(ROWS):
                    for i3 in range(COLUMNS):
                        if xi1[10 - k] == x1[i2][i3][i1] and xi2[10 - k] == x2[i2][i3][i1]:
                            print('xi1[', 10 - k, ']==x1[', i2, '][', i3, '][', i1, '], ', 'xi2[', 10 - k, ']==x2[',
                                  i2, '][', i3, '][', i1, ']')
                        if xi1[10 + k] == x1[i2][i3][i1] and xi2[10 + k] == x2[i2][i3][i1]:
                            print('xi1[', 10 + k, ']==x1[', i2, '][', i3, '][', i1, '], ', 'xi2[', 10 + k, ']==x2[',
                                  i2, '][', i3, '][', i1, ']')


class SpaceGird:
    def __int__(self, space_points_x, space_points_y):
        self.space_points_x = space_points_x
        self.space_points_y = space_points_y

    def filling_coord(self):
        x1 = self.space_points_x
        x2 = self.space_points_y
        for i in range(ROWS):  # i создание точек квадрата, имеющих одинаковую координату по оси ординат
            x1.append([])
            x2.append([])
            for j in range(COLUMNS):  # переход на новый уровень вниз по оси ординат
                x1[i].append([])
                x2[i].append([])
                x1[i][j].append(-2 + j / 2)  # x[[[-2]]] - x
                x2[i][j].append(-1 - i / 2)  # x[[[-1]]] - y
                for n in range(70):  # изменение координаты во времени
                    k11 = -((0.1 * n) ** 2) * x1[i][j][n]
                    k12 = -((0.1 * n + 1 / 15) ** 2) * (x1[i][j][n] + 1 / 15 * k11)
                    k13 = -((0.1 * n + 1 / 15) ** 2) * (x1[i][j][n] + 0.1 * (-1 / 3 * k11 + k12))
                    x1[i][j].append(x1[i][j][n] + 0.1 * (0.25 * k11 + 0.5 * k12 + 0.25 * k13))
                    k21 = 0.1 * n * x2[i][j][n]
                    k22 = (0.1 * n + 1 / 15) * (x2[i][j][n] + 1 / 15 * k21)
                    k23 = (0.1 * n + 1 / 15) * (x2[i][j][n] + 0.1 * (-1 / 3 * k21 + k22))
                    x2[i][j].append(x2[i][j][n] + 0.1 * (0.25 * k21 + 0.5 * k22 + 0.25 * k23))


class PointTrajectory:
    def __init__(self, material_point, x, y):
        self.material_point = material_point
        self.x = x
        self.y = y


class BodyTrajectory:
    def __init__(self, point_trajectories, material_body):
        self.point_trajectories = point_trajectories
        self.material_body = material_body


class MaterialPoints:
    def __int__(self, l_coord_x, l_coord_y):
        self.l_coord_x = l_coord_x
        self.l_coord_y = l_coord_y


class MaterialBody:
    def __int__(self, material_points):
        self.material_points = material_points
