import pytest

from .solution import Solution


DATASET = [
    (
        [[0, 1], [1, 0]],
        2,
    ),
    (
        [[0, 0, 0], [1, 1, 0], [1, 1, 0]],
        4,
    ),
    (
        [[1, 0, 0], [1, 1, 0], [1, 1, 0]],
        -1,
    ),
    (
        [[0]],
        1,
    ),
    (
        [
            [0, 0, 1, 0],
            [1, 0, 1, 0],
            [1, 1, 0, 1],
            [0, 0, 0, 0]
        ],
        4,
    )
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().shortestPathBinaryMatrix(data[0])
    assert result == data[1], result
