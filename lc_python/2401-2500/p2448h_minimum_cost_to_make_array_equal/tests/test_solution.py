import pytest

from ..solution import Solution


DATASET = [
    (([1, 3, 5, 2], [2, 3, 1, 14]), 8),
    (([2, 2, 2, 2, 2], [4, 2, 8, 1, 3]), 0),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().minCost(*data[0])
    assert result == data[1], result
