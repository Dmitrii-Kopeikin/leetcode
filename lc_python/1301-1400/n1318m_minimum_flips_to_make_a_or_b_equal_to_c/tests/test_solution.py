import pytest

from ..solution import Solution


DATASET = [
    ((2, 6, 5), 3),
    ((4, 2, 7), 1),
    ((1, 2, 3), 0),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().minFlips(*data[0])
    assert result == data[1], result
