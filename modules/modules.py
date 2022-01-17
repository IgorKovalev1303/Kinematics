class MaterialPoints:
    def __int__(self, l_coord_x, l_coord_y):
        self.l_coord_x = l_coord_x
        self.l_coord_y = l_coord_y


class MaterialBody:
    def __int__(self, material_points_x, material_points_y):
        self.material_points_x = material_points_x
        self.material_points_y = material_points_y

    def filling_coord(self):
        x1 = self.material_points_x
        x2 = self.material_points_y
        for i in range(6):  # i создание точек квадрата, имеющих одинаковую координату по оси ординат
            x1.append([])
            x2.append([])
            for j in range(6):  # переход на новый уровень вниз по оси ординат
                x1[i].append([])
                x2[i].append([])
                x1[i][j].append(-2 + j / 5)  # x[[[-2]]] - x
                x2[i][j].append(-1 - i / 5)  # x[[[-1]]] - y
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


class SpacePoint:
    def __init__(self, coord_x, coord_y, velocity_x, velocity_y):
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y


class SpaceGrid:
    def __init__(self, space_points):
        self.space_points = space_points
