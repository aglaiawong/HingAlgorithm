int LCS(string X, string Y){
	
	// noted X and Y may not be the same! 
	int m = X.size();
	int n = Y.size();
	
	int c[m+1][n+1];	//the extra row and column for special case: 0
	for(int i=1;i<=m;i++)
		c[i][0] = 0;		//horizontal x
	for(int j=0;j<=n;j++)
		c[0][j] = 0; 		//vertical y
	
	for(int i=1; i<=m; i++){
		for(int j=1; j<=n; j++){
			if(X[i] == Y[j])
				c[i][j] = c[i-1][j-1]+1;
			else if(c[i-1][j] >= c[i][j-1])		//left cell >= upper;.l/
				c[i][j] = c[i-1][j];
			else
				c[i][j] = c[i][j-1]; 
		}
		//c[i-1][j] or c[i][j-1] means either not take a char from X or from Y
	}
	return c;
} 