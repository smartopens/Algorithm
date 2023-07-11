#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <string>
#include <map>
#include <cstring>
#include <algorithm>
#include <vector>

using namespace std;

int n;
int str_idx[10];

int alp_res[27];
vector<char> alp_idx[10];

int a_id;
int al_id;

char alps[10];
map<char, int> alp_int;
int n_vi[10];

string words[10];
int max_wn;

void num_match(int a, int now_n)
{
    if (a >= al_id) {

        int wn = 0;
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < words[i].length(); j++)
            {
                int now_w = alp_int[words[i][j]];
                int m_s = words[i].length() - j - 1;
                int mm_n = 1;

                for (int s = 0; s < m_s; s++)
                {
                    mm_n *= 10;
                }
                wn += mm_n * now_w;
            }
        }

        if (max_wn < wn)
        {
            max_wn = wn;
        }
        return;
    }

    int is_in = 0;
    for (int s = 0; s < alp_idx[a].size(); s++)
    {
        char st = alp_idx[a][s];
        if (alp_int[st] == -1)
        {
            is_in += 1;
        }
    }

    if (is_in > 1) {
        for (int s = 0; s < alp_idx[a].size(); s++)
        {
            char st = alp_idx[a][s];
            if (alp_int[st] == -1)
            {
                alp_int[st] = now_n;

                is_in = true;
                num_match(a, now_n - 1);

                alp_int[st] = -1;
            }
        }
    }
    else if (is_in == 1) {
        for (int s = 0; s < alp_idx[a].size(); s++)
        {
            char st = alp_idx[a][s];
            if (alp_int[st] == -1)
            {
                alp_int[st] = now_n;

                num_match(a + 1, now_n - 1);

                alp_int[st] = -1;
            }
        }
    }
    else if(is_in == 0){
        num_match(a + 1, now_n);
    }
    return;
}

int main() {
    cin >> n;
    string st_in = "";
    for (int i = 0; i < n; i++)
    {
        cin >> st_in;
        words[i] = st_in;
        str_idx[i] = st_in.length();

        if (al_id < st_in.length())
        {
            al_id = st_in.length();
        }
    }

    for (int i = 0; i < n; i++)
    {
        st_in = words[i];
        for (int j = 0; j < st_in.length(); j++)
        {
            bool is_in = false;
            for (int s = 0; s < alp_idx[al_id - st_in.length() + j].size(); s++)
            {
                if (alp_idx[al_id - st_in.length() + j][s] == st_in[j])
                {
                    is_in = true;
                    break;
                }
            }
            if (is_in == false)
            {
                alp_idx[al_id - st_in.length() + j].push_back({ st_in[j] });
            }
            alp_res[st_in[j] - 'A'] = 1;
        }
    }

    for (int i = 0; i < 27; i++)
    {
        if (alp_res[i] == 0) continue;
        alps[a_id] = 'A' + i;
        alp_int['A' + i] = -1;
        a_id += 1;
    }

    num_match(0,9);
    cout << max_wn << endl;
    return 0;
};
