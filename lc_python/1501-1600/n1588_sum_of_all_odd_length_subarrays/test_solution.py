import pytest

from .solution import Solution
from .solution_other import Solution as SolutionOther


DATASET = [
    ([1,4,2,5,3], 58),
    ([1,2], 3),
    ([10,11,12], 66),
    ([1], 1),
    ([], 0),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().sumOddLengthSubarrays(data[0])
    assert result == data[1], result


@pytest.mark.parametrize("data", DATASET)
def test_solution_other(data):
    result = SolutionOther().sumOddLengthSubarrays(data[0])
    assert result == data[1], result
