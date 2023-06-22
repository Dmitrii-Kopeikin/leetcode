import pytest

from ..solution_split import Solution
from .test_solution import DATASET


@pytest.mark.parametrize("data", DATASET)
def test_solution_split(data):
    result = Solution().lengthOfLastWord(data[0])
    assert result == data[1], result
