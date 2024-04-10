#include <iostream>
#include <queue>

using namespace std;

int n, m;

struct n_no
{
	int e_n;
	int e_ord;
};

n_no c_map[502][502];
int vi[502][502];

int sr, sc;

struct p_no
{
	int r;
	int c;
};

int dr[8] = { -2,-1,1,2,2,1,-1,-2 };
int dc[8] = { 1,2,2,1,-1,-2,-2,-1 };

int d_ans[1002];

void m_count()
{
	queue<p_no> q;
	q.push({ sr,sc });
	vi[sr][sc] = 1;

	while (!q.empty())
	{
		p_no qv = q.front();
		q.pop();

		int tr, tc;
		for (int di = 0; di < 8; di++)
		{
			tr = qv.r + dr[di];
			tc = qv.c + dc[di];
			if (0 > tr || n - 1 < tr || 0 > tc || n - 1 < tc) continue;
			if (vi[tr][tc] != 0) continue;

			vi[tr][tc] = vi[qv.r][qv.c] + 1;
			if (c_map[tr][tc].e_n == 1)
			{
				d_ans[c_map[tr][tc].e_ord] = vi[tr][tc] - 1;
			}
			q.push({ tr,tc });
		}
	}
	return;
}

int main()
{
	cin >> n >> m;
	cin >> sr >> sc;
	sr -= 1;
	sc -= 1;
	int in_r, in_c;
	for (int dv = 1; dv < m + 1; dv++)
	{
		cin >> in_r >> in_c;
		in_r -= 1;
		in_c -= 1;
		c_map[in_r][in_c] = { 1,dv };
	}

	m_count();

	for (int dv = 1; dv < m + 1; dv++)
	{
		cout << d_ans[dv] << " ";
	}
	return 0;
}