#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
 
int n, m, r;

vector<int> down_gp[100002];
int vi[100002];

int gv_ord[100002];
int o_n;

void ord_reco(int a, int gv)
{
    vi[gv] = 1;
    o_n += 1;
    gv_ord[gv] = o_n;

    int to_v;
    for (int s = 0; s < down_gp[gv].size(); s++)
    {
        to_v = down_gp[gv][s];

        if (vi[to_v] != 0) continue;
        ord_reco(a + 1, to_v);
    }
}

int main()
{
    cin >> n >> m >> r;
    int ga, gb;
    for (int i = 0; i < m; i++)
    {
        cin >> ga >> gb;
        down_gp[ga].push_back(gb);
        down_gp[gb].push_back(ga);
    }

    for (int gv = 1; gv < n + 1; gv++)
    {
        sort(down_gp[gv].begin(), down_gp[gv].end(), greater<int>());
    } 

    o_n = 0;
    ord_reco(1,r);

    for (int gv = 1; gv < n + 1; gv++)
    {
        cout << gv_ord[gv] << "\n";
    }

 	return 0;
}