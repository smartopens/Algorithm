#include <iostream>
#include <string>
#include <cstring>

using namespace std;

int n;
int s_board[9][9];
int vi[9][9];

int max_a;
int p_sn[10];
bool find_sdo;

bool is_sdo(int vr, int vc)
{
	int now_n = s_board[vr][vc];
	// 행판단
	for (int s = 0; s < n; s++)
	{
		if (now_n == s_board[vr][s])
		{
			if (vc == s) continue;
			return false;
		}
	}

	// 열판단
	for (int s = 0; s < n; s++)
	{
		if (now_n == s_board[s][vc])
		{
			if (vr == s) continue;
			return false;
		}
	}

	// 사각형 판단
	int sr = (vr / 3) * 3;
	int sc = (vc / 3) * 3;

	for (int rp = 0; rp < 3; rp++)
	{
		for (int cp = 0; cp < 3; cp++)
		{
			if (now_n == s_board[sr + rp][sc + cp])
			{
				if ((sr + rp) == vr && (sc + cp) == vc) continue;
				return false;
			}
		}
	}
	return true;
}

void make_sdouku(int vr, int vc)
{
	if (vr > n-1)
	{
		if (find_sdo == false)
		{
			for (int r = 0; r < n; r++)
			{
				for (int c = 0; c < n; c++)
				{
					cout << s_board[r][c];
				}
				cout << endl;
			}
			find_sdo = true;
		}
		return;
	}

	if (find_sdo)
	{
		return;
	}

	/*for (int r = 0; r < n; r++)
	{
		for (int c = 0; c < n; c++)
		{
			cout << s_board[r][c] << " ";
		}
		cout << endl;
	}
	cout << endl;*/

	if (vc > n - 1)
	{
		make_sdouku(vr + 1, 0);
		return;
	}

	if (s_board[vr][vc] != 0)
	{
		make_sdouku(vr, vc + 1);
	}
	else {
		for (int i = 1; i < 10; i++)
		{
			s_board[vr][vc] = i;
			if (is_sdo(vr, vc)) {
				make_sdouku(vr, vc + 1);
			}
			s_board[vr][vc] = 0;
		}
	}
}

int main()
{
	n = 9;
	string in_sn;
	for (int r = 0; r < n; r++)
	{
		cin >> in_sn;
		for (int c = 0; c < n; c++)
		{
			s_board[r][c] = (int)(in_sn[c] - '0');
			if (s_board[r][c] == 0)
			{
				max_a += 1;
			}
		}
	}

	/*for (int r = 0; r < n; r++)
	{
		for (int c = 0; c < n; c++)
		{
			cout << s_board[r][c] << " ";
		}
		cout << endl;
	}
	cout << endl;*/
	find_sdo = false;
	make_sdouku(0,0);

	return 0;
}