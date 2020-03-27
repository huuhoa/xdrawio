from xdrawio import randomString

class Shape(object):
    def __init__(self):
        self.id = randomString()
        self.x = 0
        self.y = 0
        self.w = 0
        self.h = 0
        self.display_name = ""
        self.type = "unknnown"
