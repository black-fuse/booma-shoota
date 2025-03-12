from direct.showbase.ShowBase import ShowBase
from panda3d.core import WindowProperties, ClockObject
from direct.task import Task
from camera import Camera  
from scenes import scene1, sceneTemplate, scene2


class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.accept("escape", self.userExit)
        self.disableMouse()
        self.clock = ClockObject().getGlobalClock()
        
        self.camera = Camera(self)
        
        #self.scene = scene1(self)
        #self.scene = sceneTemplate(self)
        self.scene = scene2(self)

        props = WindowProperties()
        props.setSize(800, 600)
        props.setTitle("really cool game Game")
        self.win.requestProperties(props)

        self.taskMgr.add(self.update, "update_task")

    def update(self, task):
        
        dt = self.clock.getDt()
        self.camera.update_camera()
        
        return Task.cont


game = Game()
game.run()
