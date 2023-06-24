#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <vector>
#include <cstring>

using namespace std;

int t;
int peo_p[11][11];

int po_vi[10];
int p_vi[11];
int peo_vi[11];

vector<int> f_p;
vector<int> ori_f_p;

int max_p;

void po_count(int a, int now_po)
{
    if (a >= 11)
    {
        if (now_po > max_p)
        {
            max_p = now_po;
        }
        return;
    }

    int now_p = 0;

    for (int p = 0; p < 11; p++)
    {
        if (peo_p[p][a] == 0) continue;
        if (p_vi[p] != 0) continue;

        p_vi[p] = 1;
        peo_vi[a] = p;

        po_count(a + 1, now_po + peo_p[p][a]);

        p_vi[p] = 0;

    }
};

int main() {
    cin >> t;

    for (int ci = 0; ci < t; ci++)
    {
        max_p = 0;
        for (int r = 0; r < 11; r++)
        {
            for (int c = 0; c < 11; c++)
            {
                cin >> peo_p[r][c];
            }
        }

        memset(p_vi, 0, sizeof(p_vi));

        po_count(0, 0);
        cout << max_p << endl;
    }
    return 0;
};
