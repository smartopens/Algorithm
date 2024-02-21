#include <iostream>
#include <vector>

using namespace std;

int n, m;
int m_map1[32][32];
int m_map2[32][32];

int vi[32][32];

struct m_no
{
	int r;
	int c;
};

vector<m_no> g_map[1000];

int dr[4] = { -1,0,1,0 };
int dc[4] = { 0,1,0,-1 };

bool can_cpcu;

void dfs(int gr, int gc, int g_id, int m_v)
{
	int tr, tc;
	for (int i = 0; i < 4; i++)
	{
		tr = gr + dr[i];
		tc = gc + dc[i];
		if (0 > tr || n - 1 < tr || 0 > tc || m - 1 < tc) continue;
		if (vi[tr][tc] != 0) continue;
		if (m_map1[tr][tc] != m_v) continue;

		vi[tr][tc] = 1;
		g_map[g_id].push_back({ tr,tc });
		dfs(tr, tc, g_id, m_v);
	}
}

int main()
{
	cin >> n >> m;
	for (int r = 0; r < n; r++)
	{
		for (int c = 0; c < m; c++)
		{
			cin >> m_map1[r][c];
		}
	}

	for (int r = 0; r < n; r++)
	{
		for (int c = 0; c < m; c++)
		{
			cin >> m_map2[r][c];
		}
	}

	int g_id = 1;
	for (int r = 0; r < n; r++)
	{
		for (int c = 0; c < m; c++)
		{
			if (vi[r][c] != 0) continue;
			
			vi[r][c] = 1;
			g_map[g_id].push_back({ r,c });
			dfs(r, c, g_id, m_map1[r][c]);
			g_id += 1;
		}
	}
	
	can_cpcu = true;
	bool now_cpcu = true;
	int n_same = 0;
	for (int gv = 1; gv < g_id; gv++)
	{
		now_cpcu = true;
		// 변환 후의 백신 판단
		int tr1, tc1, tr2, tc2;
		int m1_v, m2_v;
		for (int s = 0; s < g_map[gv].size()-1; s++)
		{
			tr1 = g_map[gv][s].r;
			tc1 = g_map[gv][s].c;
			tr2 = g_map[gv][s+1].r;
			tc2 = g_map[gv][s+1].c;

			if (m_map2[tr2][tc2] != m_map2[tr1][tc1])
			{
				now_cpcu = false;
				break;
			}
		}

		if (now_cpcu == false)
		{
			can_cpcu = false;
		}
		else if (now_cpcu == true)
		{
			m1_v = m_map1[g_map[gv][0].r][g_map[gv][0].c];
			m2_v = m_map2[g_map[gv][0].r][g_map[gv][0].c];

			if (m1_v != m2_v)
			{
				n_same += 1;
			}
		}
	}

	if (n_same >= 2)
	{
		can_cpcu = false;
	}

	if (can_cpcu == true)
	{
		cout << "YES\n";
	}
	else if (can_cpcu == false)
	{
		cout << "NO\n";
	}

	return 0;
}