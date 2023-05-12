import pytest

from .solution import Solution


DATASET = [
    (19, True),
    (2, False),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().isHappy(data[0])
    assert result == data[1], result
