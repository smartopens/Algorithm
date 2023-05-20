#define _CRT_SECURE_NO_WARNINGS

#include <cstring>
#include <queue>
#include <iostream>

using namespace std;

// 바다정보 선언
int n, m;
int sea[302][302];
int visited[302][302] = { {} };

// 방향
int dr[4] = { -1,0,1,0 };
int dc[4] = { 0,1,0,-1 };

// 위치
struct node {
	int r;
	int c;
};

// 하나의 빙산 그룹 기록하기
void view_v(int sr, int sc) {
	queue<node> q;
	q.push({ sr, sc });

	visited[sr][sc] = 1;
	while (!q.empty())
	{
		node now = q.front();
		q.pop();
		int nr, nc;

		for (int di = 0; di < 4; di++)
		{
			nr = now.r + dr[di];
			nc = now.c + dc[di];

			if (0 > nr || n <= nr || 0 > nc || m <= nc) continue;
			if (visited[nr][nc] != 0) continue;
			if (sea[nr][nc] == 0) continue;

			visited[nr][nc] = 1;
			q.push({ nr, nc });
		}
	}
}

// 빙산 개수 세기
int v_count() {
	int v_num = 0;
	memset(visited, 0, sizeof(visited));

	for (int r = 0; r < n; r++)
	{
		for (int c = 0; c < m; c++)
		{
			if (sea[r][c] == 0) continue;
			if (visited[r][c] != 0) continue;

			view_v(r, c);
			v_num += 1;
		}
	}

	return v_num;
};

// 빙산 녹이기
void v_melt() {
	int new_sea[302][302] = { {} };

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
				if (sea[nr][nc] != 0) continue;
				s_num += 1;
			}

			if (sea[r][c] <= s_num)
			{
				new_sea[r][c] = 0;
			}
			else if (sea[r][c] > s_num)
			{
				new_sea[r][c] = sea[r][c] - s_num;
			}
		}
	}

	memcpy(sea, new_sea, sizeof(sea));

};

int main() {
	cin >> n >> m;

	int time = 1;

	// 더 이상 빙산이 없을 경우 기록한다.
	bool empty = false;
	
	// 빙산 정보 입력
	for (int r = 0; r < n; r++)
	{
		for (int c = 0; c < m; c++)
		{
			cin >> sea[r][c];
		}
	}

	// 시간이 흐른다.
	while (true)
	{
		// 빙산이 녹는다.
		v_melt();
		
		// 빙산의 개수 세기
		int v_num = v_count();

		// 문제 종료 조건
		if (v_num > 1) break;
		
		// 빙산이 없을 경우
		if (v_num == 0) {
			empty = true;
		}
		if (empty == true) break;
		time += 1;
	}

	// 빙산이 없다면 0을,
	// 여러그룹이라면 시간을 출력한다.
	if (!empty) {
		cout << time << endl;
	}
	else if (empty == true) {
		cout << 0 << endl;
	}

	return 0;
}
