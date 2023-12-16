#include <iostream>
#include <cstring>

using namespace std;

// 치즈의 2변이상이 빈공간과 접해있다면 녹는다.
// 시간복잡도: 60*(100*100*2 + 4*100*100 + 100*100)

int n, m;
int c_board[102][102];
int c_board_tmp[102][102];
int c_vi[102][102];

int out_air[102][102];
int out_vi[102][102];

int dr[4] = { -1,0,1,0 };
int dc[4] = { 0,1,0,-1 };

void c_melt()
{
	memcpy(c_board_tmp, c_board, sizeof(c_board));

	int to_r, to_c, on;
	for (int r = 0; r < n; r++)
	{
		for (int c = 0; c < m; c++)
		{
			if (c_board_tmp[r][c] == 1)
			{
				on = 0;
				for (int i = 0; i < 4; i++)
				{
					to_r = r + dr[i];
					to_c = c + dc[i];
					if (0 > to_r || n - 1 < to_r || 0 > to_c || m - 1 < to_c) continue;
					if (c_board[to_r][to_c] != 0) continue;
					if (out_air[to_r][to_c] == 0) continue;

					on += 1;
				}
				
				if (on >= 2)
				{
					c_board[r][c] = 0;
				}
			}
		}
	}
}

// s1, s2, s3, ...s
void out_count(int ar, int ac)
{
	out_vi[ar][ac] = 1;
	out_air[ar][ac] = 1;
	
	int to_r, to_c;
	for (int i = 0; i < 4; i++)
	{
		to_r = ar + dr[i];
		to_c = ac + dc[i];
		if (0 > to_r || n - 1 < to_r || 0 > to_c || m - 1 < to_c) continue;
		if (c_board[to_r][to_c] != 0) continue;
		if (out_vi[to_r][to_c] != 0) continue;

		out_count(to_r, to_c);
	}
}

int main()
{
	cin >> n >> m;
	for (int r = 0; r < n; r++)
	{
		for (int c = 0; c < m; c++)
		{
			cin >> c_board[r][c];
		}
	}

	bool is_empty = true;
	int h_tm = 0;

	while (true)
	{
		// 종료 조건
		is_empty = true;
		for (int r = 0; r < n; r++)
		{
			for (int c = 0; c < m; c++)
			{
				if (c_board[r][c] != 0)
				{
					is_empty = false;
				}
			}
		}

		if (is_empty)
		{
			break;
		}

		// 외부 공간 기록
		memset(out_air, 0, sizeof(out_air));
		memset(out_vi, 0, sizeof(out_vi));
		for (int r = 0; r < n; r++)
		{
			if (c_board[r][0] == 0 && out_vi[r][0] != 1)
			{
				out_count(r,0);
			}
			if (c_board[r][m-1] == 0 && out_vi[r][m-1] != 1)
			{
				out_count(r, m-1);
			}
		}

		for (int c = 0; c < m; c++)
		{
			if (c_board[0][c] == 0 && out_vi[0][c] != 1)
			{
				out_count(0, c);
			}
			if (c_board[n-1][c] == 0 && out_vi[n-1][c] != 1)
			{
				out_count(n-1, c);
			}
		}

		// 치즈 녹는 경우
		c_melt();

		h_tm += 1;
	}

	cout << h_tm << endl;
	return 0;
}