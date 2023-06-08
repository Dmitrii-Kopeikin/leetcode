import pytest

from .solution_accepted import Solution
from .solution import Solution as SolutionOther

RADIANT = "Radiant"
DIRE = "Dire"
DATASET = [
    ("RD", RADIANT),
    ("RDD", DIRE),
    ("RDDRRDDD", DIRE),
    # ("RRDDD", RADIANT),
    ("RDDR", RADIANT),
    ("RRDD", RADIANT),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().predictPartyVictory(data[0])
    assert result == data[1], result


@pytest.mark.parametrize("data", DATASET)
def test_solution_other(data):
    result = SolutionOther().predictPartyVictory(data[0])
    assert result == data[1], result
