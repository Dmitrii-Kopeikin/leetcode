import pytest

from .solution import Solution


DATASET = [
    (([["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], [1,2]), 1),
    (([["+", "+", "+"], [".", ".", "."], ["+", "+", "+"]], [1, 0]), 2),
    (([[".","+"]], [0, 0]), -1)
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().nearestExit(*data[0])
    assert result == data[1], result
