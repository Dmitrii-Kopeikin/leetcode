import pytest

from ..solution import Solution
from ..solution import TreeNode


def create_bst(values: list) -> TreeNode:
    if not values:
        raise ValueError()

    root = TreeNode(values[0])

    def add(value: int, node: TreeNode):
        if value is None:
            return
        if value > node.val:
            if node.right:
                add(value, node.right)
            else:
                node.right = TreeNode(value)
        if value < node.val:
            if node.left:
                add(value, node.left)
            else:
                node.left = TreeNode(value)

    for value in values[1:]:
        add(value, root)

    return root


DATASET = [
    (create_bst([4, 2, 6, 1, 3]), 1),
    (create_bst([1, 0, 48, None, None, 12, 49]), 1),
    (create_bst([236, 104, 701, None, 227, None, 911]), 9),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().getMinimumDifference(data[0])
    assert result == data[1], result
