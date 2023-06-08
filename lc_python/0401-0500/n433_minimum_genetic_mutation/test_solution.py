import pytest

from .solution import Solution


DATASET = [
    (
        ("AACCGGTT", "AACCGGTA", ["AACCGGTA"]),
        1,
    ),
    (
        ("AACCGGTT", "AAACGGTA", ["AACCGGTA", "AACCGCTA", "AAACGGTA"]),
        2,
    ),
    (
        ("AGCAAAAA", "GACAAAAA", ["AGTAAAAA",
         "GGTAAAAA", "GATAAAAA", "GACAAAAA"]),
        4,
    ),
    (
        (
            "AAAACCCC",
            "CCCCCCCC",
            [
                "AAAACCCA", "AAACCCCA", "AACCCCCA", "AACCCCCC",
                "ACCCCCCC", "CCCCCCCC", "AAACCCCC", "AACCCCCC",
            ],
        ),
        4,
    )
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().minMutation(*data[0])
    assert result == data[1], result
