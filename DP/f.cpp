#include <iostream>
#include <vector>
#include <cstdlib>  

using namespace std;

template<class T> inline bool chmax(T& a, T b){
    if (a < b){
        a = b;
        return 1;
    }
    return 0;
}
template<class T> inline bool chmin(T& a, T b){
    if(a > b){
        a = b;
        return 1;
    }
    return 0;
}

string s, t;

int dp[3100][3100] = {0};

int main(){
    cin >> s >> t;

    for (int i = 0; i < s.size(); i++){
        for (int j = 0; j < t.size(); j++){
            if (s[i] == t[j]){
                chmax(dp[i+1][j+1], dp[i][j] + 1);
            }
            chmax(dp[i+1][j+1], dp[i+1][j]);
            chmax(dp[i+1][j+1], dp[i][j+1]);
        }
    }
    // ここまででLCSは解けた
    string res = "";
    int i = (int)s.size(), j = (int)t.size();
    while (i > 0 && j > 0){
        if (dp[i][j] == dp[i-1][j]){
            --i;
        }

        else if (dp[i][j] == do[i][j-1]) {
            --j;
        }

        else {
            res = s[i-1] + res;
            --i;
            --j;
        }
    }
    cout << res << endl;
}