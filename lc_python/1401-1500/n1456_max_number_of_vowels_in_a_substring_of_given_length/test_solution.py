import pytest

from .solution import Solution
from .solution_deque import Solution as SolutionDeque


DATASET = [
    (("abciiidef", 3), 3),
    (("aeiou", 2), 2),
    (("leetcode", 3), 2),
    (("kjghtkfhj", 3), 0),
    (("", 1), 0),
    (("aaiuyopoiddspoo", 4), 4),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution_deque(data):
    result = SolutionDeque().maxVowels(*data[0])
    assert result == data[1], result


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().maxVowels(*data[0])
    assert result == data[1], result
