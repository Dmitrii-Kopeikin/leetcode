import pytest

from .solution import Solution, TreeNode


DATASET = [
    (TreeNode(3, left=TreeNode(9), right=TreeNode(20, left=TreeNode(15), right=TreeNode(7))), 3),
    (TreeNode(1, right=TreeNode(2)), 2)
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().maxDepth(data[0])
    assert result == data[1], result
