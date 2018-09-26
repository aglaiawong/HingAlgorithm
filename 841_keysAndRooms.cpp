/*
841. Keys and Rooms
*/

//BFS

class Solution {
public:
	bool canVisitAllRooms(vector<vector<int>>& rooms){
		unordered_set<int> visited; 
		queue<int> to_visit;
		
		to_visit.push(0);
		while(!to_visit.empty()){
			int curr = to_visit.front();
			to_visit.pop();
			visited.insert(curr);
			for(int k: rooms[curr]) if (visited.find(k) == visited.end())		//get keys to visited room
				to_visit.push(k);
				
				
			/* a typical formulation of dfs:
			use a for-loop + recursive function inside;
			--> to induce the effect of backtracking when lower part of tree's finished;
			*/
		}
		return visited.size() == room.size();
	}
};

//DFS formulation
class Solution{
	void dfs(vector<vector<int>>& rooms, unordered_set<int>& keys, unordered_set<int>& visited, int curr){
		visited.insert(curr);
		for (int k: rooms[curr]) keys.insert(k);
		for (int k: keys) if (visited.find(k) == visited.end())
			dfs(rooms, keys, visited, k);	//only 1 dfs happens at a time; next dfs starts only when the previous dfs returns (either return due to no unvisited keys, or used up all keys so far)
	}
	
	public:
		bool canVisitAllRooms(vector<vector<int>>& rooms){
			unordered_set<int> keys;
			unordered_set<int> visited;
			
			/*
			BFS use a stack to micmic layer-wise search
			*/
			
			dfs(rooms, keys, visited, 0);
			return visited.size() == rooms.size();
		}
}



