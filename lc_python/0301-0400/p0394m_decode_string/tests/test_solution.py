import pytest

from ..solution import Solution


DATASET = [
    ("abc", "abc"),
    ("3[a]2[bc]", "aaabcbc"),
    ("3[a2[c]]", "accaccacc"),
    ("2[abc]3[cd]ef", "abcabccdcdcdef"),
    ('a', 'a'),
    ('20[a]', 'aaaaaaaaaaaaaaaaaaaa'),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().decodeString(data[0])
    assert result == data[1], result
