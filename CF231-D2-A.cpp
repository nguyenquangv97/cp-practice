#include <bits/stdc++.h>

using namespace std;

int main(){
    int n, ans = 0;
    cin >> n;
    int x,y,z;
    for(int i = 0; i < n; i++) {
        cin >> x >> y >> z;
        if(x + y + z >= 2) {
            ans += 1;
        }
    }
    cout << ans << '\n';
}