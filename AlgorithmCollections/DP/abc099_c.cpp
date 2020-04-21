# include<iostream>
# include<cstdlib>
using namespace std;
int main(){
    int N;
    cin >> N;
    int res = N;
    for(int i = 0; i <= N; i++){
        int c = 0;
        int t = i;
        while(t > 0){
            c += t % 6;
            t /= 6;
        }
        t = N - i;
        while(t > 0){
            c += t % 9;
            t /= 9;
        }
        if(res > c){
            res = c;
            // 最悪1円N回払えばいい．resの初期値はN.
        }
    }
    cout << res << endl;
    
}