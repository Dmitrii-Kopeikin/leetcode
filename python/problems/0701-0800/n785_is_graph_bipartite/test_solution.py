import pytest

from .solution import Solution


DATASET = [
    ([[1],[0]], True),
    ([[1,2,3],[0,2],[0,1,3],[0,2]], False),
    ([[1,3],[0,2],[1,3],[0,2]], True),
    ([[4,1],[0,2],[1,3],[2,4],[3,0]], False),
    ([[1],[0,3],[3],[1,2]], True),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().isBipartite(data[0])
    assert result == data[1], result
