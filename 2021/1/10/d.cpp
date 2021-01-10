#include <bits/stdc++.h>
using namespace std;
#include <atcoder/all>
using namespace atcoder;
#define rep(i, n) for (int i = 0; i < (n); ++i)
using ll = long long;
using P = pair<int, int>;

int main(){
    int n, C;
    cin >> n >> C;
    map<int, ll> events;
    rep(i, n){
        int a, b, c;
        cin >> a >> b >> c;
        events[a] += c;
        events[b+1] -= c;
    }
}