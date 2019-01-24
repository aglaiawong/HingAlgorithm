/*
DP by tabulation
to find factorial x
*/

int factorial(int x){
	int dp[MAXN];
	int dp[0] = 1;	
	
	for(int i=1; i<=n; i++){
		dp[i] = dp[i-1]*i;		//rmb, here always starts/builds from base case
	}
}

// Memoized version to find factorial x

int dp[MAXN];		//init to -1
int factorial(int x){
	if(x==0)
		return 1;
	if(dp[x]!=-1)
		return dp[x];
	return (dp[x] = x * factorial(dp[x-1]));	//x starts from x, memotization
	// peel onion layer-by-layer; 
	// returning the value == layer-by-layer, rebuild the onion tgt 
}


//Tabulation version to find factorial x
int dp[MAXN];
//base case 
int dp[0] = 1; 
for(int i=1; i<=n; i++){	//i starts from 1 --> bottom up TABULATION
	dp[i] = dp[i-1]*1;
}
