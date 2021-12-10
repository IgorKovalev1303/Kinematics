class MaterialPoint:
    def __int__(self, l_coord_x, l_coord_y, e_coord_x, e_coord_y, vel_x, vel_y):
        self.l_coord_x = l_coord_x
        self.l_coord_y = l_coord_y
        self.e_coord_x = e_coord_x
        self.e_coord_y = e_coord_y
        self.vel_x = vel_x
        self.vel_y = vel_y


class MaterialBody:
    def __int__(self, material_points):
        self.material_points = material_points
