import pytest

from .solution_recursion import Solution


DATASET = [
    (([1, 4, 2], [1, 2, 4]), 2),
    (([2, 5, 1, 2, 5], [10, 5, 2, 1, 5, 2]), 3),
    (([1, 3, 7, 1, 7, 5], [1, 9, 2, 5, 1]), 2),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().maxUncrossedLines(*data[0])
    assert result == data[1], result
