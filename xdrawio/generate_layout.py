def generate_layout_spec(type: str, datafile_path: str, args):
    import xdrawio.arch
    if type == 'arch':
        return xdrawio.arch.generate_layout_spec(datafile_path, args.level)
