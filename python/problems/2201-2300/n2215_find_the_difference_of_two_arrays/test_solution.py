import pytest

from .solution import Solution


DATASET = [
    (([1, 2, 3], [2, 4, 6]), [[1, 3], [4, 6]]),
    (([1, 2, 3, 3], [1, 1, 2, 2]), [[3], []]),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().findDifference(*data[0])
    assert sorted(result) == sorted(data[1]), result
