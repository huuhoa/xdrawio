from xdrawio.arch.datatypes import Shape


class Page(Shape):
    r"""Page contains:
        - list of domains
        - each team contains list of groups
        - each group contains list of modules
    """

    type = "page"

    def __init__(self):
        super().__init__()
        self.domains = {}     # dictionary of domains for quick access

    def initialize(self, mdls, data, wgs_byteam):
        """ initialize page data

        input:
        - list of modules with full information
        - configurations = data

        output:
        - Page.domains will contains all domains mentioned in input modules.
            Each team will contains list of groups
            Each group will contains list of modules
        - Page.layers will contains all domains' layers
        """
        from xdrawio.arch.datatypes import Domain, Group

        for item in mdls:
            team_code = item.team
            team_info = data.domains[team_code]
            if team_code not in self.domains:
                t = Domain()
                t.gbound.display_name = team_info['Domain Name']
                t.gbound.style = team_info['Style']
                t.code = team_code
                t.workgroup = wgs_byteam[team_code]
                self.domains[team_code] = t

            team = self.domains[team_code]

            group_code = item.group
            if group_code not in team.groups:
                g = Group()
                g.display_name = data.groups[group_code]["Group Name"]
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
        for team in self.domains.values():
            all_items.append(team.gbound)
            for wg in team.workgroup.values():
                all_items.append(wg)
            for group in team.groups.values():
                all_items.append(group)
                all_items = all_items + group.items

        # print(all_items)
        return all_items
