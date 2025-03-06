from panda3d.core import Vec3 as vec3

class camera():
    def __init__(self, base):
        self.base = base
        self.position = vec3(0, 0, 0)
        self.camera = base.camera

        self.mouse = base.mouseWatcherNode

        self.yaw = 0
        self.pitch = 0



        # movement options
        self.base.accept("w", self.moveForward)
        self.base.accept("a", self.moveLeft)
        self.base.accept("s", self.moveBackward)
        self.base.accept("d", self.moveRight)

    def cameraMovement(self):
        md = self.base.win.getPointer(0)
        x = md.getX()
        y = md.getY()

        if self.mouse.isButtonDown(1):
            self.yaw = self.yaw - (x - 400)
            self.pitch = self.pitch - (y - 300)

            self.camera.setHpr(self.yaw, self.pitch, 0)
    
    def moveForward(self):
        self.camera.setPos(self.camera, 0, 1, 0)
    
    def moveBackward(self):
        self.camera.setPos(self.camera, 0, -1, 0)

    def moveLeft(self):
        self.camera.setPos(self.camera, -1, 0, 0)

    def moveRight(self):
        self.camera.setPos(self.camera, 1, 0, 0)

    def update(self):
        clock = self.base.globalClock
        dt = clock.getDt()