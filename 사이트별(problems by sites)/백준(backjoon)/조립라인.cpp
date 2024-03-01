#include<iostream>
#include<algorithm>

using namespace std;

int n;

int a_co[1002];
int b_co[1002];

int a_to[1002];
int b_to[1002];

int a_dp[1002];
int b_dp[1002];

int min_tm;

int main(int argc, char** argv)
{
    cin >> n;
    int a_v, b_v, b_to_f, a_to_f;
    for (int jv = 1; jv < n; jv++)
    {
        cin >> a_v >> b_v >> b_to_f >> a_to_f;

        a_co[jv] = a_v;
        b_co[jv] = b_v;
        b_to[jv + 1] = b_to_f;
        a_to[jv + 1] = a_to_f;
    }

    cin >> a_co[n];
    cin >> b_co[n];

    min_tm = 0;
    bool on_a = false;
    bool on_b = false;

    int to_a_co1 = a_co[1];
    int to_a_co2 = a_co[1];
    int to_b_co1 = b_co[1];
    int to_b_co2 = b_co[1];

    a_dp[1] = a_co[1];
    b_dp[1] = b_co[1];
    int to_min_tm = 21e8;

    if (n == 1)
    {
        min_tm = min(a_dp[1], b_dp[1]);
    }
    else if (n > 1)
    {
        for (int to_v = 2; to_v < n + 1; to_v++)
        {
            // A 작업 시간 고려
            a_dp[to_v] = min(a_dp[to_v - 1] + a_co[to_v], b_dp[to_v - 1] + a_to[to_v] + a_co[to_v]);

            // B 작업 시간 고려
            b_dp[to_v] = min(b_dp[to_v - 1] + b_co[to_v], a_dp[to_v - 1] + b_to[to_v] + b_co[to_v]);
        }
    }

    min_tm = min(a_dp[n], b_dp[n]);
    cout << min_tm << endl;
    return 0;
}