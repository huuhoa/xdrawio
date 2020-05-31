from typing import Dict

from xdrawio.arch.dataloader import Data
from xdrawio.arch.datatypes import Domain, Group, Page
from xdrawio.arch.layout.layoutparser import parseLayoutSpec
from xdrawio.arch.layout.stacklayout import FixLayout, Layout
from xdrawio.arch.layout.stacklayout import HStack


def generate_layout_spec_level_1(d: Data, page: Page):
    # Step 1: layout spec for root
    spec = d.layoutspec.get("ROOT", None)
    if spec is not None:
        ls = parseLayoutSpec(spec)
    else:
        # default layout
        ls = HStack()
        for team in page.domains.values():
            ls.items.append(FixLayout(team.code, 0, 0))

    # Step 2: layout spec for team
    for team in page.domains.values():
        team_info = d.domains[team.code]
        # 2.1 layout spec for team, result a layout tree
        ltree = create_team_node(team, d.layoutspec, d.configurations)
        # 2.2 add team spec for layout tree
        ltree.add_attribute({
            'padding': {'top': 100, 'left': 10, 'bottom': 10, 'right': 10},
            'margin': {'all': 10},
            'display_name': team_info['Domain Name'],
            'class': 'domain',
            'style': d.configurations[team_info['Style']]
        })

        # 2.3 replace layout tree with team node in root
        replace_node(ls, team.code, ltree)

    return ls.dumps()


def replace_node(root: Layout, code: str, new_node: Layout):
    root.replace(code, new_node)


def create_team_node(team: Domain, layoutspec, configs):
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


def create_group_node(group: Group, configs: Dict[str, str]) -> Layout:
    # default layout
    ls = FixLayout(group.code, 500, 150)
    ls.add_attribute({
        'display_name': group.display_name,
        'padding': {'top': 100, 'left': 10, 'bottom': 10, 'right': 10},
        'margin': {'all': 10},
        'class': 'group',
    })
    return ls
