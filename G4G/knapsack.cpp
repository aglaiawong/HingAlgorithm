#include <iostream>
#include <algorithm>
using namespace std;


/*
DP in knapsack problem:
2 variables: capacity of knapsack and 
*/

// W, wt[] and val[] are constant terms 
// W: max capacity of knapsack; wt[] and val[] are weights and values of items; n is the number of items 
int knapsack(int W, int wt[], int val[], int n){
	int i,w;	// 'w': current knapsack capacity; 'n': current item to csdr
	int K[n+1][W+1];	//why '+1'? basis for packing items in a 0 capacity knapsack. 
	
	
	/*
		prove of correctness of nested loop:
		for evey item, consider all weights to contain it. 
	*/
	for(i=0;i<n;i++){
		for(w=0; w<=W; w++){
			if(i==0 || w == 0) K[i][w]=0;
			else if(wt[i-1] <= w)	//when still hv space there are 2 choices: whether to pack/not pack a particular item i; 
				K[i][w] = max(val[i-1]+K[i-1][w-wt[i-1]], K[i-1][w]);
				//all got '-1' cz original K[n+1][W+1] covers special case
				// where item = 0 and capacity = 0; 
			else
				K[i][w] = k[i-1][w];
		}
	}
	return K[n][W];		//soln to dp: at right bottom corner; 
}

int main() 
{ 
    int val[] = {60, 100, 120}; 
    int wt[] = {10, 20, 30}; 
    int  W = 50; 
    int n = sizeof(val)/sizeof(val[0]); 
    printf("%d", knapSack(W, wt, val, n)); 
    return 0; 
} 

