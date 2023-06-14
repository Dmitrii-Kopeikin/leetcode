import pytest

from ..solution import Solution


DATASET = [
    ([5, 10, -5], [5, 10]),
    ([8, -8], []),
    ([10, 2, -5], [10]),
    ([10, 2, -11], [-11]),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().asteroidCollision(data[0])
    assert result == data[1], result
