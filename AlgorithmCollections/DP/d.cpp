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

int N;
long long W, w[110], v[110];
long long dp[110][100100] = {0};

int main(){
    cin >> N >> W;
    for (int i = 0; i < N; i++) cin >> w[i] >> v[i];

    // DP loop
    for (int i = 0; i < N; i++){
        for(int sum_w = 0; sum_w <= W; sum_w++){

            // i番目の品物を選ぶ場合
            // i番目のwがsum_wよりも大きくなければ選べます
            if (sum_w - w[i] >= 0){
                chmax (dp[i+1][sum_w], dp[i][sum_w - w[i]] + v[i]);
            }

            // i番目の品物を選ばない場合
            // 初期値0なので，大きいものには更新されるよ
            chmax(dp[i+1][sum_w], dp[i][sum_w]);
            // さっきの総利得と同じ
        }
    }
    cout << dp[N][W] << endl;
}






