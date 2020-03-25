#!/usr/bin/env python3

from jinja2 import Environment, FileSystemLoader, select_autoescape

import random
import string

# teams = {
#     "DP": { "layer": 1, "display_name": "Data Report &amp; Platform" },
#     "AD": { "layer": 2, "display_name": "Accounting Domain" },
#     "PP": { "layer": 2, "display_name": "Promotion Platform" },
#     "PE": { "layer": 3, "display_name": "Payment Engine" },
#     "UD": { "layer": 3, "display_name": "User Domain" },
#     "MT": { "layer": 3, "display_name": "Transfer Domain" },
#     "CC": { "layer": 3, "display_name": "Common Services" },
#     "TC": { "layer": 4, "display_name": "Telco" },
#     "GW": { "layer": 4, "display_name": "Payment Gateway" },
# }

items = [
    {
        "wg_type": 1,
        "display_name": "User Assets",
        "status": 0,
        "type": "module",
        "team": "UD",
        "group": "User Products",
        "sub_group": "",
    },
    {
        "wg_type": 2,
        "display_name": "User Limitation",
        "status": 0,
        "type": "module",
        "team": "UD",
        "group": "User Products",
        "sub_group": "",
    },
    {
        "wg_type": 3,
        "display_name": "User KYC",
        "status": 0,
        "type": "module",
        "team": "UD",
        "group": "User Products",
        "sub_group": "",
    },
    {
        "wg_type": 1,
        "display_name": "User Profile",
        "status": 2,
        "type": "module",
        "team": "UD",
        "group": "User Products",
        "sub_group": "",
    },
    {
        "wg_type": 1,
        "display_name": "User Verification",
        "status": 2,
        "type": "module",
        "team": "UD",
        "group": "Back Office",
        "sub_group": "",
    },
    {
        "wg_type": 3,
        "display_name": "Transaction History",
        "status": 1,
        "type": "module",
        "team": "UD",
        "group": "Back Office",
        "sub_group": "",
    },
    {
        "wg_type": 1,
        "display_name": "User Assets",
        "status": 0,
        "type": "module",
        "team": "UD",
        "group": "Back Office",
        "sub_group": "",
    },
    {
        "wg_type": 2,
        "display_name": "User Limitation",
        "status": 0,
        "type": "module",
        "team": "UD",
        "group": "User Products",
        "sub_group": "",
    },
    {
        "wg_type": 3,
        "display_name": "User KYC",
        "status": 0,
        "type": "module",
        "team": "UD",
        "group": "User Products",
        "sub_group": "",
    },
    {
        "wg_type": 1,
        "display_name": "User Profile",
        "status": 2,
        "type": "module",
        "team": "DP",
        "group": "Back Office",
        "sub_group": "",
    },
    {
        "wg_type": 1,
        "display_name": "User Verification",
        "status": 2,
        "type": "module",
        "team": "AD",
        "group": "User Products",
        "sub_group": "",
    },
    {
        "wg_type": 3,
        "display_name": "Transaction History",
        "status": 1,
        "type": "module",
        "team": "UD",
        "group": "User Products",
        "sub_group": "",
    },
    {
        "wg_type": 3,
        "display_name": "Bank Binding",
        "status": 1,
        "type": "module",
        "team": "UD",
        "group": "User Products",
        "sub_group": "PCI DSS",
    },
    {
        "wg_type": 3,
        "display_name": "User Core (User Info)",
        "status": 1,
        "type": "module",
        "team": "UD",
        "group": "User Core",
        "sub_group": "",
    },
    {
        "wg_type": 3,
        "display_name": "BIM (Bank Info)",
        "status": 1,
        "type": "module",
        "team": "UD",
        "group": "User Core",
        "sub_group": "PCI DSS",
    },
    {
        "wg_type": 1,
        "display_name": "User Assets",
        "status": 0,
        "type": "module",
        "team": "DP",
        "group": "Back Office",
        "sub_group": "",
    },
    {
        "wg_type": 2,
        "display_name": "User Limitation",
        "status": 0,
        "type": "module",
        "team": "AD",
        "group": "Accounting System",
        "sub_group": "",
    },
    {
        "wg_type": 2,
        "display_name": "User Limitation",
        "status": 0,
        "type": "module",
        "team": "AD",
        "group": "Reconciliation",
        "sub_group": "",
    },
    {
        "wg_type": 2,
        "display_name": "User Limitation",
        "status": 0,
        "type": "module",
        "team": "AD",
        "group": "Reconciliation",
        "sub_group": "",
    },
    {
        "wg_type": 2,
        "display_name": "User Limitation",
        "status": 0,
        "type": "module",
        "team": "AD",
        "group": "Reconciliation",
        "sub_group": "",
    },
    {
        "wg_type": 2,
        "display_name": "User Limitation",
        "status": 0,
        "type": "module",
        "team": "AD",
        "group": "Reconciliation",
        "sub_group": "",
    },
    {
        "wg_type": 2,
        "display_name": "User Limitation",
        "status": 0,
        "type": "module",
        "team": "AD",
        "group": "FA BackOffice",
        "sub_group": "",
    },
    {
        "wg_type": 2,
        "display_name": "User Limitation",
        "status": 0,
        "type": "module",
        "team": "AD",
        "group": "FA BackOffice",
        "sub_group": "",
    },
    {
        "wg_type": 2,
        "display_name": "User Limitation",
        "status": 0,
        "type": "module",
        "team": "AD",
        "group": "FA BackOffice",
        "sub_group": "",
    },
    {
        "wg_type": 2,
        "display_name": "User Limitation",
        "status": 0,
        "type": "module",
        "team": "AD",
        "group": "FA BackOffice",
        "sub_group": "",
    },
    {
        "wg_type": 2,
        "display_name": "User Limitation",
        "status": 0,
        "type": "module",
        "team": "AD",
        "group": "FA BackOffice",
        "sub_group": "",
    },
    {
        "wg_type": 2,
        "display_name": "User Limitation",
        "status": 0,
        "type": "module",
        "team": "AD",
        "group": "FA BackOffice",
        "sub_group": "",
    },
    {
        "wg_type": 2,
        "display_name": "User Limitation",
        "status": 0,
        "type": "module",
        "team": "AD",
        "group": "FA BackOffice",
        "sub_group": "",
    },
    {
        "wg_type": 2,
        "display_name": "User Limitation",
        "status": 0,
        "type": "module",
        "team": "AD",
        "group": "FA BackOffice",
        "sub_group": "",
    },
    {
        "wg_type": 3,
        "display_name": "User KYC",
        "status": 0,
        "type": "module",
        "team": "UD",
        "group": "User Products",
        "sub_group": "",
    },
    {
        "wg_type": 1,
        "display_name": "User Profile",
        "status": 2,
        "type": "module",
        "team": "MT",
        "group": "User Products",
        "sub_group": "",
    },
    {
        "wg_type": 1,
        "display_name": "User Verification",
        "status": 2,
        "type": "module",
        "team": "MT",
        "group": "User Products",
        "sub_group": "",
    },
    {
        "wg_type": 3,
        "display_name": "Transaction History",
        "status": 1,
        "type": "module",
        "team": "MT",
        "group": "User Products",
        "sub_group": "",
    },
    {
        "wg_type": 3,
        "display_name": "Bank Binding",
        "status": 1,
        "type": "module",
        "team": "MT",
        "group": "User Products",
        "sub_group": "PCI DSS",
    },
    {
        "wg_type": 3,
        "display_name": "User Core (User Info)",
        "status": 1,
        "type": "module",
        "team": "MT",
        "group": "User Core",
        "sub_group": "",
    },
    {
        "wg_type": 3,
        "display_name": "BIM (Bank Info)",
        "status": 1,
        "type": "module",
        "team": "MT",
        "group": "User Core",
        "sub_group": "PCI DSS",
    },
]

header_height = 100
item_height = 50
item_width = 180
padding_bottom = 10
padding_left = 20
padding_right = 20
group_padding_left = 20
group_padding_right = 20
group_padding_bottom = 20


def read_team_data(data):
    td = {}
    header = None
    for row in data:
        # Get a list of all columns in each row
        cols = []
        for col in row:
            cols.append(col.value)
        
        if header is None:
            header = cols
        else:
            td[cols[0]] = { 
                "layer": cols[2],
                "display_name": cols[1].replace("&", "&amp;"),
            }
    return td


def read_workgroup_data(data):
    wgs = {}
    header = None
    for row in data:
        # Get a list of all columns in each row
        cols = []
        for col in row:
            cols.append(col.value)
        
        if header is None:
            header = cols
        else:
            wgs[cols[0]] = {
                "type": cols[1],
                "team": cols[2],
                "members": cols[3],
            }
    return wgs


def read_module_data(data):
    mdls = []
    header = None
    for row in data:
        # Get a list of all columns in each row
        cols = []
        for col in row:
            cols.append(col.value)
        
        if header is None:
            header = cols
        else:
            mdl = {
                "team": cols[0],
                "group": cols[1],
                "display_name": cols[2],
                "wg_type": cols[3],
                "status": convert_status(cols[4]),
                "sub_group": cols[5],
                "type": "module",
            }
            mdls.append(mdl)
    return mdls


def convert_status(status):
    if status == "Not Started":
        return 0
    if status == "In Progress":
        return 1
    if status == "Completed":
        return 2
    
    return 100


def read_data(file_path):
    # Reading an excel file using Python 
    import openpyxl

    # To open Workbook 
    wb = openpyxl.load_workbook(file_path) 
    ws = wb["Teams"]
    
    # For row 0 and column 0 
    for tbl in ws._tables:
        # print(tbl.name)
        # Grab the 'data' from the table
        data = ws[tbl.ref]
        if tbl.name == "Teams":
            teams = read_team_data(data)

        if tbl.name == "WorkGroups":
            wgs = read_workgroup_data(data)
            # print(wgs)

        if tbl.name == "Modules":
            mdls = read_module_data(data)
            # print(mdls)

    for mdl in mdls:
        mdl["wg_type"] = wgs[mdl["wg_type"]]["type"]

    return mdls, teams, wgs


def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


def layout_items(items, start_x, start_y):
    x = start_x
    y = start_y
    column = 0
    row = 0
    width = 0
    height = 0
    overflow_w = 0
    for item in items:
        item["x"] = x
        item["y"] = y
        column = (column + 1) % 3
        if column == 0:
            row = row + 1
            y += item_height + padding_bottom
            x = start_x
            overflow_w = item_width
        else:
            x += item_width + padding_left

        width = max(width, x - start_x)
        height = max(height, y - start_y)
    
    if column == 0:
        # full row
        height -= item_height + padding_bottom
    if overflow_w == 0 and column != 0:
        overflow_w = -padding_left

    width += overflow_w
    height += item_height

    return width, height


def relayout_items(items, start_x, end_y):
    y = end_y
    column = 0
    min_x = 10000000
    for item in items:
        min_x = min(min_x, item["x"])

    offset_x = min_x - start_x
    for item in items:
        item["x"] = item["x"] - offset_x
        item["y"] = y - item_height
        column = (column + 1) % 3
        if column == 0:
            y -= item_height + padding_bottom


def distribute_horizontal(items, start_x, padding):
    for item in items:
        item["x"] = start_x
        start_x += item["w"] + padding


def create_layout(items):
    root = {}
    layers = {}
    for item in items:
        team_code = item["team"]
        team_info = teams[team_code]
        if team_code not in root:
            root[team_code] = {
                "id": randomString(),
                "display_name": team_info["display_name"],
                "type": "team",
                "groups": {},
            }
        team = root[team_code]

        layer = team_info["layer"]
        if layer not in layers:
            layers[layer] = []

        r_layer = layers[layer]
        if team not in r_layer:
            r_layer.append(team)

        group_code = item["group"]
        if group_code not in team["groups"]:
            team["groups"][group_code] = {
                "id": randomString(),
                "display_name": group_code,
                "type":"group",
                "items":[],
            }
        group = team["groups"][group_code]
        item["id"] = randomString()
        group["items"].append(item)

    start_x = 120
    start_y = 100

    # first pass, layout all items inside group
    for team in root.values():
        team["x"] = start_x
        team["y"] = start_y
        max_w = 0
        max_h = 0
        for group in team["groups"].values():
            start_x = start_x + group_padding_left
            g_y = start_y + header_height
            w, h = layout_items(group["items"], start_x + padding_left, g_y + header_height)
            group["x"] = start_x
            group["y"] = g_y
            g_w =  w + group_padding_left + group_padding_right
            g_h = h + header_height + group_padding_bottom
            group["w"] = g_w
            group["h"] = g_h
            start_x = start_x + g_w
            max_w = max(max_w, start_x - team["x"])
            max_h = max(max_h, g_h)
        team["w"] = max_w + group_padding_right
        team["h"] = max_h + header_height + group_padding_bottom

        start_x = start_x + padding_left + padding_right # next team

    # second pass, rebalance teams, make sure all teams have equal height
    start_y = 0
    for l in sorted(layers.keys(), reverse = True):
        start_x = 120
        distribute_horizontal(layers[l], start_x, group_padding_right)

        max_h = 0
        for team in layers[l]:
            max_h = max(max_h, team["h"])

        for team in layers[l]:
            start_y = max(team["y"], start_y)
            team["y"] = start_y
            team["h"] = max_h
    
        start_y = start_y + max_h + group_padding_bottom * 3

    # max_h = 0
    # for team in root.values():
    #     max_h = max(max_h, team["h"])
    # for team in root.values():
    #     team["h"] = max_h

    # third pass, rebalance groups, make sure all groups have equal height
    for team in root.values():
        start_x = team["x"] + group_padding_left
        max_h = 0
        for group in team["groups"].values():
            max_h = max(max_h, group["h"])

        for group in team["groups"].values():
            h = team["h"] - header_height - group_padding_bottom
            start_y = team["y"] + header_height
            start_y = team["y"] + team["h"] - group_padding_bottom - max_h
            group["x"] = start_x
            group["y"] = start_y
            group["h"] = max_h

            relayout_items(group["items"], start_x + padding_left, start_y + max_h - group_padding_bottom)
            w = group["w"]
            start_x = start_x + w + group_padding_right

    # flat out
    all_items = []
    for team in root.values():
        all_items.append(team)
        for group in team["groups"].values():
            all_items.append(group)
            all_items = all_items + group["items"]

    # print(all_items)
    return all_items


env = Environment(
    loader=FileSystemLoader('./templates'),
    autoescape=select_autoescape(['html', 'xml']),
    trim_blocks = True,
    lstrip_blocks = True,
)

template = env.get_template('main.tmpl')


wg_style = [
    "",
    "rounded=0;whiteSpace=wrap;html=1;fillColor=#d5e8d4;fontSize=12;strokeColor=#82b366;gradientColor=#97d077;",
    "rounded=0;whiteSpace=wrap;html=1;fillColor=#f8cecc;fontSize=12;strokeColor=#b85450;gradientColor=#ea6b66;",
    "rounded=0;whiteSpace=wrap;html=1;fillColor=#fff2cc;fontSize=12;strokeColor=#d6b656;gradientColor=#ffd966;",
    "rounded=0;whiteSpace=wrap;html=1;fillColor=#dae8fc;fontSize=12;strokeColor=#6c8ebf;gradientColor=#7ea6e0;"
]

status_style = [
    "rounded=0;whiteSpace=wrap;html=1;fillColor=#6d8764;fontSize=12;strokeColor=#3A5431;fontColor=#ffffff;",
    "rounded=0;whiteSpace=wrap;html=1;fillColor=#f0a30a;fontSize=12;strokeColor=#BD7000;fontColor=#ffffff;",
    "rounded=0;whiteSpace=wrap;html=1;fillColor=#60a917;fontSize=12;strokeColor=#2D7600;fontColor=#ffffff;"
]

mdls, teams, wgs = read_data("/Users/huuhoa/Documents/CorePayment/orgchart/CorePayment.xlsx")

all = create_layout(mdls)

print(template.render(items=all, wg_style=wg_style, status_style=status_style))
