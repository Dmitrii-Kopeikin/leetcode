import pytest

from .solution import Solution


DATASET = [
    ("G()()()()(al)", "Gooooal"),
    ("(al)G(al)()()G", "alGalooG"),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().interpret(data[0])
    assert result == data[1], result
