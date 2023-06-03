import pytest

from .solution import Solution


DATASET = [
    ((7, [1, 3, 4, 5]), 16),
    ((9, [5, 6, 1, 4, 2]), 22),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().minCost(*data[0])
    assert result == data[1], result
