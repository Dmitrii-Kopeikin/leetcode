import pytest

from ..solution import Solution


DATASET = [
    (([2,3,5,1,3], 3), [True, True, True, False, True]),
    (([4, 2, 1, 1, 2], 1), [True, False, False, False, False]),
    (([12, 1, 12], 10), [True, False, True]),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().kidsWithCandies(*data[0])
    assert result == data[1], result
