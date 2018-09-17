/*
877. Stone Game
*/

#include <iostream>
#include <vector>
using namespace std;

class Solution {
  public:
  
	int maxElement(vector<int>& piles){
		bool secondChoice = false; 
		bool secIdxFront = false; 	//default back 		
		int firstElement = piles.front();
		int lastElement = piles.back();
		int result = 0; 
		
		if(firstElement == lastElement and size>=4){
			secondChoice = true;
			int secEle = piles[1];
			int secLastEle = piles[size-2];
			
			//if still equal, randomly picked; 
			int secMax = max(secEle, secLastEle);
			if(secMax == secLastEle){
				result = piles.front();
				piles.erase(piles.begin());
			} else {
				result = piles.back();
				piles.erase(piles.end()-1);
			}
		}
		
        int maxElement = max(firstElement, lastElement);

        if(maxElement == firstElement){
          piles.erase(piles.begin());
        } else {
          piles.pop_back(); 
        }

        if(alexTurn){
          alex += maxElement;
          alexTurn = false;
        } else {
          lee += maxElement;
          alexTurn = true;
        }
        
        size -= 1; 
		secondChoice = false; 
	}
  
  
    bool stoneGame(vector<int>& piles) {
      int alex=0;
      int lee=0;
      bool alexTurn = true; 

      int size = piles.size(); 
	  
      while(size){
        int firstElement = piles.front();
        int lastElement = piles.back(); 
		
		if(firstElement == lastElement and size>=4){
			secondChoice = true;
			int secEle = piles[1];
			int secLastEle = piles[size-2];
			
			//if still equal, randomly picked; 
			int secMax = max(secEle, secLastEle);
			if(secMax == secLastEle){
				secIdxFront = true
			} else {
				secIdxFront = false; 
			}
			
		}
		
        int maxElement = max(firstElement, lastElement);

        if(maxElement == firstElement){
          piles.erase(piles.begin());
        } else {
          piles.pop_back(); 
        }

        if(alexTurn){
          alex += maxElement;
          alexTurn = false;
        } else {
          lee += maxElement;
          alexTurn = true;
        }
        
        size -= 1; 
		secondChoice = false; 
      }
      
      cout << "alex: " << alex <<endl; 
      cout << "lee: " << lee << endl; 

      if(alex>lee) return true;
      else return false;
    
    }
};


  

int main(){
  Solution s;
  vector<int> a;
  int arr[] = {3,7,2,3}; 
  for(int i:arr){
    a.push_back(i);
  }
  
  s.stoneGame(a);
}