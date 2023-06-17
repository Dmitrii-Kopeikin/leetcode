import pytest

from ..solution import Solution


DATASET = [
    (([1,5,3,6,7], [1,3,2,4]), 1),
    (([1,5,3,6,7], [4,3,1]), 2),
    (([1,5,3,6,7], [1,6,3,3]), -1),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().makeArrayIncreasing(*data[0])
    assert result == data[1], result
