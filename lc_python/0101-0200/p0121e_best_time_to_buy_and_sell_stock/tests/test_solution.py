import pytest

from ..solution import Solution


DATASET = [
    ([7,1,5,3,6,4], 5),
    ([7,6,4,3,1], 0)
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().maxProfit(data[0])
    assert result == data[1], result
