import pytest

from .solution import Solution, SolutionRecursion


DATASET = [
    ((3, 3, 1, 1), 8),
    ((2, 3, 1, 2), 5),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().countGoodStrings(*data[0])
    assert result == data[1], result


@pytest.mark.parametrize("data", DATASET)
def test_solution_recursion(data):
    result = SolutionRecursion().countGoodStrings(*data[0])
    assert result == data[1], result
