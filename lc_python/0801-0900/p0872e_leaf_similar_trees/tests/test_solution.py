from collections import deque

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


def create_bt(values: list, idx: int = 0) -> TreeNode:
    if idx >= len(values) or values[idx] is None:
        return None
    root = TreeNode(values[idx])
    root.left = create_bt(values, idx * 2 + 1)
    root.right = create_bt(values, idx * 2 + 2)
    print(root.val, root.left, root.right)
    return root


DATASET = [
    ((create_bt([3, 5, 1, 6, 2, 9, 8, None, None, 7, 4]), create_bt(
        [3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 8])), True),
    ((create_bt([1, 2, 3]), create_bt([1, 3, 2])), False)
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().leafSimilar(*data[0])
    assert result == data[1], result
