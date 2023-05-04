import pytest

from .solution import Solution


DATASET = [
    (234, 15),
    (4421, 21),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().subtractProductAndSum(data[0])
    assert result == data[1], result
