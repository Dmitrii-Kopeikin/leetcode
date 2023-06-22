import pytest

from ..solution import Solution
from ..solution import ListNode


def create_list_node(values: list) -> ListNode:
    if not values:
        return None

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
    (create_list_node([1,2,3,4,5]), create_list_node([5,4,3,2,1])),
    (create_list_node([1,2]), create_list_node([2,1])),
    (create_list_node([]), create_list_node([])),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().reverseList(data[0])
    assert is_nodes_equal(result, data[1]), f'{str(result)} - {str(data[1])}'
