import pytest

from ..solution import Solution

DATASET = [
    ([2,1,4,3], 2),
    ([2,4,1,3], 3),
    ([1,3,4,2,5], 0),
    ([1], 0),
    ([2, 3, 5, 1, 4], 4),
]


@pytest.mark.parametrize('data', DATASET)
def test_solution(data):
    result = Solution().semiOrderedPermutation(data[0])
    assert result == data[1], result
    