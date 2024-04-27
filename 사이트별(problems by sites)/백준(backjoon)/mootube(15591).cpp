#include <iostream>
#include <vector>
#include <cstring>

using namespace std;

int n, q;

struct v_no
{
	int to;
	int co;
};

vector<v_no> vi_gp[5002];
int vi[5002];

int u_map[5002][5002];

void reco_u_val(int sv, int vv, int now_u)
{
	int to_v;
	int min_u;
	for (int s = 0; s < vi_gp[vv].size(); s++)
	{
		to_v = vi_gp[vv][s].to;

		if (vi[to_v] != 0) continue;
		if (sv == to_v ) continue;

		min_u = min(vi_gp[vv][s].co, now_u);
		u_map[sv][to_v] = min_u;

		vi[to_v] = 1;
		reco_u_val(sv, to_v, min_u);
	}
}

int main()
{
	cin >> n >> q;
	int ga, gb, co;
	for (int m = 0; m < n - 1; m++)
	{
		cin >> ga >> gb >> co;
		vi_gp[ga].push_back({ gb, co });
		vi_gp[gb].push_back({ ga, co });
	}

	for (int sv = 1; sv < n + 1; sv++)
	{
		memset(vi, 0, sizeof(vi));
		vi[sv] = 1;
		reco_u_val(sv,sv, 21e8);
	}

	int kv, sv;
	int max_un = 0;
	for (int qc = 0; qc < q; qc++)
	{
		cin >> kv >> sv;

		max_un = 0;
		//cout << sv << endl;
		for (int to_v = 1; to_v < n + 1; to_v++)
		{
			if (sv == to_v) continue;

			if (u_map[sv][to_v] >= kv)
			{
				max_un += 1;
			}

			//cout << u_map[sv][to_v] << " ";
		}
		//cout << endl;
		cout << max_un << "\n";
	}
	return 0;
}