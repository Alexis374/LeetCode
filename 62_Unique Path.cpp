/*
f(m,n) = f(m-1,n)+f(m,n-1)
f(m,1)=f(1,n)=1
构造二维数组即可解决
*/

class Solution {
public:
    int uniquePaths(int m, int n) {
        int table[m][n];
        if(m==1||n==1)return 1;
        for(int i=0;i<m;i++)table[i][0]=1;
        for(int i=0;i<n;i++)table[0][i]=1;
        table[0][0]=0;
        for(int i=1;i<m;i++){
            for(int j=1;j<n;j++){
                table[i][j] = table[i-1][j]+table[i][j-1];
            }
        }
        return table[m-1][n-1];
    }
};