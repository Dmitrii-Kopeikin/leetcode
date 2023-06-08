import pytest

from .solution import Solution

DATASET = [
    ((5, 2), [4,5]),
    ((4, 4), [2, 3, 4]),
    ((1, 1), []),
    ((2, 1), []),
    ((3, 1), [3]),
    ((3, 4), [3]),
    ((4, 1), []),
    ((5, 3), [2, 3]),
    ((5, 2), [4, 5]),
]


@pytest.mark.parametrize('data', DATASET)
def test_solution(data):
    result = Solution().circularGameLosers(*data[0])
    assert result == data[1], result
    