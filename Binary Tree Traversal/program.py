class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def pre_order(node, order=None):
    """Pre-order traversal"""
    if order is None:
        order = []
    if node is None:
        return order
    order.append(node.data)
    pre_order(node.left, order)
    pre_order(node.right, order)
    return order


def in_order(node, order=None):
    """In-order traversal"""
    if order is None:
        order = []
    if node is None:
        return order
    in_order(node.left, order)
    order.append(node.data)
    in_order(node.right, order)
    return order

def post_order(node, order=None):
    """Post-order traversal"""
    if order is None:
        order = []
    if node is None:
        return order
    post_order(node.left, order)
    post_order(node.right, order)
    order.append(node.data)
    return order


if __name__ == "__main__":
    a = Node("A")
    b = Node("B")
    c = Node("C")

    a.left = b
    a.right = c
    d = Node("D")
    c.left = d

    print(pre_order(a))
    print(in_order(a))
    print(post_order(a))
