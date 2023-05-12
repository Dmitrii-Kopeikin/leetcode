import pytest

from .solution import Solution


DATASET = [
    ([[1,2,3],[3,2,1]], 6),
    ([[1,5],[7,3],[3,5]], 10),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().maximumWealth(data[0])
    assert result == data[1], result
