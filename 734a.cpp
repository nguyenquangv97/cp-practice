#include <bits/stdc++.h>

using namespace std;

int main(){
    int n;
    int a = 0, d = 0;
    cin >> n;
    string x;
    cin >> x;
    for(int i = 0; i < n; i++){
  
        if(x[i] == 'A'){
            a++;
        } else {
            d++;
        }
    }
    if(a > d) cout << "Anton" << '\n';
    else if(d > a) cout << "Danik" << '\n';
    else cout << "Friendship" << '\n';
}