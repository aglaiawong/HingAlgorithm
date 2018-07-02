# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        """
        DFS, with temp sum and target
        check is leaf or not first before put into result
        """
        result = []
        def walk(node, target, sum_temp, result_temp):
            if not node:
                return
            sum_temp += node.val
            result_temp.append(node.val)
            if sum_temp == target:
                if node.left is None and node.right is None:
                    result.append(result_temp[:])
            walk(node.left, target, sum_temp, result_temp)
            walk(node.right, target, sum_temp, result_temp)
            result_temp.pop()
            
        result = []
        walk(root, sum, 0, [])
        return result
        
		
##########################################################################
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def pathSum(self, root, sum):
		self.paths = []
		self.dfs(root, sum, [])
		return self.paths
		
	def dfs(self, root, sum, path):
		if not root:
			return 
		
		if root.val == sum and not any((root.left, root.right)):
			self.paths.append(path+[root.val])
			return
		
		self.dfs(root.left, sum-root.val, path+[root.val])
		self.dfs(root.right, sum-root.val, path+[root.val])