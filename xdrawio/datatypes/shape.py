from xdrawio import randomString

class Shape(object):
    type = "unknnown"
    def __init__(self):
        self.id = randomString()
        self.x = 0
        self.y = 0
        self.w = 0
        self.h = 0
        self.display_name = ""

    def measure(self):
        """ performs measurement on Shape object to determine expected width and height """
        raise NotImplementedError

    def __repr__(self):
        return "{" + "dp:'{}', type:{}, x:{}, y:{}, w:{}, h:{}".format(
            self.display_name, self.type, self.x, self.x, self.w, self.h
        ) + "}"
