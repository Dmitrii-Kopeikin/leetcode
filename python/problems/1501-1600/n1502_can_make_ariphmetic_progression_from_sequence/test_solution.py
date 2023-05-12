import pytest

from .solution import Solution


DATASET = [
    ([], False),
    ([2, 4], True),
    ([1], False),
    ([3,5,1], True),
    ([1,2,4], False),
    ([-2, 0, 4, 8, -6, 2, 6, -4], True),
    ([-2, 0, 1, 4, 8, - 6], False),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().canMakeArithmeticProgression(data[0])
    assert result == data[1], result
