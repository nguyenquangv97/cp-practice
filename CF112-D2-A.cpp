#include <bits/stdc++.h>
using namespace std;

int main() {
    string a; cin >> a;
    string b; cin >> b;
    int i = 0;
    int res = 0;
    while(i < a.length()) {
        if(tolower(a[i]) > tolower(b[i])){
            res = 1;
            break;
        }
        else if (tolower(a[i]) < tolower(b[i])) {
            res = -1;
            break;
        }
        else res = 0;
        i++;
    }
    cout << res << endl;
 

}