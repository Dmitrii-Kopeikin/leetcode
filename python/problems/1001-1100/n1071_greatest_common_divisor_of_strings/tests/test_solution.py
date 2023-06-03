import pytest

from ..solution import Solution


DATASET = [
    (('ABCABC', 'ABC'), 'ABC'),
    (('ABABAB', 'ABAB'), 'AB'),
    (('LEET', 'CODE'), ''),
    (('', ''), ''),
    (('', 'ABC'), ''),
]


@pytest.mark.parametrize('data', DATASET)
def test_solution(data):
    result = Solution().gcdOfStrings(*data[0])
    assert result == data[1], result
