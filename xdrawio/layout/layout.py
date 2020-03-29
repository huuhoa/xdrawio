import xdrawio
from .parser import ParseSpec
from xdrawio.layout.stack import FixLayout, HStack

header_height = 100
item_height = 50
item_width = 180
padding_bottom = 10
padding_left = 20
padding_right = 20
group_padding_left = 20
group_padding_right = 20
group_padding_bottom = 20


def move_workgroup_to(wg, start_x, start_y):
    wg[0]["x"] = start_x
    wg[0]["y"] = start_y

    offset_y = 40
    for i in range(1, 5):
        wgi = wg[i]
        wgi["x"] = start_x
        wgi["y"] = start_y + offset_y
        offset_y += wgi["h"]


def layout_workgroup(wgs):
    height_lut = [30, 40, 50, 60, 70, 90, 110, 120, 140, 150, 160, 170]
    by_team = {}
    for wg in wgs.values():
        if wg["team"] not in by_team:
            by_team[wg["team"]] = { 
                0: {},
                1: {},
                2: {},
                3: {},
                4: {},
            }
        team = by_team[wg["team"]]
        team[wg["type"]] = wg

    # create layout for each team
    for team in by_team.values():
        for i in range(5):
            ti = team[i]
            ti["w"] = 110
            ti["h"] = height_lut[len(ti.get("members", []))]    # minimum height for empty
            ti["style"] = "WGStyle%d" % i
            ti["type"] = "wg"
            ti["id"] = xdrawio.randomString()
            ti["display_name"] = "&lt;br/&gt;".join(ti.get("members", ""))
        
        # recaliberate team 0 height
        h = 0
        for i in range(1, 5):
            h += team[i]["h"]
        team[0]["h"] = h
        team[0]["display_name"] = "Leader: %s" % team[0]["display_name"]

        # start_x = 100
        # start_y = 200
        # move_workgroup_to(team, start_x, start_y)
        # print(team)

    return by_team

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


class TeamLayout(object):
    def __init__(self, team, layoutspec):
        super().__init__()
        self.team = team
        self.layoutspec = layoutspec
        
        if self.layoutspec is not None:
            self.ls = ParseSpec(self.layoutspec)
        else:
            # default layout
            self.ls = HStack()
            for group in self.team.groups.values():
                self.ls.items.append(FixLayout(group.code))

    def measure(self):
        self.ls.layout_children(self.team.groups)
        self.team.w = self.ls.w + group_padding_left + group_padding_right
        self.team.h = self.ls.h + header_height + group_padding_bottom

    def layout_children(self):
        start_x = self.team.x + group_padding_left
        max_h = 0
        for group in self.team.groups.values():
            max_h = max(max_h, group.h)

        # group placement

        self.ls.layout_children(self.team.groups)
        self.team.w = self.ls.w + group_padding_left + group_padding_right
        self.team.h = self.ls.h + header_height + group_padding_bottom
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


class PageLayout(object):
    def __init__(self, page, layoutspec):
        super().__init__()
        self.page = page
        self.layoutspec = layoutspec
        self.children = []
        for team in self.page.teams.values():
            self.children.append(TeamLayout(team, self.layoutspec.get(team.code)))

    def distribute_horizontal(self, items, start_x, padding):
        # sort items by sort order
        items.sort(key=lambda x: x.order)
        for item in items:
            item.x = start_x
            start_x += item.w + padding

    def measure(self):
        self.page.measure()
        for tl in self.children:
            tl.measure()

    def layout_children(self):
        wg_padding = 180

        # second pass, rebalance teams, make sure all teams have equal height
        start_y = 300
        for l in sorted(self.page.layers.keys(), reverse = True):
            start_x = 120 + 80
            self.distribute_horizontal(self.page.layers[l], start_x, group_padding_right + wg_padding)

            max_h = 0
            for team in self.page.layers[l]:
                max_h = max(max_h, team.h)

            for team in self.page.layers[l]:
                start_y = max(team.y, start_y)
                team.y = start_y
                team.h = max_h
        
            start_y = start_y + max_h + group_padding_bottom * 3

        # third pass, rebalance groups, make sure all groups have equal height
        for tl in self.children:
            tl.layout_children()


def create_layout(page, wgs_byteam, data):
    from xdrawio.datatypes import Team, Group

    # first pass, layout all items inside group
    pl = PageLayout(page, data.layoutspec)
    pl.measure()
    pl.layout_children()
    # fourth pass, move working group to top-left of each team
    for team in page.teams.values():
        move_workgroup_to(wgs_byteam[team.code], team.x - 120, team.y)
