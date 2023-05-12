import pytest

from .solution import Solution, ListNode


DATASET = [
    (ListNode(1, ListNode(0, ListNode(1))), 5),
    (ListNode(0), 0)
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().getDecimalValue(data[0])
    assert result == data[1], result
