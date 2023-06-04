import pytest

from ..solution import Solution

DATASET = [
    ((3, [[0,0,1],[1,2,2],[0,2,3],[1,0,4]]), 23),
    ((3, [[0,0,4],[0,1,2],[1,0,1],[0,2,3],[1,2,1]]), 17),
]


@pytest.mark.parametrize('data', DATASET)
def test_solution(data):
    result = Solution().matrixSumQueries(*data[0])
    assert result == data[1], result
    