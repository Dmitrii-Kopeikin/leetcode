import pytest

from .solution import Solution


DATASET = [
    ([[1,2],[2,3],[5],[0],[5],[],[]], [2,4,5,6]),
    ([[1,2,3,4],[1,2],[3,4],[0,4],[]], [4]),
    ([[],[0,2,3,4],[3],[4],[]], [0,1,2,3,4]),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().eventualSafeNodes(data[0])
    assert result == data[1], result
