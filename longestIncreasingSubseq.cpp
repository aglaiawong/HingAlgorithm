/*
	longest increasing subsequence
	lis[i]: length of longest inc subseq ends at idx i
	subsequence: need not contiguous 
*/

int lis(vector<int> arr, int n){
	vector<int> lis(n);		//initialize an empty vector with size n
	for(int i=0; i<n; i++){
		lis[i] = 1;
	}
	
	for(int i=0; i<n; i++)
		for(int j=0; j<n; j++)
			if(arr[i]>arr[j] and lis[j]+1>lis[i])
				lis[i] = lis[j]+1;
			
	for(int i=0; i<n; i++)
		if(max < lis[i])
			max = lis[i];

	return max

}

/*
	longest common subsequence: 2D DP problem
	start compare if the same the last letters from both strings, then recurse on the smaller part of string 
	e.g. lcs('AXYT', 'AYZX') recuse on lcs('AXY', 'AYZX') and lcs('AXYT', 'AYZ')
	i.e. since last char on both strings are not same, recurse on either of them with 1 char shorter
	reconstruct the common subseq: reach diagonal arrow, append the char in current cell to the front of string
*/

// X = "AGGTAB", Y="GXTXAYB"
int lcs(char* X, char* Y, int m, int n){
	int L[m+1][n+1];	//One extra for the empty set {0} with no char at all
	int i,j;
	
	for(int i=0; i<=m; i++){
		for(int j=0; j<=n; j++){
			if(i==0 || j==0)	//match every char in every string with a null set first
				L[i][j] = 0;
			else if(X[i-1] == Y[j-1])	//take the diagonal
				L[i][j] = L[i-1][j-1]+1;
			else
				L[i][j] = max(L[i-1][j], L[i][j-1]);
		}
	}
	
	return L[m][n];
}

int max(int a, int b){
	return (a>b)?a:b;
}
