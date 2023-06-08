import pytest

from ..solution import Solution


DATASET = [
    ((3, 7), 28),
    ((3, 2), 3),
    ((1, 10), 1),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().uniquePaths(*data[0])
    assert result == data[1], result
