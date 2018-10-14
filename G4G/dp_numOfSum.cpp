/*
Given 3 numbers {1, 3, 5}, we need to tell
the total number of ways we can form a number 'N' 
using the sum of the given three numbers.
(allowing repetitions and different arrangements).
https://www.geeksforgeeks.org/solve-dynamic-programming-problem/
*/

int solve(int n){
	if(n<0)
		return 0; 
	if(n==0)
		return 1;
	return solve(n-1)+solve(n-3)+solve(n-5);
}

int dp[MAXN];	//init to -1
int solve(int n){
	if(n<0)
		return 0;
	if(n==0)
		return 1;
	if(dp[n]!=-1)
		return dp[n];
	return dp[n] = solve(n-1)+solve(n-3)+solve(n-5); 
}