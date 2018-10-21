#include<stdio.h> 
#include<limits.h> 

int max(int a, int b){ return (a>b)? a:b;}

/*
M1: recursive formulation
problem: overlapping subproblem resolve and resolve again and again
*/
int cutRod(int price[], int n){
	if(n==0)
		return 0;
	int max_val = INT_MIN; 
	
	for(int i=1; i<=n;i++){
		max_val = max(max_val, price[i]+cutRod(price, n-i)); 
	} 	//here: no construction of optimal solution; just return ultimate goal
	
	return max_val; 
}
/* Proof of correctness
cutRod(price, n-i-1): (n-i-1)=0, then max=(INT_MIN, price[n-1])
*/



/*
SOLN: avoid resolving subproblem by tabulation
NOTE: no recursion here! 
*/

int cutRod(int price[], int n){	//n as price.size()
	int r[n+1];		//special case in dp: first column/row =0
	r[0] = 0;		//step 1: init the base case for tabulation 
	
	for(int j=1; j<=n+1; j++){
		int max_val = INT_MIN;	
		for(int i=1; i<=j; i++){
			max_val = max(max_val, p[i]+r[j-i]);	//j fixed
		}
		r[j]=max_val;
	}
	
	return r[n+1]; 
}

/*
SOLN: memotization
*/

int memoized_cut_rod_aux(int p[], int n, int r[]){
	if(r[n]>=0) return r[n];		//already calculated last element; simply returns this as answer 
	int q;
	if(n==0)	//rod is of length=0
		q = 0;
	else if(q == INT_MIN){
		for(int i=1; i<=n;i++){		//must start from 1
			q = max(q, p[i]+memoized_cut_rod_aux(p, n-i, r))
			//memotize by recursion, top-down 
			// current maximum, q, stores the most profitable segmentation so far, while trying new cuts, finally take the maximum
		}
	}
	
	r[n] = q;
	return q; 
}


int memoized_cut_rod(int p[], int n){
	//p[0] = 0 assumed; 
	
	int r[n+1];		//r[0,1,...,n]
	for(int i=0;i<=n;i++){
		r[i] = INT_MIN;		//memoization: top-down needs initializations
	}
	
	return memoized_cut_rod_aux(p,n,r);		//just to start the recursion 
}
