import pytest

from .solution import Solution


DATASET = [
    (([[1, 2], [3, 4]], 1, 4), [[1, 2, 3, 4]]),
    (([[1, 2], [3, 4]], 2, 4), [[1, 2], [3, 4]]),
    (([[1, 2], [3, 4]], 4, 1), [[1], [2], [3], [4]]),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().matrixReshape(*data[0])
    assert result == data[1], result
