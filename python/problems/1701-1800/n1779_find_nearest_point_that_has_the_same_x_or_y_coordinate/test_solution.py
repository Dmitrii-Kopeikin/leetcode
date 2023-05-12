import pytest

from .solution import Solution


DATASET = [
    ((3, 4, [[1,2],[3,1],[2,4],[2,3],[4,4]]), 2),
    ((3, 4, [[3,4]]), 0),
    ((3, 4, [[2,3]]), -1),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().nearestValidPoint(*data[0])
    assert result == data[1], result
