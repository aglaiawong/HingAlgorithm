/* beats 98.69 %
Number of Islands
DFS
*/
class Solution{
	public:
		int numIslands(vector<vector<char>>& grid){
			if(grid.size() == 0 || grid[0].size() == 0)		//boundary check: empty tree directly returns 0
				return 0;
				
			int res = 0;
			for(int i=0; i<grid.size(); i++){
				for(int j=0; j<grid[0].size(); j++){
					if(grid[i][j]=='1'){
						++res;	//the result, i.e. # of islands. 
						DFS(grid,i,j);	//for: turn all continguous '1' into '0' --> thus eliminated 1 island
						// that's why in above is the res++ 
					}
				}
			}
			
			return res; 
		}
		
	private:
		void DFS(vector<vector<char>>& grid, int x, int y){
			grid[x][y] = '0'; 	//to avoid repeated searching; same as mark as grey/'visited'
			
			//search for all 4 directions
			if(x>0 && grid[x-1][y]=='1')	 //index manipulation: always check bounds 
				DFS(grid, x-1,y);
			if(x<grid.size()-1 && grid[x+1][y]=='1')	//plus index: ensure originally index < bound; avoid out of bound
				DFS(grid, x+1, y);
			if(y>0 && grid[x][y-1]=='1')	//minus index: ensure orginally index>0; avoid index = -1
				DFS(grid, x, y-1);
			if(y<grid[0].size()-1 && grid[x][y+1] == '1')
				DFS(grid, x, y+1);
			
			//here: all 4 directions without 
		}
}


/*
Loop for all i,j for grid[i][j]
	- If grid[i][j]==1, do DFS on it
DFS is for turning all char in A SINGLE ISLAND into '0'
Basic operation of DFS: turn nodes into 'visited' and continue
*/