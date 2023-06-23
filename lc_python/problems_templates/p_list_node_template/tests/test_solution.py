import pytest

from ..solution import Solution
from ..solution import ListNode


def create_list_node(values: list) -> ListNode:
    if not values:
        raise ValueError()

    head = ListNode(values[0])
    node = head
    for i in range(1, len(values)):
        node.next = ListNode(values[i])
        node = node.next

    return head

def is_nodes_equal(node: ListNode, other_node: ListNode):
    while node or other_node:
        # print(node)
        # print(other_node)
        if not node or not other_node or node.val != other_node.val:
            return False
        node, other_node = node.next, other_node.next
    return True


DATASET = [
    (None, None),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().some_method(data[0])
    assert result == data[1], result
