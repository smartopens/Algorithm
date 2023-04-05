#define _CRT_SECURE_NO_WARNINGS

#include <queue>
#include <iostream>

using namespace std;

int board[100][100];

int dr[3] = { 0,0,1 };
int dc[3] = { -1,1,0 };

struct node {
	int r;
	int c;
};

bool is_ok = false;

void bfs(int sc) {
	queue<node> q = {};
	q.push({ 0,sc });

	int visited[100][100] = { {} };
	visited[0][sc] = 1;

	while (!q.empty()) {

		node now = q.front();
		q.pop();

		int r, c;
		int nr, nc;

		r = now.r;
		c = now.c;

		bool col_di = false;
		for (int i = 0; i < 2; i++) {
			nr = r + dr[i];
			nc = c + dc[i];

			if (0 > nr || 100 <= nr || 0 > nc || 100 <= nc) continue;
			if (visited[nr][nc] != 0) continue;
			if (board[nr][nc] == 0) continue;

			if (board[nr][nc] == 2) {
				is_ok = true;


				//cout << endl;
				//for (int r = 0; r < 100; r++) {
				//	for (int c = 0; c < 100; c++) {
				//		cout << visited[r][c] << " ";
				//	}
				//	cout << endl;
				//}

				return;
			}
			col_di = true;
			visited[nr][nc] = 1;
			q.push({ nr,nc });
		}

		if (col_di == false) {
			for (int i = 2; i < 3; i++) {
				nr = r + dr[i];
				nc = c + dc[i];

				if (0 > nr || 100 <= nr || 0 > nc || 100 <= nc) continue;
				if (visited[nr][nc] != 0) continue;
				if (board[nr][nc] == 0) continue;

				if (board[nr][nc] == 2) {
					is_ok = true;


					//cout << endl;
					//for (int r = 0; r < 100; r++) {
					//	for (int c = 0; c < 100; c++) {
					//		cout << visited[r][c] << " ";
					//	}
					//	cout << endl;
					//}

					return;
				}

				visited[nr][nc] = 1;
				q.push({ nr,nc });
			}
		}
	}

	return;
}

int main() {
	int t = 10;

	for (int i = 1; i < t + 1; i++) {
		int tc;
		cin >> tc;

		is_ok = false;
		for (int r = 0; r < 100; r++) {
			for (int c = 0; c < 100; c++) {
				cin >> board[r][c];
			}
		}

		for (int sc = 0; sc < 100; sc++) {
			if (board[0][sc] == 0) continue;

			bfs(sc);

			if (is_ok == true) {

				cout << "#" << tc << " " << sc << endl;
				
				break;
			}
		}
	}
	return 0;
}