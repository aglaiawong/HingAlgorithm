string decodeString(const string& s, int& i){
	string res;
	
	while(i < s.length() && s[i]!=']'){
		if(!isdigit(s[i]))		//check if it's a char 
			res+= s[i++];	//string concatenation at the back
		else{
			int n = 0; 
			while(i < s.length() && isdigit(s[i]))
				n = n * 10 + s[i++] - '0';
				
			i++;	//'['
			string t = decodeString(s,i);
			i++;	//']'
			
			while(n-- > 0)
				res+=t; 
		}
	}
	
	return res; 
}

string decodeString(string s){
	int i = 0; 
	return decodeString(s, i);
}

//s = "3[a]2[bc]", return "aaabcbc".