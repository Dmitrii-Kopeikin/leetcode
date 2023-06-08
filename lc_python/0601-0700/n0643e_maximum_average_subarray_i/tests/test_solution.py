import pytest

from ..solution import Solution


DATASET = [
    (([1, 12, -5, -6, 50, 3], 4), 12.75),
    (([5], 1), 5.0),
    (([0, 1, 1, 3, 3], 4), 2.0),
    (([-5, -4, -3, -2, -1], 2), -1.5),
    (([0, 4, 0, 3, 2], 1), 4.0),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().findMaxAverage(*data[0])
    assert result == data[1], result
