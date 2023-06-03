import pytest

from .solution import Solution


DATASET = [
    ([[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]],
     [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]]),
    ([[1, 1], [1, 0]], [[1, 1], [1, 1]]),
    (
        [[0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 0, 0], [0, 1, 0, 0, 1, 0], [
            0, 0, 1, 0, 1, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0]],
        [[0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 0, 0], [0, 1, 0, 0, 1, 0], [
            0, 0, 1, 0, 1, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0]],
    )
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().gameOfLife(data[0])
    assert data[0] == data[1], result
