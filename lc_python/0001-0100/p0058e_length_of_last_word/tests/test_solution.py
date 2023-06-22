import pytest

from ..solution import Solution


DATASET = [
    ('', 0),
    ('Hello World', 5),
    ('   fly me   to   the moon  ', 4),
    ('luffy is still joyboy', 6),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().lengthOfLastWord(data[0])
    assert result == data[1], result
