#include <bits/stdc++.h>
#define INF 0x3f3f3f3f
using namespace std;

typedef pair<int,int> iPair;

class Graph{
    int V;
    //adj list with weights
    //list<int> *adj; without weights 
    list <pair<int,int> > *adj;

public:
	Graph(int V);
	void addEdge(int u,int v,int w);
	void primMST();
};
Graph::Graph(int V){
    this->V = V;
    adj = new list<iPair>[this->V];
}
void Graph::addEdge(int u,int v,int w){
    //Para lista de adyacencia es (label,weight)
    adj[u].push_back(make_pair(v,w));
    adj[v].push_back(make_pair(u,w));
}
void Graph::primMST(){
    //Priority Queue (PQ) es (weight,label)
    //Implementa un MIN HEAP de iPair
    priority_queue<iPair,vector<iPair>,greater<iPair> > pq;		//bubble up those with smaller weights

    int src = 0;				//Prim's stands for pick a node; Diff src gv diff MST. 

    vector<int> key(V,INF);		//init all nodes to INF, i.e. non-visited; 
    vector<int> parent(V,-1);	//for printing MST only.
    vector<bool> inMST(V,false);	// subset of MST 

    pq.push(make_pair(0,src));		//push first node into pq with least weights; 
									// so as to be popped up as the first node under the greater<>; 
    key[src] = 0;					// if key[node]!=INF --> i.e. it's visited

    while(!pq.empty()){
        int u = pq.top().second;	//get the node (label); use this parent node within each loop in while
        pq.pop();

        inMST[u] = true;
        list<pair<int,int> >::iterator it;
        for(it = adj[u].begin();it!=adj[u].end();it++){	//for each of child of u 
            int v = (*it).first;
            int weight = (*it).second;

            if(!inMST[v] && key[v] > weight){	//find the child with least weight under u
				// key[v] > weight iff the node has been unvisited before
				//key[v] check if a node is visited or not. 
				//actually key[] can be turned into a boolean array of visited[]; 
				//cz key[v] is not enqueued anyway; INF or False make no difference=
                key[v] = weight;		//compare among child of u to find the least weight 
                pq.push(make_pair(key[v],v));		//contain the weight and the node of children enqueued
                parent[v] = u;
            }
        }
    }
    for(int i=1;i<V;i++){
        cout << parent[i] << " - "  << i << endl;
    }
}
int main(){
    int V = 5;
    Graph g(V);
    g.addEdge(0,1,3);
    g.addEdge(0,2,2);
    g.addEdge(1,2,1);
    g.addEdge(1,3,4);
    g.addEdge(2,4,1);
    g.addEdge(3,4,2);
    g.primMST();
    return 0;
}