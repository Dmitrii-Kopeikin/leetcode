import pytest

from .solution import Solution


DATASET = [
    (("abcd", "abcde"), "e"),
    (("", "y"), "y"),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().findTheDifference(*data[0])
    assert result == data[1], result
