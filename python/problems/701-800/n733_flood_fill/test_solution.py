import pytest

from .solution import Solution


DATASET = [
    (([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2), [[2,2,2],[2,2,0],[2,0,1]]),
    (([[0,0,0],[0,0,0]], 0, 0, 0), [[0,0,0],[0,0,0]]),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().floodFill(*data[0])
    assert result == data[1], result
