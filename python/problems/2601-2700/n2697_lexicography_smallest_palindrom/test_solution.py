import pytest

from .solution import Solution

DATASET = [
    ("egcfe", "efcfe"),
    ("abcd", "abba"),
    ("seven", "neven"),
    ("n", "n"),
]


@pytest.mark.parametrize('data', DATASET)
def test_solution(data):
    result = Solution().makeSmallestPalindrome(data[0])
    assert result == data[1], result
    