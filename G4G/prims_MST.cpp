#include<iostream>
#include<queue>
#define INF 0x3f3f3f3f

using namespace std;

typedef pair<int,int> iPair; 

class Graph{
	int size;
	list<pair<int,int> > *adj;		// a set of weighted graph 

public:
	Graph(int n);
	void addEdge(int src, int des, int w);
	void prims(int s);
}

Graph::Graph(int n){
	size = n;
	adj = new list<iPair>[n]; 	
}

void Graph::addEdge(int src, int des, int w){
	// undirected graph's adjacey list
	adj[src].push(make_pair(des,w));
	adj[des].push(make_pair(src,w));
}

void Graph::prims(int s){
	priority_queue<iPair, vector<iPair>, greater<iPair> > pq; 
	
	int src = 0;
	
	vector<int> key(n, INF);	//size of n, all init val of INF
	vector<int> parent(n, -1);
	vector<bool> inMST(V, false);
	
	pq.push(make_pair(0,src));
	key[src] = 0; 
	
	while(!pq.empty()){
		int u = pq.top().second;
		pq.pop();
		
		inMST[u] = true; 
		list<iPair>::iterator it;
		for(it = adj[u].begin(); it!=adj[u].end(); it++){
			int v = (*it).first;
			int weight = (*it).second;
			
			if(!inMST[u] && key[v]>weight){
				
			}
		}
	}
	
	
	
	bool* visited = new bool[n];
	for(int i=0; i<n; i++){
		visited[i] = false;
	}
	
	visited[s] = true; 
	
	
	
}

