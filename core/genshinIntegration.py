import genshinstats as gs


class Integration:
    active: bool = False

    def setOn(self):
        self.active = True

    def setOff(self):
        self.active = False


gs.set_cookie_auto()
