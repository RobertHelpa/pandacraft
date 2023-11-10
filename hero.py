class Hero:
    def __init__(self, pos, land):
        self.land = land
        self.hero = loader.loadModel("smiley")
        self.hero.setColor(1, 0.5, 0, 1)
        self.hero.setScale(0.3)
        self.hero.setPos(pos)

        self.hero.reparentTo(render)

        self.cameraBind()

        self.acceptEvents()

    def cameraBind(self):
        base.disableMouse()
        base.camera.reparentTo(self.hero)
        base.camera.setPos(0,0,1.5)
        base.camera.setH(180)
        
        self.cameraOn = True
    
    def cameraUnbind(self):
        base.enableMouse()
        base.camera.reparentTo(render)

        pos = self.hero.getPos()
        base.mouseInterfaceNode.setPos(-pos[0], -pos[1], -pos[2]-1)
        
        self.cameraOn = False

    def changeMode(self):
        if self.cameraOn:
            self.cameraUnbind()
        else:
            self.cameraBind()

    def turnLeft(self):
        angle = self.hero.getH()
        angle += 5
        self.hero.setH(angle)
        
        #self.hero.setH((self.hero.getH() + 5))
    def turnRight(self):
        self.hero.setH((self.hero.getH() - 5))

    def turnUp(self):
        self.hero.setP((self.hero.getP() - 5))

    def turnDown(self):
        self.hero.setP((self.hero.getP() + 5))

    def lookAt(self):
        ...

    def checkDir(self):
        ...

    def forward(self):
        ...
    
    def back(self):
        ...

    def acceptEvents(self):
        base.accept("c", self.changeMode)

        base.accept("arrow_left", self.turnLeft)
        base.accept("arrow_left"+'-repeat', self.turnLeft)

        base.accept("arrow_right", self.turnRight)
        base.accept("arrow_right"+'-repeat', self.turnRight)

        base.accept("arrow_up", self.turnUp)
        base.accept("arrow_up"+'-repeat', self.turnUp)

        base.accept("arrow_down", self.turnDown)
        base.accept("arrow_down"+'-repeat', self.turnDown)