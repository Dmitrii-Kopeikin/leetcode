import pytest

from ..solution_divide_and_conquer import Solution

from .test_solution import is_nodes_equal, DATASET


@pytest.mark.parametrize("data", DATASET)
def test_solution_divide_and_conquer(data):
    result = Solution().mergeKLists(data[0])
    assert is_nodes_equal(result, data[1]), result
