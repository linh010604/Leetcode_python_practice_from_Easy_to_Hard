class Solution {
public:
    string smallestString(string s) {
        int idx = 0 ;
      
        while (idx < s.size() && s[idx] == 'a') {
            idx++ ;
        }
        if (idx == s.size()) {
            s[idx-1] = 'z' ;
        }
        while (idx < s.size() && s[idx] != 'a'){
            s[idx] = s[idx] - 1 ;
            idx ++ ;
        }
        
        return s ;
    }
};
