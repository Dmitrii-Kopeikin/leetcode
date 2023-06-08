import pytest

from ..solution import Solution


DATASET = [
    ('the sky is blue', 'blue is sky the'),
    ('  hello world  ', 'world hello'),
    ('a good   example', 'example good a'),
    (' ', ''),
    ('a', 'a'),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().reverseWords(data[0])
    assert result == data[1], result
