import pytest

from .solution import Solution


DATASET = [
    ([[1,2,3],[4,5,6],[7,8,9]], [1,2,3,6,9,8,7,4,5]),
    ([[1,2,3,4],[5,6,7,8],[9,10,11,12]], [1,2,3,4,8,12,11,10,9,5,6,7]),
]



@pytest.mark.parametrize('data', DATASET)
def test_solution(data):
    nums = Solution().spiralOrder(data[0])
    assert nums == data[1], nums
