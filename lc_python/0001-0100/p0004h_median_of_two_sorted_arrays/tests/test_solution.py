import pytest

from ..solution import Solution


DATASET = [
    (([1, 2], [3, 4]), 2.5),
    (([1, 3], [2]), 2.0),
    (([1, 1], [1, 1]), 1),
    (([1, 1], [1, 1, 1]), 1),
    (([1, 1, 1, 1], [1, 1, 1]), 1),
    (([], [1, 1]), 1),
    (([1, 1], []), 1),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().findMedianSortedArrays(*data[0])
    assert result == data[1], result
