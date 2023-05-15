import pytest

from .solution import Solution

DATASET = [
    ([1,1,0], True),
    ([1,1], True),
    ([1,0], False),
]


@pytest.mark.parametrize('data', DATASET)
def test_solution(data):
    result = Solution().doesValidArrayExist(data[0])
    assert result == data[1], result
    