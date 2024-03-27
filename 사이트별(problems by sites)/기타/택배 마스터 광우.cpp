#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int n, m;
int k;

int rail_w[12];
int rail_o[12];
vector<int> rail_o2;
int vi[12];

int min_w;

void g_work(int a)
{
    // 일을 수행하는 경우 고려하기
    if (a > n - 1)
    {
        int now_k = k;
        int ws = 0;
        int now_w = 0;
        int to_w;
        int sum_w = 0;
        //for (int s = 0; s < n; s++)
        //{
        //    cout << rail_o[s] << " ";
        //}
        //cout << endl;

        while (true)
        {
            to_w = rail_w[rail_o[ws]];

            // 택배에 무게를 담을 수 있는 경우
            if (now_w + to_w <= m)
            {
                now_w += to_w;
                sum_w += to_w;

                if (now_w == m)
                {
                    now_w = 0;
                    now_k -= 1;
                }
                ws = (ws + 1) % n;
            }
            else
            {
                now_w = 0;
                now_k -= 1;
            }

            if (now_k <= 0) break;
        }

        if (min_w > sum_w)
        {
            min_w = sum_w;
        }
        return;
    }
    for (int to_v = 0; to_v < n; to_v++)
    {
        if (vi[to_v] != 0) continue;
        vi[to_v] = 1;

        // 레일 순서 담기
        rail_o[a] = to_v;
        g_work(a + 1);
        vi[to_v] = 0;

    }
}

int main(int argc, char** argv)
{
    cin >> n >> m >> k;
    for (int i = 0; i < n; i++)
    {
        cin >> rail_w[i];
    }

    for (int i = 0; i < n; i++)
    {
        rail_o[i] = i;
    }

    min_w = 21e8;
    do {

        int now_k = k;
        int ws = 0;
        int now_w = 0;
        int to_w;
        int sum_w = 0;
        //for (int s = 0; s < n; s++)
        //{
        //    cout << rail_o[s] << " ";
        //}
        //cout << endl;

        while (true)
        {
            to_w = rail_w[rail_o[ws]];

            // 택배에 무게를 담을 수 있는 경우
            if (now_w + to_w <= m)
            {
                now_w += to_w;
                sum_w += to_w;

                if (now_w == m)
                {
                    now_w = 0;
                    now_k -= 1;
                }
                ws = (ws + 1) % n;
            }
            else
            {
                now_w = 0;
                now_k -= 1;
            }

            if (now_k <= 0) break;
        }

        if (min_w > sum_w)
        {
            min_w = sum_w;
        }

    } while (next_permutation(rail_o, rail_o + n));
    //g_work(0);
    cout << min_w << endl;
    return 0;
}