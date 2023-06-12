import pytest

from ..solution import Solution


DATASET = [
    ([1, 1, 0, 1], 3),
    ([0, 1, 1, 1, 0, 1, 1, 0, 1], 5),
    ([1, 1, 1], 2),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().longestSubarray(data[0])
    assert result == data[1], result
