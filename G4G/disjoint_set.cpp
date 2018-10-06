/*
Disjoint-set data structures
- keep track of a set of elements partions
- near O(n) for: add new sets, merge sets, determine if an element's in a set. 
- used in Kruskal for finding MST
- possible operations: union-find
*/

#include <iostream>
using namespace std; 

/*
The only difference between a struct and class in C++ is 
the default accessibility of member variables and methods. 
In a struct they are public; in a class they are private.
*/

//reference: http://www.techiedelight.com/graph-implementation-c-without-using-stl/

struct Node {
	int val;
	Node* next; 
}

struct Edge{
	int src, dest;
}

class Graph{
	//a private method to get append new node at the head of adjacey list
	Node* getAdjListNode(int dest, Node* head){
		Node* newNode = new Node();
		newNode->val = dest;
		newNode->next = head; 
		return newNode; 
	}
	
	int N; //number of nodes in graph
	
public:
	Node** head; 		//a pointer to pointer
	Graph(Edge edges[], int n, int N){
		head = new Node*[N](); 	//a pointer to an array of pointers
		this->N = N; 
		
		for(int i =0; i<N;i++)
			head[i] = NULL; 
		
		//for directed graph
		for(int i=0; i<n; i++){
			int src = edges[i].src;
			int dest = edges[i].dest; 
			
			Node* newNode = getAdjListNode(dest, head[src]); 
			head[src] = newNode; 
			
			//uncomment for undirected graph
			/*
			newNode = getAdjListNode(src, head[dest]);
			head[dest] = newNode; 
			*/
		}
	}
		
	~Graph(){
		for(int i=0; i<N; i++)
			delete[] head[i];
		
		delete[] head; 
 	}
	
};
	
	
	
	
	
	
	
	
	
	
	
	
	
}