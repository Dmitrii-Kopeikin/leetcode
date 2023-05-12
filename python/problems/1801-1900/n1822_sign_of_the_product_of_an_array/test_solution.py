import pytest

from .solution import Solution as Solution


DATASET = [
    ([-1, -2, -3, -4, 3, 2, 1], 1),
    ([1, 5, 0, 2, -3], 0),
    ([-1, 1, -1, 1, -1], -1),
    ([0], 0),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().arraySign(data[0])
    assert result == data[1], result
