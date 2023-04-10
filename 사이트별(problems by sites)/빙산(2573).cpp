#define _CRT_SECURE_NO_WARNINGS

#include <cstring>
#include <queue>
#include <iostream>

using namespace std;

int n, m;
int sea[302][302];
int visited[302][302] = { {} };

int dr[4] = { -1,0,1,0 };
int dc[4] = { 0,1,0,-1 };

struct node {
	int r;
	int c;
};

void view_v(int sr, int sc) {
	queue<node> q;
	q.push({ sr, sc });

	visited[sr][sc] = 1;
	while(!q.empty())
	{
		
	}
}

int v_count() {
	int v_num = 0;
	memset(visited, 0, sizeof(visited));

	for (int r = 0; r < n; r++)
	{
		for (int c = 0; c < m; c++)
		{
			if (sea[r][c] == 0) continue;
			if (visited[r][c] != 0) continue;

			view_v(r,c);
			v_num += 1;
		}
	}

	return v_num;
};

void v_melt() {
	for (int r = 0; r < n; r++)
	{
		for (int c = 0; c < m; c++)
		{
			if (sea[r][c] == 0) continue;
			int s_num = 0;
			int nr, nc;

			for (int di = 0; di < 4; di++)
			{
				nr = r + dr[di];
				nc = c + dc[di];

				if (0 > nr || n <= nr || 0 > nc || m <= nc) continue;
				
				s_num += 1;
			}

			if (sea[r][c] <= s_num)
			{
				sea[r][c] = 0;
			}
			else if (sea[r][c] > s_num)
			{
				sea[r][c] -= s_num;
			}
		}
	}
};

int main() {
	cin >> n >> m;

	int time = 1;
	bool empty = false;

	for (int r=0; r<n; r++)
	{
		for (int c = 0; c < m; c++)
		{
			cin >> sea[r][c];
		}
	}

	while (true)
	{
		v_melt();
		int v_num = v_count();
		if (v_num > 1) break;
		if (v_num == 0) {
			empty = true;
		}
		if (empty == true) break;
		time += 1;
	}

	if (!empty) {
		cout << time << endl;
	}
	else if (empty == true) {
		cout << 0 << endl;
	}

	return 0;
}