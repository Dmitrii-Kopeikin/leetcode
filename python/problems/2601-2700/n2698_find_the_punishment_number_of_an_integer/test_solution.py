import pytest

from .solution import Solution

DATASET = [
        (10, 182),
        (37, 1478),
    ]


@pytest.mark.parametrize('data', DATASET)
def test_solution(data):
    result = Solution().punishmentNumber(data[0])
    assert result == data[1], result
    