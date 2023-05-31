#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <string>

using namespace std;

int n;
char nums[3] = { '1','2','3' };

bool gn_find(int id, string m_str)
{
    if (id >= n)
    {
        cout << m_str << endl;
        return true;
    }

    for (int i = 0; i < 3; i++)
    {
        bool is_ok = true;
        string n_str = m_str + nums[i];
        int n_s = n_str.length();

        for (int dj = 1; dj < n_s / 2 + 1; dj++)
        {
            string tmp1 = "";
            string tmp2 = "";

            for (int k = n_s - 1; k > n_s - 1 - dj; k--)
            {
                tmp1 += n_str[k];
            }

            for (int k = n_s - 1 - dj; k > n_s - 1 - 2*dj; k--)
            {
                tmp2 += n_str[k];
            }

            if (tmp1 == tmp2) {
                is_ok = false;
                break;
            }
        }

        if (is_ok != true) continue;
        if (gn_find(id + 1, n_str)) return true;

    }

    return false;
}

int main() {
    cin >> n;

    gn_find(0, "");
    return 0;
}
