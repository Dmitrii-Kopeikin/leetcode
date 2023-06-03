import pytest

from .solution import Solution
from .solution_ordered_dict import Solution as SolutionDict
from .solution_ordered_dict_v2 import Solution as SolutionDictV2


DATASET = [
    ((["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz"), True),
    ((["word","world","row"], "worldabcefghijkmnpqstuvxyz"), False),
    ((["apple","app"], "abcdefghijklmnopqrstuvwxyz"), False),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().isAlienSorted(*data[0])
    assert result == data[1], result


@pytest.mark.parametrize("data", DATASET)
def test_solution_ordered_dict(data):
    result = SolutionDict().isAlienSorted(*data[0])
    assert result == data[1], result


@pytest.mark.parametrize("data", DATASET)
def test_solution_ordered_dict_v2(data):
    result = SolutionDictV2().isAlienSorted(*data[0])
    assert result == data[1], result
