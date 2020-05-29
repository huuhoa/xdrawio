import xdrawio.xutils


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
            ti["id"] = xdrawio.xutils.randomString()
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

