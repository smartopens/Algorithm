#include<iostream>
#include <algorithm>

using namespace std;

int n, m;
int m_w[100002];
int m_best[100002];

int bn;

int main(int argc, char** argv)
{
    cin >> n >> m;
    for (int i = 1; i < n + 1; i++)
    {
        cin >> m_w[i];
        m_best[i] = 1;
    }

    int ma, mb;
    int max_v;
    for (int i = 0; i < m; i++)
    {
        cin >> ma >> mb;
        //max_v = max(m_w[ma], m_w[mb]);

        if (m_w[ma] <= m_w[mb])
        {
            m_best[ma] = 0;
        }

        if (m_w[mb] <= m_w[ma])
        {
            m_best[mb] = 0;
        }
    }

    bn = 0;
    for (int i = 1; i < n + 1; i++)
    {
        if (m_best[i] == 0) continue;
        bn += 1;
    }

    cout << bn << endl;
    return 0;
}