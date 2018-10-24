#include<bits/stdc++.h>
using namespace std; 

const int MAX = 100;
int getMaxGold(int gold[][MAX], int m, int n){	//size of 2-d array
	int result[m+1][n+1];		//all init to zero;
	
	for(int i=0; i<=m; i++){
		result[0][i] = 0;
	}
	
	for(int j=0; j<=0; j++){
		result[j][0] = 0;
	}
	
	for(int i=0; i<=m; i++){
		//consider (x,y-1), (x-1,y-1), (x-1, y+1) three cases 
		
		for(int j=0; j<=n; j++){
			
		}
	}
	
	
	
	return result[m][n];
	
}

/*
is this really a dynamic programming problem? 
all values are given! Just find the longest path! 
*/