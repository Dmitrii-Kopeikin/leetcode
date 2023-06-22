import pytest

from ..solution import Solution


DATASET = [
    (([1, 3, 2, 8, 4, 9], 2), 8),
    (([1, 3, 7, 5, 10, 3], 3), 6),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().maxProfit(*data[0])
    assert result == data[1], result
