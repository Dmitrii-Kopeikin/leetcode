import pytest

from ..solution import Solution


DATASET = [
    ([2, 2, 1], 1),
    ([4, 1, 2, 1, 2], 4),
    ([1], 1),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().singleNumber(data[0])
    assert result == data[1], result
