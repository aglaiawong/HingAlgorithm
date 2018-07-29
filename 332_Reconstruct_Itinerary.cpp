/*
332_Reconstruct_Itinerary
beat 45.59%
12ms
*/

vector<string> findItinerary(vector<pair<string, string>> tickets){		//an array of pairs 
	for(auto ticket : tickets)
		target[ticket.first].insert(target[ticket.second]);		//collections of dest sorted by src airports
	visit("JFK");
	return vector<string>(route.rbegin(), route.rend());
}

map<string, multiset<string>> targets;	//map all possible destination under same airport 
vector<string> route; 	//final result holder 

void visit(string airport){		//the DFS part
	
	while(targets[airport].size()){
		string next = *targets[airport].begin();	//the prev dest is the src airport in next stop 
		targets[airport].erase(targets[airport].begin());  //N.B. the starting airport DNC! only des change! 
		visit(next);
	}
	
	//when reaching the last destination, 
	//targets[airport].size() == 0
	//we push targets into route in a reverse order due to recursion
	route.push_back(airport);
	
}

/*
8ms
- improv. by using unordered_map instead of the orderred map
*/
class Solution {
public:
    vector<string> findItinerary(vector<pair<string, string>> tickets) {
        vector<string> res;
        unordered_map<string, multiset<string>> m;
        for(int i = 0; i < tickets.size(); i++)
            m[tickets[i].first].insert(tickets[i].second);
        visit("JFK", m, res);
        reverse(res.begin(), res.end());
        return res;
    }
    
    void visit(string airport, unordered_map<string, multiset<string>>& m, vector<string>& route) {
        while(!m[airport].empty()){
            string next = *m[airport].begin();		//access O(1) for unordered_map
													//c.f. O(lgN) for (ordered) map
            m[airport].erase(m[airport].begin());
            visit(next, m, route);
        }
        route.push_back(airport);
    }
};


