import pytest

from .solution import Solution
from .solution_other import Solution as SolutionOther


DATASET = [
    ([[1,2],[2,3],[3,4],[4,5],[5,6]], True),
    ([[1,1],[2,2],[3,4],[4,5],[5,6]], False),
    ([[0,0],[0,1],[0,-1]], True),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().checkStraightLine(data[0])
    assert result == data[1], result


@pytest.mark.parametrize("data", DATASET)
def test_solution_other(data):
    result = SolutionOther().checkStraightLine(data[0])
    assert result == data[1], result
