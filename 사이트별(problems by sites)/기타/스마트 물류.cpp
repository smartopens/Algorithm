#include <iostream>
#include <string>

using namespace std;

int n, k;
char kd_center[20002];
int r_pick[20002];

int on_rn;

int main(int argc, char** argv)
{
    cin >> n >> k;
    string in_kd;
    cin >> in_kd;
    for (int i = 0; i < in_kd.length(); i++)
    {
        kd_center[i] = in_kd[i];
    }

    on_rn = 0;
    for (int rv = 0; rv < n; rv++)
    {
        if (kd_center[rv] == 'P')
        {
            // 부품 집기
            for (int s = rv - k; s < rv + k + 1; s++)
            {
                if (s < 0 || s > n - 1) continue;
                if (kd_center[s] != 'H') continue;
                if (r_pick[s] != 0) continue;

                r_pick[s] = 1;
                on_rn += 1;
                break;
            }
        }
    }

    cout << on_rn << endl;
    return 0;
}