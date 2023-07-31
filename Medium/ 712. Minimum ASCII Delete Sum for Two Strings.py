class Solution {
public:
    int minimumDeleteSum(string s1, string s2) {

        int m = s1.size() , n = s2.size() , s1sum = 0 , s2sum = 0;

        int dp[m+2][n+2] ;

        for (int i = 0 ; i <= m ; i ++) {
            s1sum += int(s1[i]) ;
            dp[i][0] = 0 ;
        }
        for(int  j = 0 ; j <= n ; j ++)  {
            s2sum += int(s2[j]) ;
            dp[0][j] = 0 ;
        }
    
        for (int i = 1 ; i <= m ; i ++) {
            for(int  j = 1 ; j <= n ; j ++){
                if (s1[i-1] == s2[j-1]) {
                    dp[i][j] = dp[i-1][j-1] + int(s1[i-1]);
                }
                else {
                    dp[i][j] = max(dp[i][j-1] , dp[i-1][j]) ;
                }
            }
        }
        return  s1sum + s2sum - 2*dp[m][n] ;
    }
};
