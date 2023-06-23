import pytest

from ..solution_1 import Solution
from .test_solution import DATASET


@pytest.mark.parametrize("data", DATASET)
def test_solution_1(data):
    result = Solution().longestArithSeqLength(data[0])
    assert result == data[1], result
