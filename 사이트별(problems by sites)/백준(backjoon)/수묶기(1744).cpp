#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <algorithm>

using namespace std;

int n;
int p_num[1000002];
int m_num[1000002];
int z_num [1000002];

int p_size;
int m_size;
int z_size;
int max_sum;

bool cmp(int a, int b)
{
    if (a > b) {
        return true;
    }
    if (a < b) {
        return false;
    }
    return false;
}

int main() {
    cin >> n;
    max_sum = 0;

    for (int i = 0; i < n; i++)
    {
        int num;
        cin >> num;

        if (num > 0) {
            p_num[p_size] = num;
            p_size += 1;
        }
        else if (num < 0) {
            m_num[m_size] = num;
            m_size += 1;
        }
        else if (num == 0) {
            z_num[z_size] = num;
            z_size += 1;
        }
    }

    
    int ps = 0;
    int ms = 0;
    int zs = 0;

    sort(p_num, p_num + p_size, cmp);
    sort(m_num, m_num + m_size);

    for (int i = 0; i < p_size-1; i+=2)
    {
        if (p_num[i] * p_num[i + 1] < p_num[i] + p_num[i + 1]) continue;
        max_sum += p_num[i] * p_num[i + 1];
        ps += 2;
    }

    for (int i = ps; i < p_size; i++)
    {
        max_sum += p_num[i];
    }

    for (int i = 0; i < m_size - 1; i += 2)
    {
        max_sum += m_num[i] * m_num[i + 1];
        ms += 2;
    }

    int ms2 = ms;
    for (int i = ms; i < m_size; i++)
    {
        if (z_size < 1) break;
        ms2 += 1;
        z_size -= 1;
    }

    for (int i = ms2; i < m_size; i++)
    {
        max_sum += m_num[i];
    }

    cout << max_sum << endl;
    return 0;
}
