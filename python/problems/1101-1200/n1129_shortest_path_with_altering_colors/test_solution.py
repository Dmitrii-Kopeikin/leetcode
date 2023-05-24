import pytest

from .solution import Solution


DATASET = [
    ((3, [[0, 1], [1, 2]], []), [0, 1, -1]),
    ((3, [[0, 1]], [[2, 1]]), [0, 1, -1]),
    ((5, [[0, 1], [1, 2], [2, 3], [3, 4]], [
     [1, 2], [2, 3], [3, 1]]), [0, 1, 2, 3, 7]),
    ((5, [[2, 2], [0, 1], [0, 3], [0, 0], [0, 4], [2, 1], [2, 0], [1, 4],
     [3, 4]], [[1, 3], [0, 0], [0, 3], [4, 2], [1, 0]]), [0, 1, 2, 1, 1]),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().shortestAlternatingPaths(*data[0])
    assert result == data[1], result
