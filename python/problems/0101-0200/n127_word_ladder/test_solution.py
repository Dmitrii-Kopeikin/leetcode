import pytest

from .solution import Solution


DATASET = [
    (("hit", "cog", ["hot","dot","dog","lot","log","cog"]), 5),
    (("hit", "cog", ["hot","dot","dog","lot","log"]), 0),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().ladderLength(*data[0])
    assert result == data[1], result
