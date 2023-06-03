import pytest

from .solution import Solution, TreeNode


DATASET = [
    (TreeNode(3, left=TreeNode(9), right=TreeNode(20, left=TreeNode(15), right=(TreeNode(7)))), 24),
    (TreeNode(1), 0),
    (TreeNode(1, left=TreeNode(2, left=TreeNode(4), right=TreeNode(5)), right=TreeNode(3)), 4),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().sumOfLeftLeaves(data[0])
    assert result == data[1], result
