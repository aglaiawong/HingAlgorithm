/*
332_Reconstruct_Itinerary
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
