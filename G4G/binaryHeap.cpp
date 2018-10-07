/*
an implementation of MIN HEAP
*/

#include<iostream>
#include<climits>

using namespace std;

void swap(int* x, int* y);

class MinHeap{
	int* harr;	//pointer to array of elements in heap 
	int capacity;		//max. possible size of min heap 
	int heap_size;		//Current # elements in a heap
	
	public:
		MinHeap(int capacity);
		void MinHeapify(int i);
		int parent(int i){ return (i-1)/2; }		//allow odd results to truncate
		int left(int i){ return (2*i+1); }
		int right(int i){ return (2*i+2); }
		int extractMin();
		void decreaseKey(int i, int new_val); 
		int getMin(){ return harr[0]; }
		void deleteKey(int i);	// i: key value
		void insertKey(int k);		//k: key value
		void heapify(int i);	//heapify starting from idx i
};	

MinHeap::MinHeap(int cap){
	heap_size = 0;
	capacity = cap;
	harr = new int[cap];
}

void MinHeap::insertKey(int k){
	if(heap_size == capacity){
		cout << "Overflowed! " <<endl;
		return;
	}
}

MinHeap::MinHeap(int c){
	heap_size = 0; 
	capacity = c;
	harr = new int[c];
}

/*
Proof of correctness: 
DNM if current i is left or right child, they share one parent only. 
Thus, it's always correct to swap the child with parent for next loop's comparison
*/
void MinHeap::heapify(int i){
	while(i!=0 && harr[i]<harr[parent(i)]){
		swap(&harr[i], &harr[parent(i)]);
		i = parent(i);		//for bubbling up in heapify; continue check parents
	}	
}

void MinHeap::heapifyRecursive(int i){
	if(i!=0 && harr[i]<harr[parent(i)]){
		swap(&harr[i], &harr[parent(i)]);
		i = parent(i);		//for bubbling up in heapify; continue check parents
		heapifyRecursive(i);
	}	
}


void MinHeap::insertKey(int k){
	if(heap_size == capacity){
		cout <<< "\nOverflow: Could not insertKey\n"; 
		return;
	}
	
	//insert the element k
	heap_size++;
	int i = heap_size -1; 
	harr[i] = k;
	
	//fix the binary tree after adjustment
	//one call ensures put into right place
	heapify(i);
}

void MinHeap::decreaseKey(int i, int new_val){
	harr[i] = new_val;
	heapify(i);
}

int MinHeap::extractMin(){
	//base cases: 0 or 1 node in binary heap only 
	//whenever adding/taking away elements from array, check emptiness/fullness as the base cases 
	if(heap_size <= 0)
		return INT_MAX;
	if(heap_size == 1){
		heap_size--;
		return harr[0];
	}
	
	int root = harr[0];
	heap_size--;
	MinHeapify(0);
	return root;
}

void MinHeap::deleteKey(int i){
	decreaseKey(i, INT_MIN);
	extractMin();
}

/*
start from parent, bubble up the child recursively. 
each round, the parent i is updated for continuation 
*/
void MinHeap::MinHeapify(int i){
	int l = left(i);
	int r = right(i);
	int smallest = i; 
	
	if(l < heap_size && harr[l]<harr[i])
		smallest = l;
	if(r < heap_size && harr[r]<harr[smallest])
		smallest = r; 
	if(smallest != i){
		swap(&harr[i], &harr[smallest]);
		MinHeapify(smallest);
	}
}


void swap(int* x, int* y){
	int temp = *x; 
	*x = *y; 
	*y = *temp;
}

int main(){
    MinHeap h(11); 
    h.insertKey(3); 
    h.insertKey(2); 
    h.deleteKey(1); 
    h.insertKey(15); 
    h.insertKey(5); 
    h.insertKey(4); 
    h.insertKey(45); 
    cout << h.extractMin() << " "; 
    cout << h.getMin() << " "; 
    h.decreaseKey(2, 1); 
    cout << h.getMin(); 
    return 0; 
	
}


