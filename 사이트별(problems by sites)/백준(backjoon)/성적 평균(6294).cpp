#include<iostream>
#include <cmath>

using namespace std;

int n, k;
double st_sco[1000002];
double s_sum[1000002];

double sco_mean;

int main(int argc, char** argv)
{
    cout << fixed;
    cout.precision(2);

    cin >> n >> k;
    for (int i = 1; i < n + 1; i++)
    {
        cin >> st_sco[i];
        s_sum[i] = st_sco[i];
    }

    for (int sv = 2; sv < n + 1; sv++)
    {
        s_sum[sv] += s_sum[sv - 1];
    }

    int ka, kb;
    for (int i = 0; i < k; i++)
    {
        cin >> ka >> kb;
        sco_mean = 0;
        sco_mean = (s_sum[kb] - s_sum[ka - 1]) / (kb - ka + 1);
        cout << sco_mean << "\n";
    }

    return 0;
}