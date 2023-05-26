import pytest

from .solution import Solution


DATASET = [
    ([2,7,9,4,4], 10),
    ([1,2,3,4,5,100], 104),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().stoneGameII(data[0])
    assert result == data[1], result
