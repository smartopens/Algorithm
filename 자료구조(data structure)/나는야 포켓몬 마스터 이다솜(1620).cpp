#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <string>
#include <cctype>
#include <unordered_map>

using namespace std;

int n, m;
unordered_map<string, int> na_id;
unordered_map<int, string> id_na;

int main() {
    cin.tie(0);
    cout.tie(0);
    ios_base::sync_with_stdio(true);

    cin >> n >> m;

    string in_na;
    for (int i = 1; i < n + 1; i++)
    {
        cin >> in_na;
        na_id[in_na] = i;
        id_na[i] = in_na;
    }

    string pro_st;
    for (int i = 0; i < m; i++)
    {
        cin >> pro_st;
        if (isdigit(pro_st[0]) == false) {
            cout << na_id[pro_st] << "\n";
        }
        else
        {
            cout << id_na[stoi(pro_st)] << "\n";
        }
    }
    return 0;
};
