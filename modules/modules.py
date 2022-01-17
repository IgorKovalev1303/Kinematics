class MaterialPoints:
    def __int__(self, l_coord_x, l_coord_y):
        self.l_coord_x = l_coord_x
        self.l_coord_y = l_coord_y


class MaterialBody:
    def __int__(self, material_points_x, material_points_y):
        self.material_points_x = material_points_x
        self.material_points_y = material_points_y

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