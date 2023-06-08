import pytest

from .solution import Solution


DATASET = [
    ([10,9,2,5,3,7,101,18], 4),
    ([0,1,0,3,2,3], 4),
    ([7,7,7,7,7,7,7], 1),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().lengthOfLIS(data[0])
    assert result == data[1], result
