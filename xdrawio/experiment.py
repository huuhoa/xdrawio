from .generate_layout import generate_layout_spec
from .generate_drawio import generate_drawio, render_drawio
import json


def experiment(args, page_configs):
    configs = {'template': 'generic.tmpl'}
    configs.update(page_configs)

    ls_tree = generate_layout_spec(args.type, args.path, args)
    if args.write_layout_tree:
        args.layout_tree.write(json.dumps(ls_tree, sort_keys=True, indent=2))

    all_items = generate_drawio(ls_tree)
    render_drawio(all_items, args, configs)
