import pytest

from .solution import Solution

DATASET = [
    ([3,-1,-5,2,5,-9], 1350),
    ([-4,-5,-4], 20),
    ([-1, -2, -3, -4], 24),
    ([-1], -1),
    ([-9, -5], 45),
    ([-9, 9], 9),
    ([9], 9),
    ([0, 0], 0),
    ([0, -1], 0),
    ([0, 9], 9),
    ([0, -4, -7], 28),
]


@pytest.mark.parametrize('data', DATASET)
def test_solution(data):
    result = Solution().maxStrength(data[0])
    assert result == data[1], result
