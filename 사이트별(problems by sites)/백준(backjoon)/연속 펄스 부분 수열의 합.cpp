#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int n;

long long puls1_dp[500002];
long long puls2_dp[500002];

long long max_sn;

long long solution(vector<int> sequence) {
    max_sn = 0;
    n = sequence.size();

    for (int pv = 0; pv < n; pv++)
    {
        if (pv % 2 == 0)
        {
            puls1_dp[pv] = sequence[pv] * -1;
            puls2_dp[pv] = sequence[pv];
        }
        else
        {
            puls1_dp[pv] = sequence[pv];
            puls2_dp[pv] = sequence[pv] * -1;
        }
    }

    max_sn = max(puls1_dp[0], puls2_dp[0]);
    for (int pv = 1; pv < n; pv++)
    {
        // 연속된 합의 경우가 지속될 경우
        if (puls1_dp[pv - 1] + puls1_dp[pv] >= puls1_dp[pv])
        {
            puls1_dp[pv] = puls1_dp[pv - 1] + puls1_dp[pv];
        }

        // 연속된 합의 경우가 지속될 경우
        if (puls2_dp[pv - 1] + puls2_dp[pv] >= puls2_dp[pv])
        {
            puls2_dp[pv] = puls2_dp[pv - 1] + puls2_dp[pv];
        }

        max_sn = max({ max_sn,puls1_dp[pv], puls2_dp[pv] });
    }

    return max_sn;
}