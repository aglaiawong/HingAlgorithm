/*
746. Min Cost Climbing Stairs
4ms, beat 100%
*/
class Solution{
	int minCostClimbingStairs(vector<int>& cost){
		// first, build a linear vector to hold optimal solutions 
		int n = cost.size();
		vector<int> dp(n);
		
		//base case
		dp[0] = cost[0];
		dp[1] = cost[1];
		
		//dp recursive formula
		for(int i=2; i<n; i++)
			dp[i] = cost[i] + min(dp[i-2], dp[i-1]);	//always look back, not forward, in dp. 
		
		return min(dp[n-2], dp[n-1]); 
		// i.e. top floor n reached either 1 or 2 stairs away; so return the minimum
		
	}
}