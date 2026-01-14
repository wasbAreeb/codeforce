
// A. Reconnaissance Problem
// Brute force method

#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

int main(){
    int n, d;
    int ways = 0;

    cin >> n >> d;
    
    vector<int> soldier(n);
    for(int i = 0; i < n; i++){
        cin >> soldier[i];
    }

    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            if (i == j){
                continue;
            }
            if(abs(soldier[i] - soldier[j]) <= d){
                ways += 1;
            }
        }
    }

    cout << ways;

    return 0;
}