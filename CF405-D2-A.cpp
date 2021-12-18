#include <bits/stdc++.h>

using namespace std;

int main(){
    int col; cin >> col;
    int a[col -1];
    for(int i = 0; i < col; i++){
        cin >> a[i];
    }
    sort(a, a + col);

    for(int i = 0; i < col; i++){
        cout << a[i] << ' ';
    }

}