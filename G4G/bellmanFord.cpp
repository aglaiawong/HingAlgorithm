#include <iostream>
#include <climits>
using namespace std; 

class Graph{
	int n;
	int **adjMatrix;
	int *distanceFromSrc; 
	int *parents; 

public:
	//for graph constructions
	Graph(int n);
	void addEdge(int v, int w); 
	
	bool bellmanFord(Graph G, int w, int u);
	void initSingleSource(Graph G, int u); 
	void relax(int u, int v);
	
};

Graph::Graph(int n){
	this->n = n;
	adjMatrix = new int*[n];
	distanceFromSrc = new int[n];
	parents = new int[n];
	
	for(int i=0; i<n; i++)
		adjMatrix[i] = new int[n];
}

void Graph::addEdge(int u, int v, int w){
	adjMatrix[u][v] = w;		//[src][dst]
}

void Graph::initSingleSource(int u){
	
	for(int i=0; i<n; i++){
		distanceFromSrc[i] = INT_MAX;
		parents[i] = -1;		//-1 means no parents yet  
	}
	parents[u] = 0; 
}

void Graph::relax(int u, int v){
	
	int t_distance = distanceFromSrc[u]+adjMatrix[u][v];
	
	if(distanceFromSrc[v]>t_distance){
		distanceFromSrc[v] = t_distance;
		parents[v] = u; 
	}
}

void Graph::bellmanFord(int src){
	initSingleSource(src);
	for(int iter=0; iter<n-1; iter++){	//maximum # iterations allowed in BF
	
		//for each weighted edge exist in the graph 
		for(int i=0; i<n; i++)
			for(int j=0; j<n; j++)
				if(adjMatrix[u][v]!=INT_MAX)	//ensure the weighted edge truly exists in graph 
					relax(u,v);

	}
	
	for(int i=0; i<n; i++)
		for(int j=0; j<n; j++)
			if(adjMatrix[u][v]!=INT_MAX)	//ensure the weighted edge truly exists in graph 
				if(distanceFromSrc[v] > distanceFromSrc[u]+adjMatrix[u][v])
					return false; 
	return true; 
}


