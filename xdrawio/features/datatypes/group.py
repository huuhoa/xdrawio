from xdrawio.features.datatypes import Shape

class Group(Shape):
    type = "group"

    def __init__(self):
        super().__init__()
        self.code = ""
        self.items = []

