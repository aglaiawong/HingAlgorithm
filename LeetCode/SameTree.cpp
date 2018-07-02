

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
 
//2ms 
#include <cstddef>
using namespace std; 
class Solution {
	public: 
	bool isSameTree(TreeNode *p, TreeNode *q) {
		if (p == NULL || q == NULL) return (p == q);		//compress some return statements
		return (p->val == q->val && isSameTree(p->left, q->left) && isSameTree(p->right, q->right));
	}
};


//############################################################################

//4ms
class Solution {
public:
    bool isSameTree(TreeNode* p, TreeNode* q) {
        if (p== NULL && q==NULL) return true;
        
        if(p!=NULL && q!=NULL){
            return((p->val == q->val)&&
                   isSameTree(p->left,q->left)&&
                   isSameTree(p->right,q->right)
            );
        }
        
        return false; 
    }
};

//############################################################################

//6ms
class Solution {
public:
    bool isSameTree(TreeNode* p, TreeNode* q) {
         return (!p && !q) || (p && q && p->val == q->val && isSameTree(p->left, q->left) && isSameTree(p->right, q->right));		//too many comparison on a line: (p&q) redundant comparison
    }
};