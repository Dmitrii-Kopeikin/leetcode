import pytest

from ..solution import Solution


DATASET = [
    ([2, 1, 3], 1),
    ([3, 4, 5, 1, 2], 5),
    ([1, 2, 3], 0),
    ([9, 4, 2, 1, 3, 6, 5, 7, 8, 14, 11, 10, 12, 13, 16, 15, 17, 18], 216212978),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().numOfWays(data[0])
    assert result == data[1], result
