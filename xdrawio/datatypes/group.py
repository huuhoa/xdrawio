from xdrawio.datatypes import Shape

class Group(Shape):
    header_height = 100
    item_height = 50
    item_width = 180
    item_padding_bottom = 10
    item_padding = 20
    group_padding_left = 20
    group_padding_right = 20
    group_padding_bottom = 20

    type = "group"

    def __init__(self):
        super().__init__()
        self.code = ""
        self.items = []

    def measure(self):
        max_w = 0
        max_h = 0
        item_count = len(self.items)
        row = ((item_count + 2)/3).__int__()
        column = item_count % 3
        if item_count >= 3:
            column = 3
        max_w = Group.item_width * column + Group.item_padding * (column - 1) + Group.group_padding_left + Group.group_padding_right
        max_h = Group.header_height + Group.item_height * row + Group.item_padding_bottom * (row - 1) + Group.group_padding_bottom

        return max_w, max_h
