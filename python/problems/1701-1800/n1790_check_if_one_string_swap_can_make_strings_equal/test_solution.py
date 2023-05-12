import pytest

from .solution import Solution
from .solution_other import Solution as SolutionOther


DATASET = [
    (("bank", "kanb"), True),
    (("attack", "defend"), False),
    (("kelb", "kelb"), True),
    (("aa", "ac"), False),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().areAlmostEqual(*data[0])
    assert result == data[1], result


@pytest.mark.parametrize("data", DATASET)
def test_solution_other(data):
    result = SolutionOther().areAlmostEqual(*data[0])
    assert result == data[1], result
