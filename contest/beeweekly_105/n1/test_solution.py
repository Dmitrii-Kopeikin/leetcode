import pytest

from .solution import Solution

DATASET = [
    (([1,2,2], 3), 0),
    (([3,2,3], 3), 3),
]


@pytest.mark.parametrize('data', DATASET)
def test_solution(data):
    result = Solution().buyChoco(*data[0])
    assert result == data[1], result
