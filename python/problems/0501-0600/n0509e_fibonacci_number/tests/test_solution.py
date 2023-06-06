import pytest

from ..solution import Solution


DATASET = [
    (2, 1),
    (3, 2),
    (4, 3),
    (0, 0),
    (1, 1),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().fib(data[0])
    assert result == data[1], result
