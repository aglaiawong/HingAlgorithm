#include<iostream>
#include<queue>
using namespace std;

class Graph{
	int n;
	queue<int>* adj;	//pointer to an array of queues, one queue per node
	queue<int> result; 	//hold the DFS ordering
public:
	Graph(int n);
	void addEdge(int v, int w);		//node to add & weight
	void DFS(int s);	//s as starting node 
	void DFS_Main(int s);
};

Graph::Graph(int n){
	this->n = n;
	adj = new queue<int>[n];	//one extendible queue per node
}

void Graph::addEdge(int v, int w){
	adj[v].push(w);		//add weight to a node v's adj list==add an edge
}

/*DFS*/
void Graph::DFS(int v, bool visited[]){
	visited[v] = true;		//start from parent node v, traverse downwards
	result.push(v);
	
	queue<int>::iterator it;
	for(it=adj[v].begin();it!=adj[v].begin();it++){
		if(!visited[*it]){
			DFS(*it, visited);	//when returned from recursive frame, then examine another child of current parent node
			//No confuse: visited nodes still in adjacey list and is not indeed removed
			// thus, 'removal' is conceptual.
		}
	}
}

void Graph::DFS_Main(int s){	//pick a node to run DFS/BFS
	
	//initialize visit array, be amended in subroutine
	bool *visited = new bool[n];
	for(int i=0;i<n;i++){
		visited[i] = false; 
	}
	DFS(s, visited);
}

/*DFS*/