
/*
TIME LIMIT EXCEEDED: O(n^2) Brute Force
*/

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int max = 0;
        for(int i=0; i<prices.size()-1; i++){
            for(int j=i+1; j<prices.size(); j++){
                int curr_price = prices[j] - prices[i];
                if(curr_price > max){
                    max = curr_price;
                }
            }
        }
        return max; 
    }
};


/*
4 ms solution 
        // O(N) time solution:
        // max profit = max value that comes after min value - min value of the vector
*/

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int profit = 0;
        if(prices.size() == 0 or prices.size() == 1)	//base cases; special cases 
            return profit;
        
        int min = prices[0];		//buy at minimum;
        for(int i=0; i<prices.size()-1; i++)  //for loop: find min value and max profit and update them at the same time
        {
            if(prices[i] <= min)
                min = prices[i];
            if(prices[i+1] - min > profit)
                profit = prices[i+1] - min;
        }
        if(prices.back()-min > profit)
            profit = prices.back()-min;
        return profit;
    }
};

/*
Why this is dynamic programming:
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/discuss/39112/Why-is-this-problem-tagged-with-%22Dynamic-programming%22/36893

*/


int maxProfit(vector<int> &prices) {
    int maxPro = 0;
    int minPrice = INT_MAX;
    for(int i = 0; i < prices.size(); i++){
        minPrice = min(minPrice, prices[i]);
        maxPro = max(maxPro, prices[i] - minPrice);
		//special case: prices[i] == minPrice for the last element i
    }
    return maxPro;
}
