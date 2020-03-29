from xdrawio.datatypes import Shape

class Page(Shape):
    r"""Page contains:
        - list of layers: dict with key=layer number, value=layer
        - each layer contains list of sorted teams
        - each team contains list of groups
        - each group contains list of modules
    """

    type = "page"

    def __init__(self):
        super().__init__()
        self.layers = {}    # layers of teams
        self.teams = {}     # dictionary of teams for quick access

    def initialize(self, mdls, data):
        """ initialize page data

        input:
        - list of modules with full information
        - configurations = data

        output:
        - Page.teams will contains all teams mentioned in input modules. 
            Each team will contains list of groups
            Each group will contains list of modules
        - Page.layers will contains all teams' layers
        """
        from xdrawio.datatypes import Team, Group

        for item in mdls:
            team_code = item.team
            team_info = data.teams[team_code]
            if team_code not in self.teams:
                t = Team()
                t.display_name = team_info["display_name"]
                t.style = team_info["style"]
                t.code = team_code
                t.order = team_info["sort_order"]
                self.teams[team_code] = t

            team = self.teams[team_code]

            layer = team_info["layer"]
            if layer not in self.layers:
                self.layers[layer] = []

            r_layer = self.layers[layer]
            if team not in r_layer:
                r_layer.append(team)

            group_code = item.group
            if group_code not in team.groups:
                g = Group()
                g.display_name = data.groups[group_code]["display_name"]
                g.code = group_code
                team.groups[group_code] = g
            group = team.groups[group_code]
            group.items.append(item)

    def flatten_tree(self):
        """ convert existing tree structure (team -> groups -> modules) into array of renderable items

        Example output

        >>> [team1,group1,m1,m2,group2,m3,m4,m5,team2,group3,m6]
        """
        all_items = []
        for team in self.teams.values():
            all_items.append(team)
            for group in team.groups.values():
                all_items.append(group)
                all_items = all_items + group.items
        
        return all_items

    def measure(self):
        for team in self.teams.values():
            w, h = team.measure()
            team.w = w
            team.h = h
