from xdrawio.datatypes import Shape
import xdrawio

class Module(Shape):
    def __init__(self, display_name, status, progress):
        super().__init__()
        self.type = "module"
        self.display_name = xdrawio.encode_name(display_name)
        self.team = ""
        self.group = ""
        self.wg_type = ""
        self.status = convert_status(status)
        self.sub_group = ""
        self.progress = convert_progress(progress)


def convert_progress(progress):
    if progress is None:
        return 0
    return progress


def convert_status(status):
    if status == "Not Started":
        return "StatusStyle0"
    if status == "In Progress":
        return "StatusStyle1"
    if status == "Completed":
        return "StatusStyle2"
    
    return "StatusStyleU"

