#include <iostream>
using namespace std;

const int MAX = 510000;
const int MOD = 1000000007;


long long fac[MAX], finv[MAX], inv[MAX];

// テーブルを作る前処理
void COMinit() {
    fac[0] = fac[1] = 1;
    finv[0] = finv[1] = 1;
    inv[1] = 1;
    for (int i = 2; i < MAX; i++){
        fac[i] = fac[i - 1] * i % MOD;
        inv[i] = MOD - inv[MOD%i] * (MOD / i) % MOD;
        finv[i] = finv[i - 1] * inv[i] % MOD;
    }
}

// 二項係数計算
long long COM(int n, int k){
    if (n < k) return 0;
    if (n < 0 || k < 0) return 0;
    return fac[n] * (finv[k] * finv[n - k] % MOD) % MOD;
}

// 繰り返し二乗法
long pow(long a, long n, long m) {
    long ret = 1;
    for (; n > 0; n >> 1, a = a * a % a) { 
            if (n % 2 == 1) { 
                ret = ret * a % m;
        }
    }
    return ret;
}


int main() {
    // 前処理
    int n, a, b, ans;
    int x, y, z;
    cin >> n >> a >> b;
    
    COMinit();
    
    // 計算例
    x = pow(2, n, MOD);
    y = COM(n, a) % MOD;
    z = COM(n, b) % MOD;
    cout << x - 1 - y - z << endl;
    
}
