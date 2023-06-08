import pytest

from .solution import Solution


DATASET = [
    (
        [
            [1, 2, 2, 3, 5],
            [3, 2, 3, 4, 4],
            [2, 4, 5, 3, 1],
            [6, 7, 1, 4, 5],
            [5, 1, 1, 2, 4],
        ],
        [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]],
    ),
    (
        [[1]],
        [[0, 0]],
    )
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().pacificAtlantic(data[0])
    result.sort()
    assert result == sorted(data[1]), result
