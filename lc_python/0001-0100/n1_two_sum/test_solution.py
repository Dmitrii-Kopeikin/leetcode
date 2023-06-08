import pytest

from .solution import Solution
from .solution_less_than_on2 import Solution as SolutionDict


DATASET = [
    (([2, 7, 11, 15], 9), ([0, 1], [1, 0])),
    (([3, 2, 4], 6), ([1, 2], [2, 1])),
    (([3, 3], 6), ([0, 1], [1, 0])),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().twoSum(*data[0])
    assert result in data[1], result


@pytest.mark.parametrize("data", DATASET)
def test_solution_dict(data):
    result = SolutionDict().twoSum(*data[0])
    assert result in data[1], result
