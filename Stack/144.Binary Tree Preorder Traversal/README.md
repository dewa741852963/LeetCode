###### tags: `Stack`,`Tree`,`Depth-First Search`,`Binary Tree`

# LeetCode 144.Binary Tree Preorder Traversal

Given the ```root``` of a binary tree, return the preorder traversal of its nodes' values.  
  
 

>Example 1:  

![](https://assets.leetcode.com/uploads/2020/09/15/inorder_1.jpg)
```
Input: root = [1,null,2,3]
Output: [1,2,3]
```

>Example 2:
```
Input: root = []
Output: []
```
>Example 3:
```
Input: root = [1]
Output: [1]
```
 

### Constraints:

- The number of nodes in the tree is in the range ```[0, 100]```
- $-100 <= Node.val <= 100$




---
### Idea:
>先把右邊的印完再印左邊的就可以了。
### Solution

```python=
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def dfs(node):
            if not node:
                return
            ans.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ans
```
