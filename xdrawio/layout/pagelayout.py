
from .layoutparser import parseLayoutSpec
from .teamlayout import TeamLayout

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

    def measure(self):
        # first mesure all children width and height
        for tl in self.children:
            tl.measure()

        # then measure the boundary to hold children
        self.ls.measure(self.page.teams)

    def layout_children(self):
        # first calculate the position and dimension of all teams
        self.ls.layout_children(self.page.teams)
        team_dict = self.ls.to_dict()
        # print(team_dict)

        # second move all teams to respective position, resize all team
        start_x = 80
        start_y = 300
        for team in self.page.teams.values():
            t = team_dict[team.code]
            team.x = t.x + start_x
            team.y = t.y + start_y
            team.w = t.w
            team.h = t.h

        # third apply the layout process to every team
        for tl in self.children:
            tl.layout_children()
