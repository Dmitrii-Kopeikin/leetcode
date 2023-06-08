import pytest

from ..solution import Solution


DATASET = [
    (([1, 2, 3, 4], 5), 2),
    (([3, 1, 3, 4, 3], 6), 1),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().maxOperations(*data[0])
    assert result == data[1], result
