#define _CRT_SECURE_NO_WARNINGS

#include <iostream>

using namespace std;

int n, m;
int t_s;

int t_peo[52];
int t_peo_pa[52];
int pa[52];

int p_info[52][52];
int s_num;

int Find(int now)
{
    if (pa[now] == now) {
        return now;
    }
    else {
        return pa[now] = Find(pa[now]);
    }
};

void Union(int one, int two) {
    int p_one = Find(one);
    int p_two = Find(two);

    if (p_one < p_two)
    {
        pa[p_two] = p_one;
    }
    else if (p_one > p_two)
    {
        pa[p_one] = p_two;
    }
};

int main() {
    cin >> n >> m;
    cin >> t_s;

    for (int i = 1; i < n + 1; i++)
    {
        pa[i] = i;
    }

    for (int i = 0; i < t_s; i++)
    {
        int tp_id = 0;
        cin >> tp_id;
        t_peo[i] = tp_id;
    }

    for (int i = 0; i < m; i++)
    {
        int m_s;
        cin >> m_s;

        for (int j = 0; j < m_s; j++)
        {
            int p_id;
            cin >> p_id;
            p_info[i][j] = p_id;
        }

        for (int j = 0; j < m_s-1; j++)
        {
            Union(p_info[i][j], p_info[i][j + 1]);
        }
    }
    
    for (int i = 0; i < t_s; i++)
    {
        t_peo_pa[Find(t_peo[i])] = 1;
    }

    for (int i = 0; i < m; i++)
    {
        bool s_ok = true;
        for (int j = 0; j < n; j++)
        {
            if (p_info[i][j] == 0) break;

            if (t_peo_pa[Find(p_info[i][j])] == 1) {
                s_ok = false;
                break;
            }
        }

        if (s_ok == true)
        {
            s_num += 1;
        }
    }

    cout << s_num << endl;
    return 0;
};
