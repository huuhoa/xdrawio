item_height = 50
item_width = 180
padding_bottom = 10
padding_left = 20
padding_right = 20
group_padding_bottom = 20

class GroupLayout(object):
    def __init__(self, group):
        super().__init__()
        self.group = group

    def layout_children(self):
        start_x = self.group.x + padding_left
        y = self.group.y + self.group.h - group_padding_bottom - item_height
        column = 0
        x = start_x
        for item in self.group.items:
            item.x = x
            item.y = y
            column = (column + 1) % 3
            if column == 0:
                y -= item_height + padding_bottom
                x = start_x
            else:
                x += item_width + padding_left
