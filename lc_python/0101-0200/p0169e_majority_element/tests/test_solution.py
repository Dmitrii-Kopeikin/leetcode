import pytest

from ..solution import Solution


DATASET = [
    ([3, 2, 3], 3),
    ([2, 2, 1, 1, 1, 2, 2], 2)
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().majorityElement(data[0])
    assert result == data[1], result
