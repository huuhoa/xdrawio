def generate_layout_spec(type, datafile_path):
    import xdrawio.arch
    if type == 'arch':
        return xdrawio.arch.generate_layout_spec(datafile_path)
