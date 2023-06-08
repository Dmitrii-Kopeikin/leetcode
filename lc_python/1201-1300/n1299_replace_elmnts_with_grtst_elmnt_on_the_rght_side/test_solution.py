import pytest

from .solution import Solution as Solution


DATASET = [
    ([17,18,5,4,6,1], [18,6,6,6,1,-1]),
    ([400], [-1]),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().replaceElements(data[0])
    assert result == data[1], result
