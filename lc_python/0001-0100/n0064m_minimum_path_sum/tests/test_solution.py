import pytest

from ..solution import Solution


DATASET = [
    ([[1,3,1],[1,5,1],[4,2,1]], 7),
    ([[1,2,3],[4,5,6]], 12),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().minPathSum(data[0])
    assert result == data[1], result
