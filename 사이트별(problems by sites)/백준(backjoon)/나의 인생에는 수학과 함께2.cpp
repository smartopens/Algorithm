#include <iostream>

using namespace std;

int n;
char m_map[6][6];
int vi[6][6];

int dr[2] = { 1,0 };
int dc[2] = { 0,1 };

int max_co;
int min_co;

void co_count(int pr, int pc, int now_co, int c_t)
{
	int ori_co = now_co;
	int ori_ct = c_t;

	if (pr == n && pc == n)
	{
		max_co = max(max_co, now_co);
		min_co = min(min_co, now_co);
		return;
	}

	int tr, tc;
	for (int i = 0; i < 2; i++)
	{
		tr = pr + dr[i];
		tc = pc + dc[i];

		if (1 > tr || n < tr || 1 > tc || n < tc) continue;
		if (vi[tr][tc] != 0) continue;

		vi[tr][tc] = 1;

		if (m_map[tr][tc] == '+')
		{
			co_count(tr, tc, now_co, 0);
		}
		else if (m_map[tr][tc] == '-')
		{
			co_count(tr, tc, now_co, 1);
		}
		else if (m_map[tr][tc] == '*')
		{
			co_count(tr, tc, now_co, 2);
		}
		else {
			// 연산하기
			if (c_t == 0)
			{
				co_count(tr, tc, now_co + (int)(m_map[tr][tc] - '0'), c_t);
			}
			else if (c_t == 1)
			{
				co_count(tr, tc, now_co - (int)(m_map[tr][tc] - '0'), c_t);
			}
			else if (c_t == 2)
			{
				co_count(tr, tc, now_co * (int)(m_map[tr][tc] - '0'), c_t);
			}
		}

		vi[tr][tc] = 0;
	}
}

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	cin >> n;
	for (int r = 1; r < n + 1; r++)
	{
		for (int c = 1; c < n + 1; c++)
		{
			cin >> m_map[r][c];
		}
	}

	max_co = -21e8;
	min_co = 21e8;
	vi[1][1] = 1;
	co_count(1, 1, m_map[1][1]-'0', 0);

	cout << max_co << " ";
	cout << min_co << endl;
	return 0;
}