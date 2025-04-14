class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n


def get_height(node):
    if node is None:
        return 0

    left_h = get_height(node.left)
    right_h = get_height(node.right)
    return max(left_h, right_h) + 1


def get_level(node, level=0, items=None):
    if node is None:
        return
    if items is None:
        items = []
    if level == 0:
        items.append(node.value)
    get_level(node.left, level - 1, items)
    get_level(node.right, level - 1, items)
    return items



def tree_by_levels(node):
    order = []
    height = get_height(node)

    for i in range(height):
        for el in get_level(node, i):
            order.append(el)

    return order


if __name__ == "__main__":
    d = Node(None, None, "D")
    b = Node(None, None, "B")
    c = Node(d, None, "C")
    a = Node(b, c, "A")

    print(get_height(a))
    print(get_level(a, 3))
    print(tree_by_levels(a))
