from __future__ import annotations
from collections import namedtuple

item_horizontal_padding = 20
item_vertical_padding = 20

Rect = namedtuple('Rect', 'x y w h')


class Layout(object):
    def __init__(self):
        super().__init__()
        self.w = 0
        self.h = 0
        self.x = 0
        self.y = 0
        self.code = ''
        self.attr = {}

    def __repr__(self):
        return "{}x{}, {}x{}".format(self.x, self.y, self.w, self.h)

    def dumps(self):
        raise NotImplementedError

    def replace(self, code: str, new_node: Layout):
        raise NotImplementedError

    def add_attribute(self, attr):
        self.attr = attr

    def to_dict(self, parent_x=0, parent_y=0):
        return {}


class FixLayout(Layout):
    def __init__(self, code, w, h):
        super().__init__()
        self.code = code
        self.w = w
        self.h = h

    def __repr__(self):
        return "<F: {}, {}>".format(self.code, super().__repr__())

    def dumps(self):
        """ dump current stack to array """
        import xdrawio.xutils

        result = {
            'id': xdrawio.xutils.random_string(),
            'type': 'fix',
        }
        if self.w > 0:
            result['width'] = self.w
        if self.h > 0:
            result['height'] = self.h
        result.update(self.attr)

        return result

    def replace(self, code, new_node):
        return False

    def to_dict(self, parent_x=0, parent_y=0):
        return {self.code: Rect(self.x + parent_x, self.y + parent_y, self.w, self.h)}


class GridLayout(Layout):
    def __init__(self, code):
        super().__init__()
        self.items = []
        self.code = code
        self._type = "G"

    def __repr__(self):
        return "<{}: {}, {}>".format(self._type, self.items, super().__repr__())

    def replace(self, code, new_node):
        for index, child in enumerate(self.items):
            if child.code == code:
                self.items[index] = new_node
                return True
            if child.replace(code, new_node):
                return True

        return False

    def dumps(self):
        """ dump current stack to array """
        import xdrawio.xutils

        children = [item.dumps() for item in self.items]
        result = {
            'id': xdrawio.xutils.random_string(),
            'type': 'grid',
            'flex-direction': 'column',
            # 'flex-wrap': 'wrap',
            'children': children
        }
        result.update(self.attr)

        return result

    def to_dict(self, parent_x=0, parent_y=0):
        result = {}
        for i in self.items:
            result.update(i.to_dict(self.x + parent_x, self.y + parent_y))
        return result


class XStack(Layout):
    def __init__(self):
        super().__init__()
        self.items = []
        self._type = "X"

    def __repr__(self):
        return "<{}: {}, {}>".format(self._type, self.items, super().__repr__())

    def replace(self, code, new_node):
        for index, child in enumerate(self.items):
            if child.code == code:
                self.items[index] = new_node
                return True
            if child.replace(code, new_node):
                return True

        return False

    def to_dict(self, parent_x=0, parent_y=0):
        result = {}
        for i in self.items:
            result.update(i.to_dict(self.x + parent_x, self.y + parent_y))
        return result


class HStack(XStack):
    def __init__(self):
        super().__init__()
        self._type = "H"

    def dumps(self):
        """ dump current stack to array """
        import xdrawio.xutils
        children = [item.dumps() for item in self.items]
        if len(children) >= 2:
            # try make last item fill remaining space
            last_child = children[len(children)-1]
            if last_child.get('class') == 'domain':
                last_child.update({'flex': 1})

        result = {
            'id': xdrawio.xutils.random_string(),
            'type': 'container',
            'flex-direction': 'row',
            'children': children,
        }
        result.update(self.attr)

        return result


class VStack(XStack):
    def __init__(self):
        super().__init__()
        self._type = "V"

    def dumps(self):
        """ dump current stack to array """
        import xdrawio.xutils
        children = [item.dumps() for item in self.items]

        result = {
            'id': xdrawio.xutils.random_string(),
            'type': 'container',
            'flex-direction': 'column',
            'children': children,
        }
        result.update(self.attr)

        return result


def H(*inputs):
    h = HStack()
    for i in inputs:
        if type(i) is str:
            h.items.append(FixLayout(i))
        else:
            h.items.append(i)

    return h


def V(*inputs):
    v = VStack()
    for i in inputs:
        if type(i) is str:
            v.items.append(FixLayout(i))
        else:
            v.items.append(i)

    return v
