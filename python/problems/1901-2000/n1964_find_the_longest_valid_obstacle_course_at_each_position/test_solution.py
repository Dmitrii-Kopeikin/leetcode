import pytest

from .solution import Solution


DATASET = [
    ([1, 2, 3, 2], [1, 2, 3, 3]),
    ([2, 2, 1], [1, 2, 1]),
    ([3, 1, 5, 6, 4, 2], [1, 1, 2, 3, 2, 2]),
    ([1, 5, 6, 2, 3, 4, 8], [1, 2, 3, 2, 3, 4, 5]),
    ([1], [1]),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().longestObstacleCourseAtEachPosition(data[0])
    assert result == data[1], result
