#!/usr/bin/env python3

from jinja2 import Environment, FileSystemLoader, select_autoescape

import xdrawio

def main():
    import argparse
    from xdrawio.layout import create_layout, layout_workgroup
    from xdrawio.datatypes import Page


    parser = argparse.ArgumentParser(description='Render team structure to drawio file format.')
    parser.add_argument('team_path', metavar='path', type=str,
                        help='path to xlsx file that contains team structure')
    parser.add_argument('--debug', type=bool,
                        help='debug flag, when enable only print debug data, not print drawio data')

    args = parser.parse_args()

    env = Environment(
        loader=FileSystemLoader('./templates'),
        autoescape=select_autoescape(['html', 'xml']),
        trim_blocks = True,
        lstrip_blocks = True,
        line_statement_prefix='#',
    )

    template = env.get_template('corepayment.tmpl')

    mdls, d = xdrawio.read_data(args.team_path)

    wgs_byteam = layout_workgroup(d.workgroups)

    page = Page()
    page.initialize(mdls, d)

    create_layout(page, wgs_byteam, d)
    # flat out
    all_items = page.flatten_tree()
    for wg in wgs_byteam.values():
        for i in range(5):
            all_items.append(wg[i])

    if not args.debug:
        print(template.render(items=all_items, configs=d.configurations))


if __name__ == "__main__":
    main()
