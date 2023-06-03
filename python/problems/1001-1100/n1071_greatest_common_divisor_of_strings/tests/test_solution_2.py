import pytest

from ..solution_2 import Solution
from .test_solution import DATASET


@pytest.mark.parametrize('data', DATASET)
def test_solution_2(data):
    result = Solution().gcdOfStrings(*data[0])
    assert result == data[1], result
