import pytest

from .solution import Solution, ListNode

def is_nodes_equal(node: ListNode, other_node: ListNode):
    while node or other_node:
        # print(node)
        # print(other_node)
        if not node or not other_node or node.val != other_node.val:
            return False
        node, other_node = node.next, other_node.next
    return True


DATASET = [
    (
        (ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2),
        ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5))))),
    ),
    (
        (ListNode(7, ListNode(9, ListNode(6, ListNode(6, ListNode(7, ListNode(8, ListNode(3, ListNode(0, ListNode(9, ListNode(5)))))))))), 5),
        ListNode(7, ListNode(9, ListNode(6, ListNode(6, ListNode(8, ListNode(7, ListNode(3, ListNode(0, ListNode(9, ListNode(5)))))))))),
    ),
    (
        (ListNode(1, ListNode(2)), 1),
        (ListNode(2, ListNode(1))),
    )
]




@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().swapNodes(*data[0])
    assert is_nodes_equal(result, data[1]), result
