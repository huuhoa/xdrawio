
from xdrawio.layout.parser import parseLayoutSpec
from xdrawio.layout.team import TeamLayout

class PageLayout(object):
    def __init__(self, page, layoutspec):
        super().__init__()
        self.page = page
        self.layoutspec = layoutspec
        self.children = []
        if "CP" in self.layoutspec:
            self.ls = parseLayoutSpec(self.layoutspec.get("CP"))

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
        self.ls.layout_children(self.page.teams)
        # print(self.ls)

    def layout_children(self):
        wg_padding = 180

        # second pass, rebalance teams, make sure all teams have equal height
        self.ls.layout_children(self.page.teams)
        team_dict = self.ls.to_dict()
        # print(team_dict)

        start_x = 80
        start_y = 300
        for team in self.page.teams.values():
            t = team_dict[team.code]
            team.x = t.x + start_x
            team.y = t.y + start_y
            team.w = t.w
            team.h = t.h

        # for l in sorted(self.page.layers.keys(), reverse = True):
        #     start_x = 120 + 80
        #     self.distribute_horizontal(self.page.layers[l], start_x, group_padding_right + wg_padding)

        #     max_h = 0
        #     for team in self.page.layers[l]:
        #         max_h = max(max_h, team.h)

        #     for team in self.page.layers[l]:
        #         start_y = max(team.y, start_y)
        #         team.y = start_y
        #         team.h = max_h
        
        #     start_y = start_y + max_h + group_padding_bottom * 3

        # third pass, rebalance groups, make sure all groups have equal height
        for tl in self.children:
            tl.layout_children()
