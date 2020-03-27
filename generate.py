#!/usr/bin/env python3

from jinja2 import Environment, FileSystemLoader, select_autoescape

import xdrawio

def main():
    import argparse
    from xdrawio.layout import create_layout, layout_workgroup


    parser = argparse.ArgumentParser(description='Render team structure to drawio file format.')
    parser.add_argument('team_path', metavar='path', type=str,
                        help='path to xlsx file that contains team structure')

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
    all = create_layout(mdls, wgs_byteam, d)

    print(template.render(items=all, configs=d.configurations))


if __name__ == "__main__":
    main()
