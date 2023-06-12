import pytest

from ..solution import Solution


DATASET = [
    ([2, 3, -1, 8, 4], 3),
    ([1, -1, 4], 2),
    ([2, 5], -1)
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().findMiddleIndex(data[0])
    assert result == data[1], result
