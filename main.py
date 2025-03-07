from direct.showbase.ShowBase import ShowBase
from panda3d.core import WindowProperties, ClockObject
from direct.task import Task
from camera import Camera  # Assuming your camera class is named Camera


class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.accept("escape", self.userExit)
        self.disableMouse()
        self.clock = ClockObject().getGlobalClock()
        
        # Initialize camera
        self.camera = Camera(self)
        
        # Load environment and example cube
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

        # Add the camera update to the task manager
        self.taskMgr.add(self.update, "update_task")

    def update(self, task):
        # This will be called every frame
        
        dt = self.clock.getDt()

        # Update the camera
        self.camera.update_camera()
        
        return Task.cont


game = Game()
game.run()
