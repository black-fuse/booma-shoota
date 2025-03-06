from direct.showbase.ShowBase import ShowBase
from panda3d.core import WindowProperties
from direct.task import Task
from camera import camera


class game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.accept("escape", self.userExit)
        self.disableMouse()
        self.camera = camera(self)
        env = self.loader.loadModel("models/environment")
        env.reparentTo(self.render)


        example_cube = self.loader.loadModel("models/box")
        example_cube.reparentTo(self.render)

        # Set the position of the cube
        example_cube.setPos(0, 0, 0)
        example_cube.setScale(2, 2, 2)
        example_cube.setHpr(45, 45, 45)
        

        # Set the window properties
        props = WindowProperties()
        props.setSize(800, 600)
        self.win.requestProperties(props)

    def update(self, task):
        clock = self.globalClock
        dt = clock.getDt()


        return Task.cont

game = game()
game.run()