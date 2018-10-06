#include<iostream>
#include<queue>
using namespace std;

class Graph{
	int n;
	queue<int>* adj;	//pointer to an array of queues, one queue per node
public:
	Graph(int n);
	void addEdge(int v, int w);		//node to add & weight
	void BFS(int s);	//s as starting node 
};

Graph::Graph(int n){
	this->n = n;
	adj = new queue<int>[n];	//one extendible queue per node
}

void Graph::addEdge(int v, int w){
	adj[v].push(w);		//add weight to a node v's adj list==add an edge
}

void Graph::BFS(int s){
	
	//resultant BFS ordering starting from node s
	queue<int>::result;		
	
	//node initializations for traversal
	bool *visited = new bool[n];	//used later for enqueing to unvistied nodes in bfs_q
	for(int i=0;i<n;i++){
		visited[i] = false;
	}

	//a queue for BFS
	queue<int>bfs_q; 
	queue<int>::iterator it;
	
	//start traversal: 
	bfs_q.push(s);
	visited[s] = true; 
	
	while(!bfs_q.empty()){
		//get and pop the parent
		int p = bfs_q.front();		//save parent before pop
		result.push(p);	
		bfs_q.pop();	//pop does not return anything; Thus, used with front() 
		
		// traverse its children : only traverse the queue for that parent node only.
		for(it=adj[p].begin(); it!=adj[p].end(); it++){		//look for child in adjacency list 
			if(!vistied[*it]){
				visited[*it] = true; 
				bfs_q.push(*it);		//this ensures the outter while loop keeps running when the queue is not empty. 
			}
		}
	}
	
}