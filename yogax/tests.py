import yoga

#   YGBENCHMARK("Stack with flex", {
#     const YGNodeRef root = YGNodeNew();
#     YGNodeStyleSetWidth(root, 100);
#     YGNodeStyleSetHeight(root, 100);

#     for (uint32_t i = 0; i < 10; i++) {
#       const YGNodeRef child = YGNodeNew();
#       YGNodeSetMeasureFunc(child, _measure);
#       YGNodeStyleSetFlex(child, 1);
#       YGNodeInsertChild(root, child, 0);
#     }

#     YGNodeCalculateLayout(root, YGUndefined, YGUndefined, YGDirectionLTR);
#     YGNodeFreeRecursive(root);
#   });


def test1():
    root = yoga.Node.create()
    print(dir(root))
    root.width = 100
    root.height = 100

    for i in range(10):
        child = yoga.Node.create()
        child.set_flex(1)
        root.insert_child(child, 0)

    root.calculate_layout()

    print(root)

def dump_node(root):
    print("Rect [%dx%d %dx%d], WxH: [%dx%d]" % (root.calculated_left, root.calculated_top,
        root.calculated_right, root.calculated_bottom,
        root.calculated_width, root.calculated_height))

    for child in root.children:
        dump_node(child)


def test2():
#       <View style={{
#         flex: 1,
#         width: 500,
#         height: 500,
#         alignItems: 'flex-start',
#         padding: 20,
#       }}>
    root = yoga.Node.create()
    root.width = 500
    root.height = 500
    root.align_items = yoga.Align.FlexStart
    root.set_padding(yoga.Edge.All, 20)
    root.set_flex(1)
    root.flex_wrap = yoga.Wrap.Wrap
    root.flex_direction = yoga.FlexDirection.Row
    root.align_content = yoga.Align.Stretch

#         <View style={{
#           flex: 1,
#           width: 100,
#           height: 100,
#         }} />
    child1 = yoga.Node.create()
    child1.width = 100
    child1.height = 100
    # child1.set_flex(1)
    root.insert_child(child1, 0)

#         <View style={{
#           flex: 1,
#           width: 100,
#           height: 100,
#           marginHorizontal: 20,
#           flexGrow: 1,
#         }} />
    child2 = yoga.Node.create()
    child2.width = 100
    child2.height = 100
    # child2.set_flex(1)
    child2.flex_grow = 1
    child2.set_margin(yoga.Edge.Horizontal, 20)
    root.insert_child(child2, 1)

#         <View style={{
#           flex: 1,
#           width: 100,
#           height: 100,
#         }} />
    for i in range(15):
        child3 = yoga.Node.create()
        child3.width = 100
        child3.height = 100
        # child3.set_flex(1)
        root.insert_child(child3, 2+i)

    root.calculate_layout()

    return root


def test5():
    root = yoga.Node.create()
    root.width = 320
    root.height = 80
    root.set_margin(yoga.Edge.Top, 40)
    root.set_margin(yoga.Edge.Left, 10)
    root.set_padding(yoga.Edge.All, 10)
    root.set_flex_direction(yoga.FlexDirection.Row)

    child1 = yoga.Node.create()
    child1.width = 80
    child1.set_margin(yoga.Edge.Right, 10)
    root.insert_child(child1, 0)

    child2 = yoga.Node.create()
    child2.width = 80
    child2.height = 20
    child2.flex_grow = 1
    child2.align_self = yoga.Align.Center
    root.insert_child(child2, 1)

    root.calculate_layout()

    return root

def test4():
    root = yoga.Node.create()
    root.width = 320
    root.height = 80
    root.set_margin(yoga.Edge.Top, 40)
    root.set_margin(yoga.Edge.Left, 10)
    root.set_flex_direction(yoga.FlexDirection.Row)

    child1 = yoga.Node.create()
    child1.width = 80
    root.insert_child(child1, 0)

    child2 = yoga.Node.create()
    child2.width = 80
    child2.flex_grow = 1
    root.insert_child(child2, 1)

    root.calculate_layout()

    return root


def test3():
    root = yoga.Node.create()
    root.width = 320
    root.height = 80
    root.set_margin(yoga.Edge.Top, 40)
    root.set_margin(yoga.Edge.Left, 10)
    root.set_flex_direction(yoga.FlexDirection.Row)

    root.calculate_layout()

    return root

def test6():
    root = yoga.Node.create()
    root.width = 320
    root.height = 575
    root.align_items = yoga.Align.Center
    root.justify_content = yoga.Justify.FlexEnd
    root.set_margin(yoga.Edge.Top, 40)
    root.set_margin(yoga.Edge.Left, 10)
    root.set_padding(yoga.Edge.All, 10)
    root.flex_direction = yoga.FlexDirection.Row

    child1 = yoga.Node.create()
    child1.width = 80
    child1.set_margin(yoga.Edge.Right, 10)
    root.insert_child(child1, 0)

    child2 = yoga.Node.create()
    child2.width = 80
    child2.height = 20
    child2.flex_grow = 1
    child2.align_self = yoga.Align.Center
    root.insert_child(child2, 1)

    root.calculate_layout()

    return root


n = test2()
dump_node(n)
