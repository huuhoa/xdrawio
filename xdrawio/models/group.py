from xdrawio.models import Shape

class Group(Shape):
    def __init__(self):
        super().__init__()
        self.type = "group"
        self.items = []

