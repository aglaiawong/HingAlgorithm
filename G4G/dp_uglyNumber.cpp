/* Ugly number@G4G: https://www.geeksforgeeks.org/ugly-numbers/
Find the nth Ugly number.
- i.e. define ugly number: Ugly numbers are numbers whose only prime factors are 2, 3 or 5.
- i.e. ensure no other prime factor. <-- how to achieve this? 
- check the result of division, if even, let it go;
  otherwise, i.e. if odd, recursively divide into base case and see if the result belongs to {2,3,5}
  
Ugly numbers are numbers whose only prime factors are 2, 3 or 5. The sequence 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, … shows the first 11 ugly numbers. By convention, 1 is included.

Given a number n, the task is to find n’th Ugly number. 
  
  
i.e. 'only prime number': since all even factor divisible by 2, we only left with prime factors to determine. 

*/

/* recursive formulation
	time complexity: O(n)
	space complexity: O(1)
*/
int maxDivide(int a, int b){
	while(a%b==0)
		a = a/b;
	return a; 
}

int isUgly(int no){
	no = maxDivide(no, 2);
	no = maxDivide(no, 3);
	no = maxDivide(no, 5);
	
	return (no == 1)? 1:0;
}

int getNthUglyNo(int n){
	int i=1; 	//list of ugly number starts from one
	int count = 1;
	
	while(n>count){		//since need to find the nth ugly number
		i++;		//form ugly number list one-by-one
		if(isUgly(i))
			count++;
	}
	return i; 
}


/*
dp formulation by tabulation
because every number can only be divided by 2, 3, 5, one way to look at the sequence is to split the sequence to three groups as below:
     (1) 1×2, 2×2, 3×2, 4×2, 5×2, …
     (2) 1×3, 2×3, 3×3, 4×3, 5×3, …
     (3) 1×5, 2×5, 3×5, 4×5, 5×5, …
*/

# include<bits/stdc++.h>
int getNthUglyNo(int n){
	int ugly[n];
	int i2 = 0, i3 = 0, i5 = 0;		//indices for current 
	int next_multiple_of_2 = 2;
	int next_multiple_of_3 = 3;
	int next_multiple_of_5 = 5;
	int next_ugly_no = 1; 
	
	ugly[0] = 1;		//Given in Q
	for(int i:n){		//until the nth ugly number found  
		next_ugly_no = min(next_multiple_of_2, min(next_multiple_of_3,next_multiple_of_5));		//the key
		ugly[i] = next_ugly_no;
		
		if(next_ugly_no == next_multiple_of_2){
			i2 = i2+1;
			next_multiple_of_2 = ugly[i2]*2;	//just update for next round 
		}
		
		if(next_ugly_no == next_multiple_of_3){
			i3 = i3+1;
			next_multiple_of_2 = ugly[i3]*3;
		}
		
		if(next_ugly_no == next_multiple_of_5){
			i5 = i5+1;
			next_multiple_of_2 = ugly[i5]*3;
		}		
	}
	return next_ugly_no;
}













































