import pytest

from ..solution import Solution


DATASET = [
    (2, 2),
    (3, 3),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().climbStairs(data[0])
    assert result == data[1], result
