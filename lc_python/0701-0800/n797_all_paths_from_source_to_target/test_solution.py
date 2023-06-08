import pytest

from .solution import Solution


DATASET = [
    ([[1, 2], [3, 1], [3], []], [[0, 1, 3], [0, 2, 3]]),
    ([[4, 3, 1], [3, 2, 4], [3], [4], []], [
     [0, 4], [0, 3, 4], [0, 1, 3, 4], [0, 1, 2, 3, 4], [0, 1, 4]]),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().allPathsSourceTarget(data[0])
    assert sorted(result) == sorted(data[1]), result
