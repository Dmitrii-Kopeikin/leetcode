import pytest

from .solution import Solution


DATASET = [
    (([1, 3, 3, 2], [2, 1, 3, 4], 3), 12),
    (([4, 2, 3, 1, 1], [7, 5, 10, 9, 6], 1), 30),
    (([1, 2, 3, 4, 100], [100, 4, 5, 6, 2], 2), 208),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().maxScore(*data[0])
    assert result == data[1], result
