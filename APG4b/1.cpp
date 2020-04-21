#include <bits/stdc++.h>
#include <algorithm>
#define rep(i, n) for (int i = 0; i < (n); ++i)
#define _GLIBCXX_DEBUG
using namespace std;
using ll = long long;
using P = pair<int, int>;

void change(int &n, vector<int> &vec) {
    n = 1;
    vec.at(0) = 1;
    return;
}

int sum(int n) {
    if (n == 0) {
        return 0;
    }
    return n + sum(n - 1);
}


int main() { 

    int n = 5;
    // vector<int> math(n, 5);
    // vector<int> en(n, 5);

    // for (int i = 0; i < n; i++) {
    //     cout << math.at(i) + en.at(i) << endl;
    // }
    vector<int> vec = { 1, 3, 5 };
    vec.push_back(10);
    vec.pop_back();

    for (int i = 0; i < vec.size(); i++) {
        cout << vec[i] << endl;
    }

    // vector<int> vec(3, 10);
    // vec = vector<int>(100, 2);
    // cout << vec[99] << endl;

    vec = {1, 5, 3};
    reverse(vec.begin(), vec.end());

    for (int i = 0; i < vec.size(); i++) {
        cout << vec.at(i) << endl;
    }
    sort(vec.begin(), vec.end());
    reverse(vec.begin(), vec.end());

    // int x = 5;
    vector<int> v  = {10, 10, 10};
    // change(x, v);
    // cout << x << endl;
    // cout << v.at(0) << endl;
    for (int x : v) {
        cout << x << endl;
    }
    string str = "hello";
    for (char c : str) {
        if (c == 'l') {
            c = 'L';
        }
        cout << c;
    }
    cout << endl;

    vector<vector<int>> data = {
        {7, 4, 0, 8},
        {2, 0, 3, 5},
        {6, 1, 7, 0},
    };
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 4; j++) {
            // cin >> data.at(i).at(j);
            cin >> data[i][j];
        }
    }
    int count = 0;
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            if (data[i][j] == 0) count++;
        }
    }
    cout << count << endl;
    vector<vector<int>> data_2(3, vector<int>(4));
    int h = data_2.size();
    int w = data_2.at(0).size();
    w = data[0].size();
    vector<vector<int>> data3(3);
    data[0].push_back(1);
    data[0].push_back(1);
    data[0].push_back(1);
    data[1].push_back(1);
    data[1].push_back(1);
    data[1].push_back(1);
    data[2].push_back(1);
    data[2].push_back(1);
    data[2].push_back(1);
    // for (int i = 0; i < data3.size(); i++) {
    //     data[i]
    // }
    vector<vector<vector<int>>> dim3(3,vector<vector<int>>(4, vector<int>(5, 0)));
    dim3.at(0).size();
    dim3.at(0).at(0).size();    
    
}

