import pytest

from ..solution_dfs_memo import Solution
from .test_solution_sorting_dp import DATASET


@pytest.mark.parametrize("data", DATASET)
def test_solution_dfs_memo(data):
    result = Solution().countPaths(data[0])
    assert result == data[1], result
