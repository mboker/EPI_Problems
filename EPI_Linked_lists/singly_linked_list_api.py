from LinkedListNode import LinkedListNode as node


def search_for_key(head_node, key):
    current_node = head_node
    while current_node is not None and current_node.data != key:
        current_node = current_node.next_node
    return current_node


def insert_node(leading_node, new_node):
    leading_node.next_node, new_node.next_node = new_node, leading_node.next_node


def delete_node_by_key(head_node, key):
    current_node = head_node
    while current_node.next_node is not None and current_node.next_node.data != key:
        current_node = current_node.next_node
    if current_node.next_node is not None:
        current_node.next_node = current_node.next_node.next_node


def delete_node_after(lead_node):
    if lead_node.next_node is not None:
        lead_node.next_node = lead_node.next_node.next_node

if __name__ == '__main__':
    # test insert
    first_node, second_node, third_node, fourth_node = \
        node(data=20), node(data=25), node(data=30), node(data=40)

    insert_node(first_node, second_node)
    insert_node(second_node, third_node)

    assert(first_node.next_node.data == 25)
    assert(second_node.next_node.data == 30)

    insert_node(second_node, fourth_node)
    assert(first_node.next_node.data == 25)
    assert(second_node.next_node.data == 40)
    assert(fourth_node.next_node.data == 30)

    # test search
    assert(search_for_key(first_node, 40) == fourth_node)
    assert(search_for_key(first_node, 50) is None)

    # test delete by key
    delete_node_by_key(first_node, 25)
    assert(first_node.next_node.data == 40)
    delete_node_by_key(first_node, 60)
    assert(first_node.next_node.data == 40 and fourth_node.next_node.data == 30)

    # test delete node after
    delete_node_after(first_node)
    assert(first_node.next_node.data == 30)
    delete_node_after(third_node)
    assert(first_node.next_node.data == 30 and third_node.next_node is None)
