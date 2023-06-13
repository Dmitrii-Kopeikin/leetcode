import pytest

from ..solution import Solution


DATASET = [
    (("abc", "bca"), True),
    (("a", "aa"), False),
    (("caabbb", "abbccc"), True),
    (("", ""), True),
    (("", "a"), False),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().closeStrings(*data[0])
    assert result == data[1], result
