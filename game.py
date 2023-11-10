from direct.showbase.ShowBase import ShowBase
from hero import Hero
from mapmanager import MapManager

class Game(ShowBase):
    def __init__(self):
        super().__init__()
        self.land = MapManager()
        self.land.loadLand('land.txt')

        self.hero = Hero((2,2,1), self.land)
        base.camLens.setFov(90)

Game().run()
        