import pytest

from .solution import Solution


DATASET = [
    ((1, 0, [-1], [0]), 0),
    ((6, 2, [2, 2, -1, 2, 2, 2], [0, 0, 1, 0, 0, 0]), 1),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().numOfMinutes(*data[0])
    assert result == data[1], result
