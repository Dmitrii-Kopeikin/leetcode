import pytest

from .solution import Solution, ListNode


DATASET = [
    (ListNode(1, ListNode(2, ListNode(3, ListNode(4)))), ListNode(2, ListNode(1, ListNode(4, ListNode(3))))),
    (None, None),
    (ListNode(1), ListNode(1)),
]


def is_nodes_equal(node: ListNode, other_node: ListNode):
    while node or other_node:
        # print(node)
        # print(other_node)
        if not node or not other_node or node.val != other_node.val:
            return False
        node, other_node = node.next, other_node.next
    return True


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().swapPairs(data[0])
    assert is_nodes_equal(result, data[1]), result
