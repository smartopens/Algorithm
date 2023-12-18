#include <iostream>
#include <vector>
#include <cstring>
#include <algorithm>

using namespace std;

// 사무실에 k개의 cctv가 있다.
// 종류: 한쪽, 두쪽(서로반대), 두쪽(직각), 세방향, 네방향
// 번호마다 방향
// cctv는 회전 가능 / 벽인 경우 막힌다.
// 시간복잡도: 64*(64) (1000)  > 4*10^6

// vector<int> v_dir [5]
// 한쪽: dr: {-1,0,1,0} ...
// 두쪽: (0,1), (0,-1) / 
// v1, v2, v3 ...

// 번호마다 방향의 경우를 고려하기
// cc1, cc2, cc3, ... cc8
// c_no: int r, int c, int cn

int n, m;
int c_board[10][10];
int c_board_back[10][10];

struct c_no
{
	int r;
	int c;
	int cn;
	int cd;
};

vector<c_no> c_info;

int dr[4] = { -1,0,1,0 };
int dc[4] = { 0,1,0,-1 };
int max_p;

int min_in;
int max_a;

// 가로방향, 세로방향
// dc:{1,-1}
// 4,2,4,4,1

void up_move(int sr, int sc)
{
	for (int r = sr - 1; r > -1; r--)
	{
		if (c_board[r][sc] == 6)
		{
			break;
		}
		c_board[r][sc] = 9;
	}
}
void right_move(int sr, int sc)
{
	for (int c = sc + 1; c < m; c++)
	{
		if (c_board[sr][c] == 6)
		{
			break;
		}
		c_board[sr][c] = 9;
	}
}

void down_move(int sr, int sc)
{
	for (int r = sr + 1; r < n; r++)
	{
		if (c_board[r][sc] == 6)
		{
			break;
		}
		c_board[r][sc] = 9;
	}
}
void left_move(int sr, int sc)
{
	for (int c = sc - 1; c > -1; c--)
	{
		if (c_board[sr][c] == 6)
		{
			break;
		}
		c_board[sr][c] = 9;
	}
}

void v_count(int a)
{
	int cv = 0;
	if (a > max_a)
	{
		int cr;
		int cc;
		int cd;
		int to_r, to_c;

		//memcpy(c_board, c_board_back, sizeof(c_board_back));

		for (int r = 0; r < n; r++)
		{
			for (int c = 0; c < m; c++)
			{
				c_board[r][c] = c_board_back[r][c];
			}
		}

		for (int s = 0; s < c_info.size(); s++)
		{
			cv = c_info[s].cn;
			cr = c_info[s].r;
			cc = c_info[s].c;
			cd = c_info[s].cd;

			if (cv == 1)
			{
				if (cd == 0)
				{
					up_move(cr, cc);
				}
				else if (cd == 1)
				{
					right_move(cr, cc);
				}
				else if (cd == 2)
				{
					down_move(cr, cc);
				}
				else if (cd == 3)
				{
					left_move(cr, cc);
				}
			}
			else if (cv == 2)
			{
				if (cd == 0)
				{
					right_move(cr, cc);
					left_move(cr, cc);
				}
				else if (cd == 1)
				{
					up_move(cr, cc);
					down_move(cr, cc);
				}
			}
			else if (cv == 3)
			{
				if (cd == 0)
				{
					up_move(cr, cc);
					right_move(cr, cc);
				}
				else if (cd == 1)
				{
					right_move(cr, cc);
					down_move(cr, cc);
				}
				else if (cd == 2)
				{
					down_move(cr, cc);
					left_move(cr, cc);
				}
				else if (cd == 3)
				{
					left_move(cr, cc);
					up_move(cr, cc);
				}
			}
			else if (cv == 4)
			{
				if (cd == 0)
				{
					up_move(cr, cc);
					right_move(cr, cc);
					down_move(cr, cc);
				}
				else if (cd == 1)
				{
					right_move(cr, cc);
					down_move(cr, cc);
					left_move(cr, cc);
				}
				else if (cd == 2)
				{
					down_move(cr, cc);
					left_move(cr, cc);
					up_move(cr, cc);
				}
				else if (cd == 3)
				{
					left_move(cr, cc);
					up_move(cr, cc);
					right_move(cr, cc);
				}
			}
			else if (cv == 5)
			{
				up_move(cr, cc);
				right_move(cr, cc);
				down_move(cr, cc);
				left_move(cr, cc);
			}
		}

		int now_in = 0;
		for (int r = 0; r < n; r++)
		{
			for (int c = 0; c < m; c++)
			{
				if (c_board[r][c] == 0)
				{
					now_in += 1;
				}
			}
		}

		if (now_in < min_in)
		{
			min_in = now_in;

			//cout << cd << "\n";
			//for (int r = 0; r < n; r++)
			//{
			//	for (int c = 0; c < m; c++)
			//	{
			//		cout << c_board[r][c] << " ";
			//	}
			//	cout << endl;
			//}
			//cout << endl;
		}

		return;
	}

	cv = c_info[a].cn;
	if(cv == 1)
	{
		for (int i = 0; i < 4; i++)
		{
			c_info[a].cd = i;
			v_count(a + 1);
		}
	}
	else if (cv == 2)
	{
		for (int i = 0; i < 2; i++)
		{
			c_info[a].cd = i;
			v_count(a + 1);
		}
	}
	else if (cv == 3)
	{
		for (int i = 0; i < 4; i++)
		{
			c_info[a].cd = i;
			v_count(a + 1);
		}
	}
	else if (cv == 4)
	{
		for (int i = 0; i < 4; i++)
		{
			c_info[a].cd = i;
			v_count(a + 1);
		}
	}
	else if (cv == 5)
	{
		for (int i = 0; i < 1; i++)
		{
			c_info[a].cd = i;
			v_count(a + 1);
		}
	}
}

int main()
{
	
	cin >> n >> m;
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	for (int r = 0; r < n; r++)
	{
		for (int c = 0; c < m; c++)
		{
			cin >> c_board[r][c];
			c_board_back[r][c] = c_board[r][c];

			if (c_board[r][c] > 0 && c_board[r][c] < 6)
			{
				c_info.push_back({ r,c,c_board[r][c],0 });
			}
		}
	}
	
	min_in = n * m;
	max_p = max(n, m) - 1;
	max_a = c_info.size() - 1;
	v_count(0);

	cout << min_in << endl;
	return 0;
}