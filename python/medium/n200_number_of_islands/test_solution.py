import pytest

from .solution import Solution


DATASET = [
    (
        [
            ["1", "0", "1"],
            ["0", "1", "0"],
            ["1", "1", "0"],
        ],
        3,
    ),
    (
        [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ],
        1,
    ),
    (
        [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ],
        3,
    ),
]


@pytest.mark.parametrize('data', DATASET)
def test_solution(data):
    result = Solution().num_islands(data[0])
    assert result == data[1], result
