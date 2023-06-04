import pytest

from ..solution import Solution

DATASET = [
    ((6, [[0,1],[0,2],[1,2],[3,4]]), 3),
    ((6, [[0,1],[0,2],[1,2],[3,4],[3,5]]), 1),
    ((6, [[1,0],[0,2],[1,2],[3,4],[3,5]]), 1),
]


@pytest.mark.parametrize('data', DATASET)
def test_solution(data):
    result = Solution().countCompleteComponents(*data[0])
    assert result == data[1], result
    