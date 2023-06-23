import pytest

from ..solution import Solution
from ..solution import TreeNode


def create_bst(values: list) -> TreeNode:
    if not values:
        return None

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

def is_nodes_equal(node_1: TreeNode, node_2: TreeNode):
    if node_1 and node_2 and node_1.val == node_2.val or not node_1 and not node_2:
        return True
    return False

DATASET = [
    ((create_bst([4, 2, 7, 1, 3]), 2), create_bst([2, 1, 3])),
    ((create_bst([4, 2, 7, 1, 3]), 5), create_bst([])),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().searchBST(*data[0])
    assert is_nodes_equal(result, data[1]), result
