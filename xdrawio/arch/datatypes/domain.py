from xdrawio.arch.datatypes import Shape


class Domain(Shape):
    type = "team"

    def __init__(self):
        super().__init__()
        self.groups = {}
        self.workgroup = {}
        self.gbound = Shape()
        self.gbound.type = self.type
