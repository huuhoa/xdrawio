
class GroupLayout(object):
    header_height = 100
    item_height = 50
    item_width = 180
    item_padding_bottom = 10
    item_padding = 20
    group_padding_left = 20
    group_padding_right = 20
    group_padding_bottom = 20

    items_per_row = 3

    def __init__(self, group):
        super().__init__()
        self.group = group

    def measure(self):
        """Based on number of modules in group, determine w,h of the rectangle to hold all modules.
        Then set the group w,h to those values"""

        max_w = 0
        max_h = 0
        item_count = len(self.group.items)
        row = ((item_count + self.items_per_row - 1)/self.items_per_row).__int__()
        column = item_count % self.items_per_row
        if item_count >= self.items_per_row:
            column = self.items_per_row
        max_w = GroupLayout.item_width * column + GroupLayout.item_padding * (column - 1) + GroupLayout.group_padding_left + GroupLayout.group_padding_right
        max_h = GroupLayout.header_height + GroupLayout.item_height * row + GroupLayout.item_padding_bottom * (row - 1) + GroupLayout.group_padding_bottom

        self.group.w = max_w
        self.group.h = max_h

    def layout_children(self):
        """Based on current group's position, move all modules to the right position"""

        start_x = self.group.x + GroupLayout.group_padding_left
        y = self.group.y + self.group.h - GroupLayout.group_padding_bottom - GroupLayout.item_height
        column = 0
        x = start_x
        for item in self.group.items:
            item.x = x
            item.y = y
            column = (column + 1) % self.items_per_row
            if column == 0:
                y -= GroupLayout.item_height + GroupLayout.item_padding_bottom
                x = start_x
            else:
                x += GroupLayout.item_width + GroupLayout.item_padding
