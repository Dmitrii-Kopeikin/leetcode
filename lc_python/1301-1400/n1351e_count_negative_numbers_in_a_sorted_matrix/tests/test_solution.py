import pytest

from ..solution import Solution


DATASET = [
    ([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]], 8),
    ([[3,2],[1,0]], 0),
    ([[1]], 0),
    ([[-1]], 1),
    ([[-1, -1, -1], [-2, -2, -2], [-3, -3, -3]], 9),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().countNegatives(data[0])
    assert result == data[1], result
