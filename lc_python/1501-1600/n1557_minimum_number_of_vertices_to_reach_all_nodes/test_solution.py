import pytest

from .solution_zip import Solution as SolutionZip
from .solution import Solution 


DATASET = [
    ((6, [[0,1],[0,2],[2,5],[3,4],[4,2]]), [0, 3]),
    ((5, [[0,1],[2,1],[3,1],[1,4],[2,4]]), [0, 2, 3]),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution_zip(data):
    result = SolutionZip().findSmallestSetOfVertices(*data[0])


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().findSmallestSetOfVertices(*data[0])
    assert set(result) == set(data[1]), result
