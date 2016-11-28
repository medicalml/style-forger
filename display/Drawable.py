
class Drawable(object):
    def __init__(self):
        self._isHidden = False

    def draw(self, timePassed):
        pass

    def hide(self):
        self._isHidden = True

    def show(self):
        self.reset()
        self._isHidden = False

    def reset(self):
        pass
