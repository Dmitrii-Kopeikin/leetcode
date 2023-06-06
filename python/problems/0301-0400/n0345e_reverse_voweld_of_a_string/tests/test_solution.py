import pytest

from ..solution import Solution


DATASET = [
    ('hello', 'holle'),
    ('leetcode', 'leotcede'),
    ('ltcd', 'ltcd'),
    ('egg', 'egg'),
    ('Aa', 'aA'),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().reverseVowels(data[0])
    assert result == data[1], result
