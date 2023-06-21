import pytest

from ..solution_sorting import Solution
from .test_solution import DATASET


@pytest.mark.parametrize("data", DATASET)
def test_solution_sorting(data):
    result = Solution().minCost(*data[0])
    assert result == data[1], result
