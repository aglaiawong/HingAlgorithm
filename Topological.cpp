/*
	Topo-sort assumed runs on directed graph
	a DAG returns at least 1 topological ordering
	else no topological order and cycle detected;
	
	Also, DAG usually no symmetric adjacency list/matrix;
	Thus, no spatial/time optimalization possible
*/


//n: total # of nodes 

bool edge[n][n];		//edge matrix
int incoming[n];		//# incoming edges for each node
queue<int> topo_order;		//hold the resulted ordering 

void topological_ordering(){
	
/*evaluate the # of incoming edges, i.e. in-degree, for each node */	

	for(int i=0; i<n; i++) incoming[i]=0;		//initialization: prepare for addition 
	
	for(int i=0; i<n;i++){		//scan along one axis once, each node as ancestor 
		for(int j=0; j<n; j++){		//each node as predeceser 
			if(edge[i][j]) incoming[j]++;		//exit(i,j): update inDeg(predeceser)
		}
	}

/*Build topo ordering*/	

	for(int i=0; i<n;i++){		//find a node s with in-deg=0; 
								//looped n times to push all nodes into topo_order
		int s = 0; 
		while(s<n && incoming[s]!=0) s++;	//find any node with inDeg=0
		if(s==n) break;		//for all v, inDeg(v)>0, cycle detected.
		incoming[s] = -1;	//else, exist at least 1 node with inDeg=0
		topo_order.push(s);
		
		for(int k=0;k<n;k++)	//eliminate all outgoing edges from s, where inDeg(s)=0
			if(edge[s][k])
				incoming[k]--;
	}
	
	if(topo_order.size()!=n)		//this is where the break above returns to 
		cout << "Cycle detected!" << endl;  
}

/* Footnote
- in topo sort, exactly which edges go to certain predeceser does not really matter;
- only the inDeg(v) matters; Thus need not record where the incoming edge's from
*/


