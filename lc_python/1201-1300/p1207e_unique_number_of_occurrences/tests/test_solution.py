import pytest

from ..solution import Solution


DATASET = [
    ([1, 2, 2, 1, 1, 3], True),
    ([1, 2], False),
    ([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0], True),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().uniqueOccurrences(data[0])
    assert result == data[1], result
