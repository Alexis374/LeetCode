/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
 /*
思路同python版本，注意vector的方法 push_back pop_back(无返回值) size(返回) back()(返回最后一个元素)
 */
class Solution {
public:
    vector<int> preorderTraversal(TreeNode *root) {
        vector<int> vi;
        if(root==NULL)return vi;
        vector<TreeNode*> vt;
        vt.push_back(root);
        while(vt.size()){
            TreeNode* top = vt.back();
            vt.pop_back();
            vi.push_back(top->val);
            if(top->right)vt.push_back(top->right);
            if(top->left)vt.push_back(top->left);
        }
        return vi;
    }
};