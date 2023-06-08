import pytest

from .solution import Solution


DATASET = [
    ([[1, 0, 1], [0, 0, 0], [1, 0, 1]], 2),
    ([[1, 0, 0], [0, 0, 0], [0, 0, 0]], 4),
    (
        [
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1]
        ],
        -1,
    ),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().maxDistance(data[0])
    assert result == data[1], result
