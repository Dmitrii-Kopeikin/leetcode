import pytest

from .solution import Solution


DATASET = [
    ([[3, 2], [4, 3], [4, 4], [2, 5]], 5),
    ([[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]], 7),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().mostPoints(data[0])
    assert result == data[1], result
