from panda3d.core import Vec3

class Camera():
    def __init__(self, base):
        self.camFront = Vec3(0.294037, 0.758073, -0.582123)
        self.camRight = Vec3(1.0, 0.0, 0.0)
        self.base = base
        self.position = Vec3(0, 0, 0)
        self.camera = base.camera
        self.sensitivity = 0.5
        self.speed = 15  # Movement speed

        self.mouse = base.mouseWatcherNode
        self.camera.lookAt(20, 20, 20)

        self.__yaw = 0
        self.__pitch = 0



    def flightMovement(self, dt):
        velocity = Vec3(0, 0, 0)

        key_down = self.base.mouseWatcherNode.isButtonDown
        if key_down("a"):
            self.position -= self.camRight * self.speed * dt
        if key_down("d"):
            self.position += self.camRight * self.speed * dt
        if key_down("w"):
            self.position += self.camFront * self.speed * dt
        if key_down("s"):
            self.position -= self.camFront * self.speed * dt
        if key_down("space"):
            self.position += Vec3(0, 0, 1) * self.speed * dt
        if key_down("shift"):
            self.position -= Vec3(0, 0, 1) * self.speed * dt
        if key_down("control"):
            self.speed = 50

        self.camera.setPos(self.position)


    def cameraMovement(self):
        md = self.base.win.getPointer(0)
        display_center = (self.base.win.getXSize() // 2, self.base.win.getYSize() // 2)
        x = md.getX()
        y = md.getY()

        self.__yaw = self.__yaw - (x - display_center[0]) * self.sensitivity
        self.__pitch = self.__pitch - (y - display_center[1]) * self.sensitivity

        self.__pitch = max(-90, min(90, self.__pitch))
        self.camera.setHpr(self.__yaw, self.__pitch, 0)

        # Reset mouse position for continuous movement
        self.base.win.movePointer(0, display_center[0], display_center[1])

        self.camFront = self.camera.getQuat().getForward()
        self.camRight = self.camera.getQuat().getRight()

    def update_camera(self):
        clock = self.base.clock
        dt = clock.getDt()

        self.cameraMovement()
        self.flightMovement(dt)
        return True
