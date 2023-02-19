###### tags: `Tree`, `Breadth-First Search`, `Binary Tree`

# LeetCode 103.Binary Tree Zigzag Level Order Traversal
Given the `root` of a binary tree, return _the zigzag level order traversal of its nodes' values_. (i.e., from left to right, then right to left for the next level and alternate between).
  
 

>Example 1:
>![][https://assets.leetcode.com/uploads/2021/02/19/tree1.jpg]
```
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
```
>Example 2:
```
Input: root = [1]
Output: [[1]]
```
>Example 3:
```
Input: root = []
Output: []
```
 

### Constraints:

- The number of nodes in the tree is in the range `[0, 2000]`.
- $-100 <= Node.val <= 100$

---


### Idea:
>https://leetcode.wang/leetcode-102-Binary-Tree-Level-Order-Traversal.html
### Solution:

Python:
```python=

```

C++:
```cpp=
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        vector<vector<int>>ans;
        vector<int>temp;
        if(root==NULL){ //if no element then return empty vector of vector.
            return ans;
        }
        queue<TreeNode*>q;
        q.push(root);

        int level=1;
        ans.push_back({root->val}); // pushing root into ans vector(root value is always included)
        while(!q.empty()){
            level++;
            int size=q.size();
            while(size--){
                auto front=q.front();
                q.pop();
                if(front->left!=NULL){  //if left exist then add it to queue and also in tempropry vector strong its node value
                    q.push(front->left);
                    temp.push_back(front->left->val);
                }
                if(front->right!=NULL){  //similar for right part
                    q.push(front->right);
                    temp.push_back(front->right->val);
                }  
            }
        if(level%2==0){          //checking when to make it zig zag .when even then make it zig zig .just reverse the temprory vector.
            reverse(temp.begin(),temp.end());
         }
        if(temp.size()>0){
             ans.push_back(temp);
            }  
            temp.clear();
        }
        return ans;
    }
};
```