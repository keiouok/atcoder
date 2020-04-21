#include <bits/stdc++.h>
#define rep(i, n) for (int i = 0; i < (n); ++i)
using namespace std;
using ll = long long;
using P = pair<int, int>;

int n;

void dfs(string s, char mx) {
    if (s.size() == n) {
        cout << s << endl;
        return;
    }
    for (char c = 'a'; c <= mx + 1; c++) {
        string t = s;
        t += c;
        dfs(t, max(mx, c));
    }
}

int main() { 
    cin >> n;
    // cout << 'a'-1 << endl;
    dfs("", 'a'-1);
    return 0;
}
