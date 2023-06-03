import pytest

from .solution import Solution

DATASET = [
    ([2,3,6], True),
    ([3,9,5], False),
    ([4,3,12,8], True),
]


@pytest.mark.parametrize('data', DATASET)
def test_solution(data):
    result = Solution().canTraverseAllPairs(data[0])
    assert result == data[1], result
