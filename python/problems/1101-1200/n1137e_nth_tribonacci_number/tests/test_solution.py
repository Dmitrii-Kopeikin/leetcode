import pytest

from ..solution import Solution


DATASET = [
    (4, 4),
    (25, 1389537),
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().tribonacci(data[0])
    assert result == data[1], result
