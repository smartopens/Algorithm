#include <iostream>
#include <queue>

using namespace std;

int n, m;

char c_map[22][22];
int vi[22][22][22][22]; // 해설 참조

int sr1, sc1;
int sr2, sc2;

struct c_no
{
	int cr1;
	int cc1;
	int cr2;
	int cc2;
	int out_cn;
};

int dr[4] = { -1,0,1,0 };
int dc[4] = { 0,1,0,-1 };

bool p_ok;
int min_bn;

vector<int> c_move(int cr, int cc, int di)
{
	int tr, tc;
	tr = cr + dr[di];
	tc = cc + dc[di];

	if (0 > tr || n - 1 < tr || 0 > tc || m - 1 < tc)
	{
		return { 0,0, 1 };
	}
	if (c_map[tr][tc] == '#')
	{
		return { cr, cc, 0 };
	}

	return { tr,tc, 0 };
}

void m_count()
{
	queue<c_no> q;
	q.push({ sr1,sc1,sr2,sc2,0 });

	vi[sr1][sc1][sr2][sc2] = 1;
	while (!q.empty())
	{
		c_no cv = q.front();
		q.pop();

		vector<int> to_c1 = {};
		vector<int> to_c2 = {};
		int to_cn = cv.out_cn;

		for (int di = 0; di < 4; di++)
		{
			to_c1 = c_move(cv.cr1, cv.cc1, di);
			to_c2 = c_move(cv.cr2, cv.cc2, di);

			to_cn = cv.out_cn;
			to_cn += to_c1[2];
			to_cn += to_c2[2];

			//cout << to_cn << " " << di << "\n";
			//cout << to_c1[0] << " " << to_c1[1] << "\n";
			if (to_cn >= 2)
			{
				continue;
			}
			else if (to_cn == 1)
			{
				p_ok = true;
				min_bn = vi[cv.cr1][cv.cc1][cv.cr2][cv.cc2];
				return;
			}

			if(vi[to_c1[0]][to_c1[1]][to_c2[0]][to_c2[1]] == 0
				&& vi[cv.cr1][cv.cc1][cv.cr2][cv.cc2] <= 9)
			{
				vi[to_c1[0]][to_c1[1]][to_c2[0]][to_c2[1]] = vi[cv.cr1][cv.cc1][cv.cr2][cv.cc2] + 1;
				q.push({ to_c1[0], to_c1[1], to_c2[0], to_c2[1],to_cn });
			}
		}
	}
}

int main()
{
	cin >> n >> m;
	bool co1_find = false;
	for (int r = 0; r < n; r++)
	{
		for (int c = 0; c < m; c++)
		{
			cin >> c_map[r][c];

			if (co1_find == false && c_map[r][c] == 'o')
			{
				sr1 = r;
				sc1 = c;
				co1_find = true;
			}
			else if (co1_find == true && c_map[r][c] == 'o')
			{
				sr2 = r;
				sc2 = c;
			}
		}
	}

	p_ok = false;
	min_bn = 0;
	m_count();

	if (p_ok == false)
	{
		cout << -1 << "\n";
	}
	else
	{
		cout << min_bn << "\n";
	}
	return 0;
}