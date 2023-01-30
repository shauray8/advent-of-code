#pragma GCC optimize ("02")
#include <bits/stdc++.h>

using namespace std;

int main(){
	long long n;
	vector<long long> aa;
	cin >> n;
	for(int i=0; i < n-1; ++i){
		int a = 0;
		cin >> a;
		aa.push_back(a);
	}

	sort(aa.begin(), aa.end());
	for(int i=1; i<n+1; i++){
		if(i == aa[i-1]){
			;
		}
		else{
			cout << i;
			break;
		}
	}
}
