import pytest

from ..solution import Solution


DATASET = [
    ([-5, 1, 5, 0, -7], 1),
    ([-4, -3, -2, -1, 4, 3, 2], 0),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().largestAltitude(data[0])
    assert result == data[1], result
