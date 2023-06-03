import pytest

from ..solution import Solution


DATASET = [
    ([[1, 2, 3], [2, 3, 1], [3, 4, 2], [4, 5, 3], [5, 6, 4]], 5),
    ([[1, 1, 5], [10, 10, 5]], 1),
    ([[2, 1, 3], [6, 1, 4]], 2),
    ([], 0),
    ([[1, 1, 10]], 1),
    ([[4,4,3],[4,4,3]], 2),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().maximumDetonation(data[0])
    assert result == data[1], result
