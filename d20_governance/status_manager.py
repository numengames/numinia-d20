class BotStatus:
    def __init__(self):
        self.operational = True

    def set_operational(self, status: bool):
        self.operational = status

    def is_operational(self):
        return self.operational
