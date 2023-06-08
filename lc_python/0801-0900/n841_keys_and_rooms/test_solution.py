import pytest

from .solution import Solution


DATASET = [
    ([[1],[2],[3],[]], True),
    ([[1,3],[3,0,1],[2],[0]], False),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().canVisitAllRooms(data[0])
    assert result == data[1], result
