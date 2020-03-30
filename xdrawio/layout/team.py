
from xdrawio.layout.parser import parseLayoutSpec
from xdrawio.layout.stack import FixLayout, HStack
from .group import GroupLayout

class TeamLayout(object):
    header_height = 100
    group_padding_left = 20
    group_padding_right = 20
    group_padding_bottom = 20
    team_padding_right = 80
    workgroup_width = 110
    workgroup_padding_right = 10
    def __init__(self, team, layoutspec):
        super().__init__()
        self.team = team
        self.layoutspec = layoutspec
        self.children = []
        for group in self.team.groups.values():
            self.children.append(GroupLayout(group))
        
        if self.layoutspec is not None:
            self.ls = parseLayoutSpec(self.layoutspec)
        else:
            # default layout
            self.ls = HStack()
            for group in self.team.groups.values():
                self.ls.items.append(FixLayout(group.code))

    def measure(self):
        # first mesure all children width and height
        for tl in self.children:
            tl.measure()

        # then measure the boundary to hold children
        self.ls.measure(self.team.groups)
        self.team.gbound.w = self.ls.w + self.group_padding_left + self.group_padding_right
        self.team.w = self.team.gbound.w + (self.workgroup_width + self.workgroup_padding_right) + self.team_padding_right
        self.team.gbound.h = self.ls.h + self.header_height + self.group_padding_bottom
        self.team.h = self.team.gbound.h

    def layout_children(self):
        # move workgroup
        move_workgroup_to(self.team.workgroup, self.team.x, self.team.y)

        # first calculate the position and dimension of all groups
        self.ls.layout_children(self.team.groups)

        # second move all groups to respective position, resize all group
        group_dict = self.ls.to_dict()
        self.team.gbound.x = self.team.x + self.workgroup_width + self.workgroup_padding_right
        self.team.gbound.y = self.team.y

        start_x = self.team.gbound.x + self.group_padding_left
        start_y = self.team.gbound.y + self.header_height
        for group in self.team.groups.values():
            g = group_dict[group.code]
            group.x = g.x + start_x
            group.y = g.y + start_y
            group.w = g.w
            group.h = g.h

        # third apply the layout process to every group
        for tl in self.children:
            tl.layout_children()


def move_workgroup_to(wg, start_x, start_y):
    wg[0]["x"] = start_x
    wg[0]["y"] = start_y

    offset_y = 40
    for i in range(1, 5):
        wgi = wg[i]
        wgi["x"] = start_x
        wgi["y"] = start_y + offset_y
        offset_y += wgi["h"]
