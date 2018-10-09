#include<iostream>
#include<queue>

using namespace std;

class Graph{
	int size;
	queue<int>* adj;
	queue<int>* edges; 

public:
	Graph(int n);
	void addEdge(int src, int des);
	void prims(int s);
}

Graph::Graph(int n){
	size = n;
	adj = new queue<int>[n];	
}

void Graph::addEdge(int src, int des){
	adj[src].push(des);
}

void Graph::prims(int s){
	bool* visited = new bool[n];
	for(int i=0; i<n; i++){
		visited[i] = false;
	}
	
	visited[s] = true; 
	
	
	
}

