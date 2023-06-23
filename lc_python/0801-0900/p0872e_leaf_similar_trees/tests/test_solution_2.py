from collections import deque

import pytest

from ..solution_2 import Solution
from .test_solution import DATASET


@pytest.mark.parametrize("data", DATASET)
def test_solution_2(data):
    result = Solution().leafSimilar(*data[0])
    assert result == data[1], result
