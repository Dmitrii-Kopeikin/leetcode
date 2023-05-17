import pytest

from .solution import Solution
# from utils.list_node import ListNode, is_nodes_equal


DATASET = [
    (None, None),
]

# def is_nodes_equal(node: ListNode, other_node: ListNode):
#     while node or other_node:
#         # print(node)
#         # print(other_node)
#         if not node or not other_node or node.val != other_node.val:
#             return False
#         node, other_node = node.next, other_node.next
#     return True


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().some_method(data[0])
    assert result == data[1], result
