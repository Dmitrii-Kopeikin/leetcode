import pytest

from .solution import Solution


DATASET = [
    (
        [
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
        ],
        8,
    ),
    ([[5]], 5),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().diagonalSum(data[0])
    assert result == data[1], result
