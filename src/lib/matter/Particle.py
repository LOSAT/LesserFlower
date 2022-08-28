class Particle:
    __id_counter = 0
    @staticmethod
    def generate_id():
        Particle.__id_counter += 1
        return Particle.__id_counter
    def __init__(self, pos, color) -> None:
        self._x = pos.x
        self._y = pos.y
        self._color = color
        self.id = Particle.generate_id()
        self.engine = None # on App.add() called

    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, value):
        self._x = value
        if(self.engine.entities.size >= self.id + 5):
            self.engine.entities[self.id + 1] = self._x
    
    @property
    def y(self):
        return self._y
    
    @y.setter
    def y(self, value):
        self._y = value
        if(self.engine.entities.size >= self.id + 5):
            self.engine.entities[self.id + 2] = self._y

    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, value):
        self._color = value
        if(self.engine.entities.size >= self.id + 5):
            self.engine.entities[self.id + 3] = self._color