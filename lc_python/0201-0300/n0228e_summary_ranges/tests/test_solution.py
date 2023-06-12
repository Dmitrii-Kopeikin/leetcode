import pytest

from ..solution import Solution


DATASET = [
    ([0, 1, 2, 4, 5, 7], ['0->2', '4->5', '7']),
    ([0, 2, 3, 4, 6, 8, 9], ['0', '2->4', '6', '8->9']),
    ([0, 2, 3, 4, 6, 8, 9, 11], ['0', '2->4', '6', '8->9', '11']),
    ([], []),
    ([1], ['1']),
]


@pytest.mark.parametrize('data', DATASET)
def test_solution(data):
    result = Solution().summaryRanges(data[0])
    assert result == data[1], result
