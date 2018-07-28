class Solution {
public:
    int getImportance(vector<Employee*> employees, int id) {
                     //id,index pair
        unordered_map<int,int > um;
        int n=employees.size();
        for(int i=0;i<n;i++)
            um[employees[i]->id]=i;		//map id to index 
        queue<int> Q;
        Q.push(id);
        int ans=0;
        while(Q.empty()!=true){
            id=Q.front();
            Q.pop();
            ans += employees[um[id]]->importance;
            int n=employees[um[id]]->subordinates.size();
            
            for(int i=0;i<n;i++)
                Q.push(employees[um[id]]->subordinates[i]);
        }
        return ans;
    }
};