#include <string>
#include <vector>
#include <iostream>
#include <math.h>
#include <algorithm>

using namespace std;

int n;
// aÀÎ °æ¿ì: 1, bÀÎ °æ¿ì:0
int dice_case[10];
vector<int> a_case;
vector<int> b_case;
vector<int> a_win;
vector<vector<int>> dice;

vector<int> a_sco_case;
vector<int> b_sco_case;

int max_a_win;

void get_sco(int a, int ds, int a_f, int now_sco)
{
    if (a > n / 2 - 1)
    {
        if (a_f != 0)
        {
            a_sco_case.push_back(now_sco);
        }
        else
        {
            b_sco_case.push_back(now_sco);
        }

        return;
    }

    for (int s = 0; s < 6; s++)
    {
        if (a_f != 0)
        {
            get_sco(a + 1, ds, a_f, now_sco + dice[a_case[a]][s]);
        }
        else
        {
            get_sco(a + 1, ds, a_f, now_sco + dice[b_case[a]][s]);
        }
    }
}

void a_win_count(int a, int d_id)
{
    if (a > n / 2 - 1)
    {
        a_case.clear();
        b_case.clear();
        a_sco_case.clear();
        b_sco_case.clear();

        for (int s = 0; s < n; s++)
        {
            if (dice_case[s] != 0)
            {
                a_case.push_back(s);
            }
            else
            {
                b_case.push_back(s);
            }
        }

        int a_win_n = 0;
        int a_sco = 0;
        int b_sco = 0;

        // a°¡ Á¡¼ö È¹µæÇÏ±â
        get_sco(0, 0, 1, 0);

        // b°¡ Á¡¼ö È¹µæÇÏ±â
        get_sco(0, 0, 0, 0);

        for (int as = 0; as < a_sco_case.size(); as++)
        {
            for (int bs = 0; bs < b_sco_case.size(); bs++)
            {
                if (a_sco_case[as] > b_sco_case[bs])
                {
                    a_win_n += 1;
                }
            }

        }

        if (max_a_win < a_win_n)
        {
            a_win = a_case;
            max_a_win = a_win_n;

        }
        return;
    }

    for (int ds = d_id; ds < n; ds++)
    {
        dice_case[ds] = 1;
        a_win_count(a + 1, ds + 1);
        dice_case[ds] = 0;
    }
}

vector<int> solution(vector<vector<int>> dice_tmp) {
    dice = dice_tmp;
    n = dice.size();

    max_a_win = 0;
    a_win.clear();
    a_win_count(0, 0);

    sort(a_win.begin(), a_win.end());
    for (int s = 0; s < a_win.size(); s++)
    {
        a_win[s] += 1;
    }

    cout << pow(6, 5);
    return a_win;
}