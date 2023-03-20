#define _NO_SECURE_WARNINGS

#include <cstring>
#include <queue>
#include <iostream>

using namespace std;

int n;
int m;
int board[20][20];

int max_ans = 0;
int visited[20][20];

int dr[4] = { -1,1,0,0 };
int dc[4] = { 0,0,-1,1 };

struct node {
	int r;
	int c;
};

void update_h_num(int h_num, int k, int sr, int sc) {
	int total_value = h_num * m - (k * k + (k - 1) * (k - 1));


	if (total_value >= 0 && h_num > max_ans) {
		max_ans = h_num;
	}
}

void bfs(int sr, int sc) {
	int ki = 1;
	int h_num = 0;
	memset(visited, 0, sizeof(visited));

	visited[sr][sc] = 1;
	
	queue<node> q = {};
	q.push({ sr,sc });


	if (board[sr][sc] == 1) h_num++;
	update_h_num(h_num, ki,sr,sc);

	while (!q.empty()) {
		
		ki++;
		int q_size = q.size();
		for (int s = 0; s < q_size; s++) {
			int r, c;
			node now = q.front();
			q.pop();

			r = now.r;
			c = now.c;

			for (int i = 0; i < 4; i++) {

				int nr, nc;
				nr = r + dr[i];
				nc = c + dc[i];

				if (0 > nr || nr >= n || 0 > nc || nc >= n) continue;
				if (visited[nr][nc] != 0) continue;
				if (board[nr][nc] == 1) h_num++;

				visited[nr][nc] = visited[r][c] + 1;
				q.push({ nr,nc });
			}
		}
		update_h_num(h_num, ki,sr,sc);
	}

	return;
}

// 모든 좌표에서 서비스 영역 탐색
void count_home() {
	for (int r = 0; r < n; r++) {
		for (int c = 0; c < n; c++) {
			bfs(r, c);
		}
	}
}

int main() {
	int t = 0;

	cin >> t;

	for (int tc = 0; tc < t; tc++) {
		max_ans = 0;
		memset(board, 0, sizeof(board));

		cin >> n >> m;

		for (int r = 0; r < n; r++) {
			for (int c = 0; c < n; c++) {
				cin >> board[r][c];
			}
		}

		count_home();
		cout << "#" << tc + 1 << " " << max_ans << endl;
	}
	return 0;
}