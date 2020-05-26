import xdrawio.xutils

class Shape(object):
    type = "unknnown"
    def __init__(self):
        self.id = xdrawio.xutils.randomString()
        self.x = 0
        self.y = 0
        self.w = 0
        self.h = 0
        self.display_name = ""

    def __repr__(self):
        return "{" + "dp:'{}', type:{}, x:{}, y:{}, w:{}, h:{}".format(
            self.display_name, self.type, self.x, self.x, self.w, self.h
        ) + "}"
