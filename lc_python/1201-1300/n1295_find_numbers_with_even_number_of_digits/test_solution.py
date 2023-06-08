import pytest

from .solution import Solution as Solution


DATASET = [
    ([555,901,482,1771], 1),
    ([12,345,2,6,7896], 2),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().findNumbers(data[0])
    assert result == data[1], result
