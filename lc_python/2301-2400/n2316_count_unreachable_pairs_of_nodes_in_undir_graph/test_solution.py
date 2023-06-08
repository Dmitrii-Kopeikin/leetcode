import pytest

from .solution import Solution
from .solution_by_class_uf import Solution as SolutionClass


DATASET = [
    ((7, [[0,2],[0,5],[2,4],[1,6],[5,4]]), 14),
    ((3, [[0,1],[0,2],[1,2]]), 0),
    ((3, [[0, 1], [0, 2], [1, 2]]), 0),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().count_pairs(*data[0])


@pytest.mark.parametrize("data", DATASET)
def test_solution_by_class(data):
    result = SolutionClass().count_pairs(*data[0])
    assert result == data[1], result
