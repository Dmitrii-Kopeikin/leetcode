import pytest

from ..solution_reduce import Solution
from .test_solution import DATASET


@pytest.mark.parametrize("data", DATASET)
def test_solution_reduce(data):
    result = Solution().singleNumber(data[0])
    assert result == data[1], result
