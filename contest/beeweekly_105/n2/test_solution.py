import pytest

from .solution import Solution

DATASET = [
    (("leetscode", ["leet","code","leetcode"]), 1),
    (("sayhelloworld", ["hello","world"]), 3),
    (("dwmodizxvvbosxxw",
["ox","lb","diz","gu","v","ksv","o","nuq","r","txhe","e","wmo","cehy","tskz","ds","kzbu"]), 7),
]


@pytest.mark.parametrize('data', DATASET)
def test_solution(data):
    result = Solution().minExtraChar(*data[0])
    assert result == data[1], result
