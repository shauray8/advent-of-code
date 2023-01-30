#pragma GCC optimize ("02")
#include <bits/stdc++.h>

using namespace std;

int main(){
	long long a;
	scanf("%lli",&a);
	printf("%lli ",a);
	while(a > 1){
		if(a % 2 == 0){
			a /= 2;
		}	
		else{
			a = a*3 + 1;
		}
		printf("%lli ",a);

	}
	
}
