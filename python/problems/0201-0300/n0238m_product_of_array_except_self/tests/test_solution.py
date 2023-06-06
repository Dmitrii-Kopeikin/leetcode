from copy import deepcopy

import pytest

from ..solution_in_place import Solution as SolutionInPlace
from ..solution import Solution


DATASET = [
    ([1,2,3,4], [24, 12, 8, 6]),
    ([1, 2, 3, 4, 5], [120, 60, 40, 30, 24]),
    ([1,2,3,0], [0, 0, 0, 6]),
    ([2, 3], [3, 2]),
    ([1], []),
    ([0, 0, 0, 0, 0], [0, 0, 0, 0, 0]),
    ([1, 4, -3, 0, 3, 25], [0, 0, 0, -900, 0, 0]),
    ([0, 1, 2, 3, 4], [24, 0, 0, 0, 0]),
]



@pytest.mark.parametrize('data', deepcopy(DATASET))
def test_solution_in_place(data):
    nums = SolutionInPlace().productExceptSelf(data[0])
    assert nums == data[1], nums


@pytest.mark.parametrize('data', deepcopy(DATASET))
def test_solution(data):
    nums = Solution().productExceptSelf(data[0])
    assert nums == data[1], nums
