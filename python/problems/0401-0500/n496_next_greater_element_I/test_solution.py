import pytest

from .solution import Solution
from .solution_other import Solution as SolutionOther


DATASET = [
    (([4, 1, 2], [1, 3, 4, 2]), [-1, 3, -1]),
    (([2, 4], [1, 2, 3, 4]), [3, -1]),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().nextGreaterElement(*data[0])
    assert result == data[1], result


@pytest.mark.parametrize("data", DATASET)
def test_solution_other(data):
    result = SolutionOther().nextGreaterElement(*data[0])
    assert result == data[1], result
