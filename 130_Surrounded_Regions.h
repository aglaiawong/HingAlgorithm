/*
130_Surrounded_Regions
*/

void solve(vector<vector<char>>& board){
	int i,j;
	int row = board.size();
	int col = board[0].size();
	
	if(!row)
		return;		//basic emptiness checking

	int col = board[0].size();		//throw exception if above not checked
	
	//check the boundaries: the first item & last item of each row 
	for(int i=0; i<row; i++){
		check(board, i, 0, row, col);		//check first item of the row 
		if(col>1)	//again, bound check for subsequent idx decrements
			check(board, i, col-1, row, col); 		//check last item of the row 
	}
	
	//check the boundaries: the first and last item of a column 
	for(int j=0; j+1<col; j++){
		check(board, 0, j, row, col);		//first item of a column 
		if(row>1)
			check(board, i-1, j, row, col);		//last item of a column 
	}
	
	for(i=0;i<row;i++)
		for(j=0;j<col;j++)
			if(board[i][j]=='O')
				board[i][j]='X';
			
	for(i=0;i<row;i++)
		for(j=0;j<col;j++)
			if(board[i][j]=='1')
				board[i][j]='O';	

}

//only the outtermost 2 layers of 4 boundaries' cells reaches this function 
//recall, all '1's are placeholder for 'O' in the final answer 
//only cells near the boundaries affected; all cells expand outwards 
void check(vector< vector<string> >& vec, int i, int j, int row, int col){
	if(vec[i][j]=='O'){
		vec[i][j] = '1';
		if(i>1)
			check(vec, i-1, j, row, col);
		if(j>1)
			check(vec, i, j-1, row, col);
		if(i+1<row)
			check(vec, i+1, j, row, col);
		if(j+1<col)
			check(vec, i, j+1, row, col);
	}
	
}