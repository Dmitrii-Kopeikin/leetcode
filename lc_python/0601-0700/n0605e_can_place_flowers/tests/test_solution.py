import pytest

from ..solution import Solution


DATASET = [
    (([1, 0, 0, 0, 1], 1), True),
    (([1, 0, 0, 0, 1], 2), False),
    (([0, 0, 0], 2), True),
    (([1, 0, 0, 0, 0, 1], 2), False),
    (([0, 1, 0], 1), False),
    (([0], 1), True),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().canPlaceFlowers(*data[0])
    assert result == data[1], result
