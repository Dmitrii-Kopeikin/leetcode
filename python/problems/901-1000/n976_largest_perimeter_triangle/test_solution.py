import pytest

from .solution import Solution


DATASET = [
    ([2, 1, 2], 5),
    ([1, 2, 1, 10], 0),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().largestPerimeter(data[0])
    assert result == data[1], result
