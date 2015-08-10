class Building:
    def __init__(self, south, west, width_we, width_ns, height=10):
        self.s = south
        self.w = west
        self.w_e = width_we
        self.n_s = width_ns
        self.h = height

    def area(self):
        return self.w_e * self.n_s

    def corners(self):
        return {'south-west': (self.s, self.w),
                'north-west': (self.n_s + self.s, self.w),
                'north-east': (self.n_s + self.s, self.w_e + self.w),
                'south-east': (self.s, self.w_e + self.w)}

    def volume(self):
        return self.area() * self.h

    def __repr__(self):
        return 'Building({}, {}, {}, {}, {})'.format(self.s, self.w, self.w_e,
                                                     self.n_s, self.h)

b = Building(1, 2, 2, 2)
assert b.corners() == {'south-west': (1, 2), 'south-east': (1, 4),
                       'north-east': (3, 4), 'north-west': (3, 2)}
assert b.area() == 4
assert b.volume() == 40
assert str(b) == 'Building(1, 2, 2, 2, 10)'
