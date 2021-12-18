#include <bits/stdc++.h>

using namespace std;

int main(){
    int l, b;
    int year = 0;
    cin >> l >> b;
    while(l <= b) {
        l *= 3;
        b *= 2;
        year += 1;
    }
    cout << year;
}