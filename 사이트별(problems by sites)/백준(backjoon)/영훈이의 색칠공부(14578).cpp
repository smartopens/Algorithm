#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#define MOD 1000000007

using namespace std;

typedef long long ll;

// 식이 계산되면서 int형을 초과할 수 있다.
// 고로 long long을 사용한다.
ll fac[100002];
ll dp[100002];

// 빨간색 블록이 정해지는 경우 : n*(n-1)*(n-2)*...
// 한 블록이 고정되고 다른 블록의 경우를 생각해야 한다.
// 이 때 교란 수열이 사용된다. 수열식: (n-1)*(dp[n-2] + dp[n-1])
// 총 점화식: n!*((n-1)*(dp[n-2] + dp[n-1])))

int main() {
    ll n, f_n;

    cin >> n;
    f_n = 1;

    // 팩토리얼 수를 저장한다.
    for (ll i = 1; i < n + 1; i++)
    {
        f_n = (f_n*i)%MOD;
        fac[i] = f_n;
    }

    // 수열식을 저장한다.
    dp[0] = 1, dp[1] = 0;
    for (ll i = 2; i < n + 1; i++)
    {
        dp[i] = (i-1)*(dp[i - 1] + dp[i - 2])%MOD;
    }

    // 최종 경우의 수를 구한다.
    cout << (fac[n]*dp[n])%MOD << endl;
    return 0;
}
