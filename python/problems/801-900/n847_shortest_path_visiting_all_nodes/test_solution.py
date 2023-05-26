import pytest

from .solution import Solution


DATASET = [
    ([[1,2,3],[0],[0],[0]], 5),
    ([[1], [0, 2, 4], [1, 3, 4], [2], [1, 2]], 4),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().shortestPathLength(data[0])
    assert result == data[1], result
