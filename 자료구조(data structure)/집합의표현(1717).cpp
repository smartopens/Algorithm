#define _CRT_SECURE_NO_WARNINGS

#include <iostream>

using namespace std;

int n, m;
int pa[1000002];

int Find(int a)
{
    if (pa[a] == a) {
        return a;
    }

    return pa[a] = Find(pa[a]);
}

void Union(int a, int b)
{
    int p_a = Find(a);
    int p_b = Find(b);

    if (p_a == p_b) return;

    if (b > a)
    {
        pa[p_b] = pa[p_a];
    }
    else {
        pa[p_a] = pa[p_b];
    }

    return;
}

// 2, 4
// 3, 10
// 5, 8


int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> n >> m;
    for (int i = 0; i < n+1; i++)
    {
        pa[i] = i;
    }

    for (int i = 0; i < m; i++)
    {
        int com, one, two;
        cin >> com >> one >> two;

        if (com == 0) {
            Union(one, two);
        }
        else if (com == 1) {
            if (Find(one) != Find(two))
            {
                cout << "NO\n";
            }
            else {
                cout << "YES\n";
            }
        }
    }
    return 0;
}
