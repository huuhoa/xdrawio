from xdrawio.datatypes import Shape

class Team(Shape):
    header_height = 100
    padding_bottom = 20
    padding_horizontal = 20

    type = "team"

    def __init__(self):
        super().__init__()
        self.groups = {}
        self.layer = 0
        self.style = ""
        self.order = 0
        self.code = ""

    def measure(self):
        max_w = 0
        max_h = 0
        for group in self.groups.values():
            w, h = group.measure()
            max_w = max_w + w
            max_h = max(max_h, h)
            group.w = w
            group.h = h

        group_count = len(self.groups)
        max_w = max_w + Team.padding_horizontal * (2 + group_count - 1)
        max_h = max_h + Team.header_height + Team.padding_bottom
        return max_w, max_h

