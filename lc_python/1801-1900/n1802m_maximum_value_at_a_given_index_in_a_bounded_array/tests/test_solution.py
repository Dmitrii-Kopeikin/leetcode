import pytest

from ..solution import Solution


DATASET = [
    ((4, 2, 6), 2),
    ((6, 1, 10), 3),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().maxValue(*data[0])
    assert result == data[1], result
