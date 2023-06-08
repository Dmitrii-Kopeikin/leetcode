import pytest

from .solution import Solution


DATASET = [
    ([1, 2, 3, 7], "Bob"),
    ([1, 2, 3, -9], "Alice"),
    ([1, 2, 3, 6], "Tie"),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().stoneGameIII(data[0])
    assert result == data[1], result
