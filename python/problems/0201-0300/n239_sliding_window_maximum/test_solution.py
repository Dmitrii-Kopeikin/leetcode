import pytest

from .solution import Solution


DATASET = [
    (([1,3,-1,-3,5,3,6,7], 3), [3,3,5,5,6,7]),
    (([1], 1), [1]),
    (([1, -1], 1), [1, -1]),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().maxSlidingWindow(*data[0])
    assert result == data[1], result
