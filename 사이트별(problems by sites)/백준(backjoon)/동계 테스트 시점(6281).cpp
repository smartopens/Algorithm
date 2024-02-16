#include <iostream>
#include <string>
#include <queue>

using namespace std;

int n;

int d_mirror[52][52];
int co_map[52][52];

int dr[4] = { -1,0,1,0 };
int dc[4] = { 0,1,0,-1 };

int min_co;

struct q_no
{
	int tr;
	int tc;
	int co;

	bool operator < (q_no now) const
	{
		if (co > now.co)
		{
			return true;
		}
		if (co < now.co)
		{
			return false;
		}
		return false;
	}
};

void cost_count()
{
	for (int r = 0; r < n; r++)
	{
		for (int c = 0; c < n; c++)
		{
			co_map[r][c] = 21e8;
		}
	}
	co_map[0][0] = 0;
	priority_queue<q_no> pq;
	pq.push({ 0,0,0 });

	while (!pq.empty())
	{
		q_no dv = pq.top();
		pq.pop();

		if (co_map[dv.tr][dv.tc] < dv.co) continue;

		int tr, tc, to_co;
		for (int di = 0; di < 4; di++)
		{
			tr = dv.tr + dr[di];
			tc = dv.tc + dc[di];

			if (0 > tr || n - 1 < tr || 0 > tc || n - 1 < tc) continue;

			to_co = co_map[dv.tr][dv.tc] + d_mirror[tr][tc];
			if (co_map[tr][tc] <= to_co) continue;
			
			co_map[tr][tc] = to_co;
			pq.push({ tr, tc, to_co });
		}
	}
}

int main()
{
	cin >> n;
	string in_d;
	for (int r = 0; r < n; r++)
	{
		cin >> in_d;
		for (int c = 0; c < n; c++)
		{
			d_mirror[r][c] = in_d[c] - '0';

			if (d_mirror[r][c] == 0)
			{
				d_mirror[r][c] = 1;
			}
			else if (d_mirror[r][c] == 1)
			{
				d_mirror[r][c] = 0;
			}
		}
	}

	min_co = 21e8;
	cost_count();

	min_co = co_map[n - 1][n - 1];
	cout << min_co << endl;

	return 0;
}