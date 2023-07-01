#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <string>

using namespace std;
string in_st;
int n;
int ans;
int vi[52];

int dfs(int n_id, int p_m)
{
    int now_n = 0;
    for (int i = n_id; i < n; i++)
    {
        if (vi[i] != 0) continue;
        if (in_st[i] == '(') {
            vi[i] = 1;
            now_n -= 1;
            now_n += dfs(i + 1, (int)(in_st[i - 1] - '0'));
        }
        else if (in_st[i] == ')') {
            vi[i] = 1;
            return now_n* p_m;
        }
        else {
            now_n += 1;
            vi[i] = 1;
        }
    }

    return now_n * p_m;
}

int main() {
    cin >> in_st;
    n = in_st.length();

    ans = dfs(0,1);
    cout << ans << endl;
    return 0;
};
