import pytest

from ..solution import Solution

DATASET = [
    (("1", "12", 1, 8), 11),
    (("1", "5", 1, 5), 5),
]


@pytest.mark.parametrize('data', DATASET)
def test_solution(data):
    result = Solution().count(*data[0])
    assert result == data[1], result
