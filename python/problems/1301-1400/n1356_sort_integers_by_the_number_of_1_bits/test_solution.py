import pytest

from .solution import Solution


DATASET = [
    ([0,1,2,3,4,5,6,7,8], [0,1,2,4,8,3,5,6,7]),
    ([1024,512,256,128,64,32,16,8,4,2,1], [1,2,4,8,16,32,64,128,256,512,1024]),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().sortByBits(data[0])
    assert result == data[1], result
