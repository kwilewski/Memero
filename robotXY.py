class robot_xy(object):
    """description of class"""

    def __init__(self,x_pos,y_pos,angle):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.angle = angle

    def position(self):
        return '{}|{}|{}'.format(self.x_pos, self.y_pos, self.angle) 

    def set_x(self, x_pos):
        self.x_pos = x_pos

    def set_y(self, y_pos):
        self.y_pos = y_pos

    def setAngle(self, angle):
        self.angle = angle

    def x_change(self, change):
        self.x_pos += change

    def y_change(self, change):
        self.y_pos += change

    def angle_change(self, change):
        self.angle += angle





