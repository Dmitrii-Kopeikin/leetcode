import pytest

from ..solution import Solution


DATASET = [
    (2, [0, 1, 1]),
    (5, [0, 1, 1, 2, 1, 2]),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().countBits(data[0])
    assert result == data[1], result
