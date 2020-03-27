from xdrawio.datatypes import Shape

class Module(Shape):
    def __init__(self):
        super().__init__()
        self.type = "module"


class Team(Shape):
    def __init__(self):
        super().__init__()
        self.type = "team"
        self.groups = {}
        self.layer = 0
        self.style = ""
        self.order = 0
        self.code = ""

