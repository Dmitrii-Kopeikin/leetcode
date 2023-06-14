import pytest

from ..solution_recursion import Solution
from .test_solution import DATASET


@pytest.mark.parametrize("data", DATASET)
def test_solution_recursion(data):
    result = Solution().decodeString(data[0])
    assert result == data[1], result
