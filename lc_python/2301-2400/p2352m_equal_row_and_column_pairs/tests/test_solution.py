import pytest

from ..solution import Solution


DATASET = [
    ([[3, 2, 1], [1, 7, 6], [2, 7, 7]], 1),
    ([[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]], 3),
    ([[1]], 1),
    ([[13,13],[13,13]], 4),
    ([[13,13],[13,1]], 2),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().equalPairs(data[0])
    assert result == data[1], result
