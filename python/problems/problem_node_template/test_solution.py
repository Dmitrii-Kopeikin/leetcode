import pytest

from .solution import Solution
from .solution import ListNode


def create_list_node(values: list) -> ListNode:
    if not values:
        raise ValueError()

    head = ListNode(values[0])
    node = head
    for i in range(1, len(values)):
        node.next = ListNode(values[i])
        node = node.next

    return head


DATASET = [
    (None, None),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().some_method(data[0])
    assert result == data[1], result
