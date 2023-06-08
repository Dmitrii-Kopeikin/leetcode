import pytest

from .solution import Node
from .solution import Solution


DATASET = [
    (
        Node(
            1,
            [
                Node(3,[Node(5), Node(6)]),
                Node(2),
                Node(4),
            ],
        ),
        [1,3,5,6,2,4],
    ),
    (
        Node(
            1,
            [
                Node(2),
                Node(3,[Node(6), Node(7,[Node(11,[Node(14)])]),],),
                Node(4, [Node(8, [Node(12)])]),
                Node(5, [Node(9, [Node(13)]), Node(10)]),
            ],
        ),
        [1,2,3,6,7,11,14,4,8,12,5,9,13,10],
    ),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().preorder(data[0])
    assert result == data[1], result
