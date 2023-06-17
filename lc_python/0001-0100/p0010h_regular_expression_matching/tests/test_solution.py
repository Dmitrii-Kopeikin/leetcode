import pytest

from ..solution import Solution


DATASET = [
    (('aa', 'a'), False),
    (('aa', 'a*'), True),
    (('ab', '.*'), True),
    (('abc', '.*c'), True),
    (('abf', '.*c'), False),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().isMatch(*data[0])
    assert result == data[1], result
