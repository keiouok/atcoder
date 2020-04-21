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

const long long INF = 1LL << 60;
const int MAX_N = 110;
const int MAX_V = 100100;

int N;
long long W, w[110], v[110];
// long long dp[110][100100] = {0};
long long dp[MAX_N][MAX_V];

int main(){
    cin >> N >> W;
    for (int i = 0; i < N; i++) cin >> w[i] >> v[i];

    for (int i = 0; i < MAX_N; i++){
        for (int j = 0; j < MAX_V; j++){
            dp[i][j] = INF;
        }
    }

    dp[0][0] = 0;

    for (int i = 0; i < N; i++) {
        for (int sum_v = 0; sum_v < MAX_V; sum_v++){
            // i番目の品物を選ぶとき
            if (sum_v - v[i] >= 0) {
                chmin(dp[i+1][sum_v], dp[i][sum_v - v[i]] + w[i]);
            }
            // i番目の品物を選ばないとき
            chmin(dp[i+1][sum_v], dp[i][sum_v]);
        }
    }

    long long res = 0;
    for (int sum_v = 0; sum_v< MAX_V; sum_v++) {
        if (dp[N][sum_v] <= W) res = sum_v;
    }
    cout << res << endl;
}



