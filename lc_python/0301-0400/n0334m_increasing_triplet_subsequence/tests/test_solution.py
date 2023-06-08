import pytest

from ..solution import Solution


DATASET = [
    ([1, 2, 3, 4, 5], True),
    ([5, 4, 3, 2, 1], False),
    ([2, 1, 5, 0, 4, 6], True),
    ([1, 2], False),
    ([1], False),
    ([1, 2, 3], True),
    ([20, 100, 10, 12, 5, 13], True),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().increasingTriplet(data[0])
    assert result == data[1], result
