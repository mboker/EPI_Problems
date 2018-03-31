# book solution is the same up until finding the start.
# in the book, to find the start, the length of the cycle
# is calculated.  Then, one head is started at the head, and
# another is started at cycle length ahead of the head.
# each is moved by one node at a time, until they meet
# which is at the start of the cycle

from LinkedListNode import LinkedListNode as node


def test_for_cycle(head_node):
    single_hop_head, double_hop_head = head_node, head_node.next_node
    contains_cylce = False
    while double_hop_head.next_node is not None and double_hop_head.next_node.next_node is not None:
        if double_hop_head == single_hop_head or double_hop_head.next_node == single_hop_head:
            contains_cylce = True
            break
        else:
            single_hop_head, double_hop_head = single_hop_head.next_node, double_hop_head.next_node.next_node

    if not contains_cylce:
        return None
    else:
        if single_hop_head == double_hop_head:
            single_hop_head = single_hop_head.next_node
        start_of_loop = head_node
        while single_hop_head != start_of_loop:
            if single_hop_head == double_hop_head:
                start_of_loop = start_of_loop.next_node
                single_hop_head = single_hop_head.next_node
            else:
                single_hop_head = single_hop_head.next_node
        return start_of_loop


if __name__ == '__main__':

    nc_node2, nc_node3, nc_node4, nc_node5, nc_node6 = \
        node(data=2), node(data=3), node(data=4), node(data=5), node(data=6)
    c_node2, c_node3, c_node4, c_node5, c_node6 = \
        node(data=2), node(data=3), node(data=4), node(data=5), node(data=6)

    non_cylical_head, cyclical_head = node(data=1, next_node=nc_node2), node(data=1, next_node=c_node2)

    nc_node2.next_node, nc_node3.next_node, nc_node4.next_node, nc_node5.next_node = \
        nc_node3, nc_node4, nc_node5, nc_node6

    c_node2.next_node, c_node3.next_node, c_node4.next_node, c_node5.next_node, c_node6.next_node = \
        c_node3, c_node4, c_node5, c_node6, c_node2

    # print(test_for_cycle(cyclical_head).data)
    assert (test_for_cycle(non_cylical_head) is None and test_for_cycle(cyclical_head) == c_node2)
