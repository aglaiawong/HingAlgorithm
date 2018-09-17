/*
198_House Robber
Wrong answer 
*/

class Solution {
public:
    int rob(vector<int>& nums) {
		int size = nums.size();
		
		if(size == 0){
			return 0;
		} else if(size == 1){
			return nums[0];
		}
		
		vector<int> dp(size);
		
		dp[0] = nums[0];
		dp[1] = max(nums[0], nums[1]);
		
		for(int i=2; i<size; i++){
			dp[i] = max(dp[i-2]+dp[i], dp[i-1]);	//WRONG: ignore cases where 2 consecutive housese are not robbed; 
		}
		
		return max(dp[size-1], dp[size-2]);
	}
};


/*
0ms solution
*/

class Solution {
public:
    int rob(vector<int>& nums) {
        
        if(nums.size() == 0)
            return 0;
        
        // whether prev house has been robbed or not
        int prev_no = 0;        
        int prev_yes = nums[0];
        int result = max(prev_no, prev_yes);
        
        // curr_no: store the largest amount of money got so far if the current house is not robbed
        // curr_yes: store the larget amount of money got so far if the current house if being robbed
        int curr_no, curr_yes;
        
        for(int i = 1; i < nums.size(); i++)
        {
            curr_no = max(prev_no, prev_yes);   // curr not robbed --> path can came from prev_no or prev_yes
            curr_yes = prev_no + nums[i];       // curr being robbed --> only path came from prev_no
            
            prev_no = curr_no;                  
            prev_yes = curr_yes;
        }
            
        return max(prev_no, prev_yes);
    }
};