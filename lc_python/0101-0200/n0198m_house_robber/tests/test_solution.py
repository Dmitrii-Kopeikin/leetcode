import pytest

from ..solution import Solution


DATASET = [
    ([1, 2, 3, 1], 4),
    ([2, 7, 9, 3, 1], 12),
    ([1, 2], 2),
    ([2], 2),
    ([], 0),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().rob(data[0])
    assert result == data[1], result
