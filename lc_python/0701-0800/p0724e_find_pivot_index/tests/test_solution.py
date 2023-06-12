import pytest

from ..solution import Solution


DATASET = [
    ([1, 7, 3, 6, 5, 6], 3),
    ([1, 2, 3], -1),
    ([2, 1, -1], 0),
    ([1], 0),
    ([], -1),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().pivotIndex(data[0])
    assert result == data[1], result
