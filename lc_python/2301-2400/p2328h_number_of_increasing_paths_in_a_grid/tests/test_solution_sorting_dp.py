import pytest

from ..solution_sorting_dp import Solution


DATASET = [
    ([[1, 1], [3, 4]], 8),
    ([[1], [2]], 3)
]


@pytest.mark.parametrize("data", DATASET)
def test_solution_sorting_dp(data):
    result = Solution().countPaths(data[0])
    assert result == data[1], result
