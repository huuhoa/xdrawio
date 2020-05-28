from xdrawio.arch.dataloader import read_data
import xdrawio
from xdrawio.arch.layout.stacklayout import FixLayout, GridLayout, HStack, VStack
from xdrawio.arch.layout.layoutparser import parseLayoutSpec

def load_data(path):
    import xdrawio.arch.layout
    import json

    mdls, d = read_data(path)

    wgs_byteam = xdrawio.arch.layout.layout_workgroup(d.workgroups)

    page = xdrawio.arch.datatypes.Page()
    page.initialize(mdls, d, wgs_byteam)

    root = {
        'id': 'root',
        'type': 'root_view',
        'width': 10000,
        'height': 10000,
        'children': [],
    }

    # Step 1: layout spec for root
    spec = d.layoutspec.get("CP", None)
    if spec is not None:
        ls = parseLayoutSpec(spec)
    else:
        # default layout
        ls = HStack()
        for team in page.teams.values():
            ls.items.append(FixLayout(team.code, 0, 0))

    # Step 2: layout spec for team
    for team in page.teams.values():
        team_info = d.teams[team.code]
        # 2.1 layout spec for team, result a layout tree
        ltree = create_team_node(team, d.layoutspec)
        # 2.2 add team spec for layout tree
        ltree.add_attribute({
            'padding': { 'top': 100, 'left': 10, 'bottom': 10, 'right': 10 },
            'margin': { 'all': 10 },
            'display_name': team_info['display_name'],
            "class": "team"
        })

        # 2.3 replace layout tree with team node in root
        replace_node(ls, team.code, ltree)

    # root['children'].append(t)

    print(json.dumps(ls.dumps(), sort_keys=True, indent=2))
    # print(json.dumps(root))

    return [], {}

    xdrawio.arch.layout.create_layout(page, wgs_byteam, d)
    # flat out
    all_items = page.flatten_tree()

    return all_items, d.configurations


def replace_node(root, code, new_node):
    root.replace(code, new_node)

    
def create_team_node(team, layoutspec):
    spec = layoutspec.get(team.code, None)
    if spec is not None:
        ls = parseLayoutSpec(spec)
    else:
        # default layout
        ls = HStack()
        for group in team.groups.values():
            ls.items.append(FixLayout(group.code, 0, 0))

    for group in team.groups.values():
        gn = create_group_node(group)
        replace_node(ls, group.code, gn)

    return ls
    # children = ls.dumps()
    # t = {
    #     'id': xdrawio.xutils.randomString(),
    #     'type': 'team',
    #     'width': 10000,
    #     'height': 10000,
    #     'children': children,
    #     # 'data': {
    #     #     'display_name': team['display_name'],
    #     # }
    # }
    # return t


def create_group_node(group):
    # default layout
    ls = GridLayout(group.code)
    max_items = 3
    if len(group.items) > 9:
        max_items = 4
    max_width = 20*2 + 180 * max_items + 20 * (max_items - 1)

    number_row = len(group.items) / max_items
    # vs = VStack()
    vs = ls
    for i in range(0, len(group.items), max_items):
        hs = HStack()
        for index in range(i, min(i+max_items, len(group.items))):
            m = group.items[index]
            item = FixLayout(m.display_name, m.w, m.h)
            item.add_attribute({
                'display_name': m.display_name,
                'margin': { 'all': 10 },
            })
            hs.items.append(item)
        vs.items.append(hs)
    # ls.items.append(vs)
    ls.add_attribute({
        'padding': { 'top': 100, 'left': 10, 'bottom': 10, 'right': 10 },
        'margin': { 'all': 10 },
        'class': 'group',
        # 'max-width': max_width,
        # 'align-items': 'flex-start',
        # 'align-self': 'flex-start',
        # 'align-content': 'flex-start',
        'flex-direction': 'column-reverse',
        'display_name': group.display_name,
    })
    return ls
