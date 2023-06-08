import pytest

from ..solution import Solution


DATASET = [
    ([10, 15, 20], 15),
    ([1, 100, 1, 1, 1, 100, 1, 1, 100, 1], 6),
    ([1, 2], 1),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().minCostClimbingStairs(data[0])
    assert result == data[1], result
