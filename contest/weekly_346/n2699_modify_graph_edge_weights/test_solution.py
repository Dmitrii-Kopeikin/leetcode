import pytest

from .solution_c import Solution

DATASET = [
    ((5, [[4, 1, -1], [2, 0, -1], [0, 3, -1], [4, 3, -1]], 0, 1, 5),
     [[4, 1, 1], [2, 0, 1], [0, 3, 3], [4, 3, 1]]),
    ((3, [[0, 1, -1], [0, 2, 5]], 0, 2, 6), []),
    # ((4, [[1, 0, 4], [1, 2, 3], [2, 3, 5], [0, 3, -1]], 0, 2, 6),
    #  [[1, 0, 4], [1, 2, 3], [2, 3, 5], [0, 3, 1]]),
    # ((4, [[3, 0, -1], [1, 3, -1], [3, 2, 10], [0, 2, 2]], 0, 1, 13),
    #  [[3, 0, 12], [1, 3, 1], [3, 2, 10], [0, 2, 2]]),
    # ((4, [[0, 1, -1], [1, 2, -1], [3, 1, -1], [3, 0, 2], [0, 2, 5]], 2, 3, 8), []),
    # ((5, [[3, 0, -1], [2, 1, -1], [4, 1, 9], [3, 4, -1], [4, 0, 6],
    #  [2, 3, 5], [4, 2, 8], [3, 1, 7], [1, 0, 6], [0, 2, 9]], 4, 1, 10), []),
    # ((5, [[1, 4, 1], [2, 4, -1], [3, 0, 2], [0, 4, -1], [1, 3, 10], [1, 0, 10]], 0,
    #  2, 15), [[1, 4, 1], [2, 4, 4], [3, 0, 2], [0, 4, 14], [1, 3, 10], [1, 0, 10]]),
    # ((3, [[0, 1, -1], [1, 2, -1]], 0, 2, 11), [[0, 1, 10], [1, 2, 1]]),
    # ((4, [[0, 1, 5], [1, 2, 7], [2, 3, 7], [3, 1, 9], [3, 0, -1], [0, 2, -1]], 2, 3, 7),
    #  [[0, 1, 5], [1, 2, 7], [2, 3, 7], [3, 1, 9], [3, 0, 1000000005], [0, 2, 6]]),
]


@pytest.mark.parametrize('data', DATASET)
def test_solution(data):
    result = Solution().modifiedGraphEdges(*data[0])
    assert result == data[1], result
