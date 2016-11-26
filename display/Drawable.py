
class Drawable(object):
    def __init__(self):
        self.isHidden = False

    def draw(self, timePassed):
        pass

    def hide(self):
        self.isHidden = True

    def show(self):
        self.isHidden = False
