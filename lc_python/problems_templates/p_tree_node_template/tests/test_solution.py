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
    return root


DATASET = [
    (None, None),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().some_method(data[0])
    assert result == data[1], result
