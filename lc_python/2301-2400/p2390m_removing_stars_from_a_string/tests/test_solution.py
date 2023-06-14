import pytest

from ..solution import Solution


DATASET = [
    ("leet**cod*e", "lecoe"),
    ("erase*****", ""),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().removeStars(data[0])
    assert result == data[1], result
