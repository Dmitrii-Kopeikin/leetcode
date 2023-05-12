import pytest

from .solution import Solution as Solution


DATASET = [
    ([10,2,5,3], True),
    ([3,1,7,11], False),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().checkIfExist(data[0])
    assert result == data[1], result
