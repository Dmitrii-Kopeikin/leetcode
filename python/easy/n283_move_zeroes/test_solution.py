import pytest

from .solution import Solution


DATASET = [
    ([0,1,0,3,12],[1,3,12,0,0]),
    ([0], [0]),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().moveZeroes(data[0])
    assert data[0] == data[1], result
