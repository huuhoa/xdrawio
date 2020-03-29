
from xdrawio.layout.parser import parseLayoutSpec
from xdrawio.layout.stack import FixLayout, HStack
from .group import GroupLayout

group_padding_left = 20
group_padding_right = 20
group_padding_bottom = 20
header_height = 100

class TeamLayout(object):
    def __init__(self, team, layoutspec):
        super().__init__()
        self.team = team
        self.layoutspec = layoutspec
        
        if self.layoutspec is not None:
            self.ls = parseLayoutSpec(self.layoutspec)
        else:
            # default layout
            self.ls = HStack()
            for group in self.team.groups.values():
                self.ls.items.append(FixLayout(group.code))

    def measure(self):
        self.ls.layout_children(self.team.groups)
        self.team.w = self.ls.w + group_padding_left + group_padding_right + 200
        self.team.h = self.ls.h + header_height + group_padding_bottom

    def layout_children(self):
        # move workgroup
        move_workgroup_to(self.team.workgroup, self.team.x, self.team.y)

        start_x = self.team.x + group_padding_left + 120
        max_h = 0
        for group in self.team.groups.values():
            max_h = max(max_h, group.h)

        # group placement

        self.ls.layout_children(self.team.groups)
        self.team.w = self.ls.w + group_padding_left + group_padding_right + 200
        # self.team.h = self.ls.h + header_height + group_padding_bottom
        # print(ls)

        group_dict = self.ls.to_dict()
        # print(group_dict)

        start_y = self.team.y + header_height
        for group in self.team.groups.values():
            g = group_dict[group.code]
            group.x = g.x + start_x
            group.y = g.y + start_y
            group.w = g.w
            group.h = g.h

        # for group in self.team.groups.values():
        #     start_y = self.team.y + self.team.h - group_padding_bottom - max_h
        #     group.x = start_x
        #     group.y = start_y
        #     group.h = max_h

        #     start_x = start_x + group.w + group_padding_right

        for group in self.team.groups.values():
            gl = GroupLayout(group)
            gl.layout_children()


def move_workgroup_to(wg, start_x, start_y):
    wg[0]["x"] = start_x
    wg[0]["y"] = start_y

    offset_y = 40
    for i in range(1, 5):
        wgi = wg[i]
        wgi["x"] = start_x
        wgi["y"] = start_y + offset_y
        offset_y += wgi["h"]
