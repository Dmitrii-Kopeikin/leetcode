import pytest

from .solution import Solution


DATASET = [
    [([1, 2], [-2, -1], [-1, 2], [0, 2]), 2],
    [
        (
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
        ),
        4096,
    ],
    [
        (
            [0, -2, 1, 3, 4],
            [0, 2, -8, 0, -3],
            [0, -1, 0, 4, 3],
            [0, 9, 0, 8, 0],
        ),
        43,
    ],
]


@pytest.mark.parametrize('data', DATASET)
def test_solution(data):
    result = Solution().fourSumCount(*data[0])
    assert result == data[1], result
