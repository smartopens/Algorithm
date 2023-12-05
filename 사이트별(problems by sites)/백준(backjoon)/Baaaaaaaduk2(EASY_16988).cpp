#include <iostream>
#include <vector>
#include <cstring>
#include <queue>

using namespace std;

// 한번에 2수씩 둘 수 있다.
// 특정 돌을 빈칸이 없게 둘러싸면 먹을 수 있다.

int n, m;
int d_board[22][22];

struct d_no {
	int r;
	int c;
};

vector<d_no> d_case;
int max_a;
d_no a_case[2];

int vi[22][22];
int dr[4] = { -1,0,1,0 };
int dc[4] = { 0,1,0,-1 };

struct dq_no {
	int r;
	int c;
	int cnt;
};

int max_d;
int now_d;

// 상대 돌을 먹는 경우
// 상대돌이 가로막히거나 우리 돌만 만나는경우의 수를 센다.
void d_count(int vr, int vc)
{
	queue<d_no> q;
	q.push({ vr,vc});

	bool a_ok = true;
	int d_cnt = 1;
	while (!q.empty())
	{
		d_no qv = q.front();
		q.pop();

		int to_r, to_c;
		for (int i = 0; i < 4; i++)
		{
			to_r = qv.r + dr[i];
			to_c = qv.c + dc[i];

			if (to_r < 0 || to_r > n - 1 || to_c < 0 || to_c > m - 1) continue;
			if (vi[to_r][to_c] != 0) continue;
			if (d_board[to_r][to_c] == 1) continue;
			if (d_board[to_r][to_c] == 0)
			{
				a_ok = false;
			}
			vi[to_r][to_c] = vi[qv.r][qv.c] +1;
			d_cnt += 1;

			q.push({ to_r,to_c });
		}
	}

	if (a_ok)
	{
		now_d += d_cnt;
	}
}

// 돌을 두었을 경우 상대돌(2)을 먹는 수를 센다.
// 이때 여러 그룹의 돌을 먹을 수 있다.
void max_d_count()
{
	memset(vi, 0, sizeof(vi));
	now_d = 0;
	for (int r = 0; r < n; r++)
	{
		for (int c = 0; c < m; c++)
		{
			if (vi[r][c] != 0) continue;
			if (d_board[r][c] != 2) continue;

			vi[r][c] = 1;
			d_count(r, c);
		}
	}

	if (now_d > max_d)
	{
		max_d = now_d;
	}
}

// 2개의 돌을 둘 수 있다.
void a_count(int a, int idx)
{
	if (a > 1)
	{
		for (int av = 0; av < 2; av++)
		{
			d_board[a_case[av].r][a_case[av].c] = 1;
		}
		max_d_count();
		for (int av = 0; av < 2; av++)
		{
			d_board[a_case[av].r][a_case[av].c] = 0;
		}
		return;
	}

	for (int i = idx; i < d_case.size(); i++)
	{
		a_case[a] = d_case[i];
		a_count(a + 1, i + 1);
	}
}

int main()
{
	// 현재 바둑돌의 정보 입력받기
	cin >> n >> m;
	for (int r = 0; r < n; r++)
	{
		for (int c = 0; c < m; c++)
		{
			cin >> d_board[r][c];
			if (d_board[r][c] == 0)
			{
				d_case.push_back({ r,c });
			}
		}
	}

	// 돌을 두는 경우 고려하기
	max_a = d_case.size();
	a_count(0,0);

	cout << max_d << endl;
	return 0;
}