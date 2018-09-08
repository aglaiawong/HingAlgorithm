/*
53. Maximum Subarray
- assume contiguous subarray
- thus, problem becomes whether to include/exclude certain elements
- alternatively, the subarray picking up current element or not
- negative element/subarray would decrease the result; thus not wanted 
*/


//java version
public int maxSubArray(int[] A) {
        int n = A.length;
        int[] dp = new int[n];//dp[i] means the maximum subarray ending with A[i];
		
		//base case & return value
        dp[0] = A[0];
        int max = dp[0];
        
		//recursive formulation from subproblem
        for(int i = 1; i < n; i++){
			// a max subarray can either include/exclude previous sequence
            dp[i] = A[i] + (dp[i - 1] > 0 ? dp[i - 1] : 0);
            max = Math.max(max, dp[i]);
        }
        
        return max;
}


//C++ version 
class Solution {
	public:
		int maxSubArray(vector<int>& nums) {
			int ret = nums[0];
			for (int i = 1; i < nums.size(); i++){
				
				/*
				 i.e. optimal solution at position i either:
				 i) contain only itself
				 ii) or itself combined with latest subarray, due to contiguity			
				*/
				
				nums[i] = max(nums[i], nums[i] + nums[i-1]);

				ret = max (ret, nums[i]);
			}
			return ret;
		}
};