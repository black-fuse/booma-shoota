from direct.showbase.ShowBase import ShowBase
from panda3d.core import WindowProperties, ClockObject
from direct.task import Task

class sceneTemplate:
    def __init__(self,base):
        self.base = base
        self.objList = []

        self.floor = self.create_object("models/box", (0, 0, -2), (100, 100, 1))
    
    def create_object(self, model_path="models/box", position=(0,0,0), scale=(1,1,1), texture='Textures\white.jpg'):
        obj = self.base.loader.loadModel(model_path)
        obj.reparentTo(self.base.render)
        obj.setPos(position)
        obj.setScale(scale)
        texture = self.base.loader.loadTexture(texture)
        obj.setTexture(texture)
        self.objList.append(obj)
        return obj
    
    def destroy_object(self, obj):
        obj.removeNode()

    def destroy_all_objects(self):
        for obj in self.objList:
            obj.removeNode()

class scene1(sceneTemplate):
    def __init__(self, base):
        self.base = base
        self.destroy_object(self.floor)

        env = self.base.loader.loadModel("models/environment")
        env.reparentTo(self.base.render)

        example_cube = self.base.loader.loadModel("models/box")
        example_cube.reparentTo(self.base.render)
        
        example_cube.setPos(0, 0, 0)
        example_cube.setScale(2, 2, 2)
        example_cube.setHpr(45, 45, 45)

class scene2(sceneTemplate):
    def __init__(self, base):
        super().__init__(base)
        self.destroy_object(self.floor)
        self.box = self.create_object("models/box", (0, 0, -2), (100, 100, 1),texture='Textures/red.jpg')

