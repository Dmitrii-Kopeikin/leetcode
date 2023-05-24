import pytest

from .solution import Solution


DATASET = [
    (([4,2,3,0,3,1,2], 5), True),
    (([4,2,3,0,3,1,2], 0), True),
    (([3,0,2,1,2], 2), False),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().canReach(*data[0])
    assert result == data[1], result
