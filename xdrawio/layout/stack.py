
from collections import namedtuple

item_horizonal_padding = 20
item_vertical_padding = 20

Rect = namedtuple('Rect', 'x y w h')

class Layout(object):
    def __init__(self):
        super().__init__()
        self.w = 0
        self.h = 0
        self.x = 0
        self.y = 0

    def __repr__(self):
        return "{}x{}, {}x{}".format(self.x, self.y, self.w, self.h)

    def layout_children(self, data):
        raise NotImplementedError

    def to_dict(self, parent_x=0, parent_y=0):
        return {}


class FixLayout(Layout):
    def __init__(self, code):
        super().__init__()
        self.code = code

    def __repr__(self):
        return "<F: {}, {}>".format(self.code, super().__repr__())

    def layout_children(self, data):
        g = data.get(self.code, None)
        if g is None:
            return
        self.w = g.w
        self.h = g.h

    def to_dict(self, parent_x=0, parent_y=0):
        return {self.code: Rect(self.x + parent_x, self.y + parent_y, self.w, self.h)}


class XStack(Layout):
    def __init__(self):
        super().__init__()
        self.items = []
        self._type = "X"

    def __repr__(self):
        return "<{}: {}, {}>".format(self._type, self.items, super().__repr__())

    def to_dict(self, parent_x=0, parent_y=0):
        result = {}
        for i in self.items:
            result.update(i.to_dict(self.x + parent_x, self.y + parent_y))
        return result


class HStack(XStack):
    def __init__(self):
        super().__init__()
        self._type = "H"

    def layout_children(self, data):
        for i in self.items:
            i.layout_children(data)

        w = 0
        h = 0
        x = 0
        for i in self.items:
            w = w + i.w
            h = max(h, i.h)
            i.x = x
            x = x + i.w + item_horizonal_padding

        w = w + (len(self.items) - 1) * item_horizonal_padding
        self.w = w
        self.h = h

        # make sure all items have same height -> strech mode
        for i in self.items:
            i.h = h


class VStack(XStack):
    def __init__(self):
        super().__init__()
        self._type = "V"

    def layout_children(self, data):
        for i in self.items:
            i.layout_children(data)

        w = 0
        h = 0
        y = 0
        for i in self.items:
            w = max(w, i.w)
            h = h + i.h
            i.y = y
            y = y + i.h + item_vertical_padding
     
        h = h + (len(self.items) - 1) * item_vertical_padding
        self.w = w
        self.h = h

        # make sure all items have same width -> strech mode
        for i in self.items:
            i.w = w

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
