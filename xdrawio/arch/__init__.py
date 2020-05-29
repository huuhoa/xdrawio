from xdrawio.arch.dataloader import read_data
from xdrawio.arch.layout.stacklayout import FixLayout, GridLayout
from xdrawio.arch.layout.stacklayout import HStack, VStack
from xdrawio.arch.layout.layoutparser import parseLayoutSpec


def load_data(path):
    import xdrawio.arch.layout
    import json

    mdls, d = read_data(path)

    wgs_byteam = xdrawio.arch.layout.layout_workgroup(d.workgroups)

    page = xdrawio.arch.datatypes.Page()
    page.initialize(mdls, d, wgs_byteam)

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
        ltree = create_team_node(team, d.layoutspec, d.configurations)
        # 2.2 add team spec for layout tree
        ltree.add_attribute({
            'padding': {'top': 100, 'left': 10, 'bottom': 10, 'right': 10},
            'margin': {'all': 10},
            'display_name': team_info['display_name'],
            'class': 'team',
            'style': d.configurations[team_info['style']]
        })

        # 2.3 replace layout tree with team node in root
        replace_node(ls, team.code, ltree)

    print(json.dumps(ls.dumps(), sort_keys=True, indent=2))

    return [], {}


def replace_node(root, code, new_node):
    root.replace(code, new_node)


def create_team_node(team, layoutspec, configs):
    # step 1: create layout specification at team level, leaf nodes are groups
    spec = layoutspec.get(team.code, None)
    if spec is not None:
        ls = parseLayoutSpec(spec)
    else:
        # default layout
        ls = HStack()
        for group in team.groups.values():
            ls.items.append(FixLayout(group.code, 0, 0))

    # step 2: create group tree, then replace the leaf node above
    for group in team.groups.values():
        gn = create_group_node(group, configs)
        replace_node(ls, group.code, gn)

    return ls


def create_group_node(group, configs):
    # default layout
    ls = VStack()
    ls.code = group.code
    max_items = 3
    if len(group.items) > 9:
        max_items = 4

    for i in range(0, len(group.items), max_items):
        hs = HStack()
        for index in range(i, min(i+max_items, len(group.items))):
            m = group.items[index]
            item = FixLayout(m.display_name, m.w, m.h)
            item.add_attribute({
                'display_name': m.display_name,
                'margin': {'all': 10},
                'extra': {
                    'wg_style': configs[m.wg_stype],
                    'status_style': configs[m.status],
                },
                'class': 'module',
            })
            hs.items.append(item)
        ls.items.append(hs)

    ls.add_attribute({
        'padding': {'top': 100, 'left': 10, 'bottom': 10, 'right': 10},
        'margin': {'all': 10},
        'class': 'group',
        'flex-direction': 'column-reverse',
        'display_name': group.display_name,
    })
    return ls
