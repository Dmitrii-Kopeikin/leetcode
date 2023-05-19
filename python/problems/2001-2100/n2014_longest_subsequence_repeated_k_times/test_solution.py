import pytest

from .solution import Solution


DATASET = [
    (('letsleetcode', 2), 'let'),
    (('bb', 2), 'b'),
    (('ab', 2), ''),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().longestSubsequenceRepeatedK(*data[0])
    assert result == data[1], result
