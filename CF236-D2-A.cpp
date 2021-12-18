#include <bits/stdc++.h>

using namespace std;

int main() {

    string s; cin >> s;
    set<char> hs; 
    for(char c : s) {
        hs.insert(c);
    }

    if(hs.size() % 2 == 0) {
        cout << "CHAT WITH HER!" << endl;
    } else {
        cout << "IGNORE HIM!" << endl;
    }
}