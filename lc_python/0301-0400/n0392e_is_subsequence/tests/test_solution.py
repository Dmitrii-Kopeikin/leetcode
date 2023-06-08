import pytest

from ..solution import Solution


DATASET = [
    (('abc', 'ahbgdc'), True),
    (('axc', 'ahbgdc'), False),
    (('', 'abc'), True),
    (('', ''), True),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().isSubsequence(*data[0])
    assert result == data[1], result
