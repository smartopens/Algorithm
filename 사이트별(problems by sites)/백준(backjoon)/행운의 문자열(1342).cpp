#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <string>
#include <map>

using namespace std;

int s_s;
string ori_str;

int str_num[28];
int vi[12];
int l_num;
map<string, int> s_vi;

void l_count(int a, char prev, string m_str)
{
    if (a >= s_s)
    {
        bool is_l = true;

        if (is_l == true) {
            l_num += 1;
        }

        return;
    }

    for (int i = 0; i < s_s; i++)
    {
        if (vi[i] != 0) continue;

        if (prev == ori_str[i])
        {
            continue;
        }

        vi[i] = 1;

        l_count(a + 1, ori_str[i], m_str + ori_str[i]);
        vi[i] = 0;

    }

    return;
}

int main() {
    cin >> ori_str;
    s_s = ori_str.length();

    for (int i = 0; i < s_s; i++)
    {
        str_num[ori_str[i] - 'a'] += 1;
    }

    l_count(0, '\0', "");

    for (int i = 0; i < 28; i++)
    {
        int d_num = 1;
        if (str_num[i] <= 1) continue;
        for (int j = 1; j < str_num[i] + 1; j++)
        {
            d_num *= j;
        }
        l_num /= d_num;
    }

    cout << l_num << endl;

    return 0;
}
