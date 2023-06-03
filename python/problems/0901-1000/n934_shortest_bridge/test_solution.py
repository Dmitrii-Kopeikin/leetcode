import pytest

from .solution import Solution


DATASET = [
    ([[0,1],[1,0]], 1),
    ([[0,1,0],[0,0,0],[0,0,1]], 2),
    ([[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]], 1),
    ([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1]], 5),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().shortestBridge(data[0])
    assert result == data[1], result
