from direct.showbase.ShowBase import ShowBase
from panda3d.core import WindowProperties


class game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        # Set the window properties
        props = WindowProperties()
        props.setSize(800, 600)
        self.win.requestProperties(props)


game = game()
game.run()