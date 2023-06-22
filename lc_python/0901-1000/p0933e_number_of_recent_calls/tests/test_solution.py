import pytest

from ..solution import RecentCounter


DATASET = [
    ([1, 100, 3001, 3002], [1, 2, 3, 3]),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    recentCounter = RecentCounter()
    result = []
    for t in data[0]:
        result.append(recentCounter.ping(t))
    assert result == data[1], result
