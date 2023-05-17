import pytest

from .solution import Solution
from leetcode_test_utils.list_node import ListNode, create_list_node

DATASET = [
    (create_list_node([5,4,2,1]), 6),
    (create_list_node([4,2,2,3]), 7),
    (create_list_node([1, 100000]), 100001),
    (create_list_node([1, 2, 3]), 4),
    (create_list_node([1]), 0),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().pairSum(data[0])
    assert result == data[1], result


def test_solution_exception():
    with pytest.raises(ValueError):
        test_solution((None, None))