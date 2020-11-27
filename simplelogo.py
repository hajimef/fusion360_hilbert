import math, adsk.core

class SimpleLogo:
    def __init__(self):
        self._x = 0
        self._y = 0
        self._dir = 180
        self._old_dir = 180
        self._old_line = None
        self._lines = None
        self._arcs = None
        self._paths = adsk.core.ObjectCollection.create()

    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y
    
    @y.setter
    def y(self, value):
        self._y = value

    @property
    def dir(self):
        return self._dir
    
    @dir.setter
    def dir(self, value):
        self._dir = value

    @property
    def lines(self):
        return self._lines
    
    @lines.setter
    def lines(self, value):
        self._lines = value

    @property
    def arcs(self):
        return self._arcs
    
    @arcs.setter
    def arcs(self, value):
        self._arcs = value

    @property
    def paths(self):
        return self._paths

    def right(self, deg):
        self._dir -= deg
        self._dir %= 360
    
    def left(self, deg):
        self._dir += deg
        self._dir %= 360

    def forward(self, len):
        lx = math.cos(math.pi / 180 * self.dir) * len
        ly = math.sin(math.pi / 180 * self.dir) * len
        arc = None
        new_line = self.lines.addByTwoPoints(adsk.core.Point3D.create(self.x, self.y, 0), adsk.core.Point3D.create(self.x + lx, self.y + ly, 0))
        self.x += lx
        self.y += ly
        self._old_dir = self.dir
        self._paths.add(new_line)
        self._old_line = new_line