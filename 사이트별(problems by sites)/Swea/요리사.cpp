#define _NO_SECURE_WARNINGS

#include <vector>
#include <string.h>
#include <cstdlib>
#include <cctype>
#include <iostream>

using namespace std;

int menu[16][16];
int visited[16];

int food_a[16];
int answer = 21e8;
int n = 0;

void dfs(int a, int num, int idx) {
	if (a >= num) {
		int a_sum = 0;
		int b_sum = 0;

		for (int i = 0; i < n; i++) {
			if (food_a[i] == 1)
				for (int j = 0; j < n; j++)
				{
					if(food_a[j] == 1) a_sum += menu[i][j];
				}
			else
			{
				for (int j = 0; j < n; j++) {
					if (food_a[j] == 0) b_sum += menu[i][j];
				}
			}
		}

		if (abs(a_sum - b_sum) < answer) answer = abs(a_sum - b_sum);

		return;
	}

	for (int i = idx; i < n; i++) {
		food_a[i] = 1;
		dfs(a+1, num, i+1);
		food_a[i] = 0;
	}

}
int main() {
	int tc = 0;
	cin >> tc;

	for (int t = 0; t < tc; t++) {
		n = 0;
		cin >> n;

		memset(menu, 0, sizeof(menu));
		memset(food_a, 0, sizeof(food_a));
		answer = 21e8;

		for (int r = 0; r < n; r++) {
			for (int c = 0; c < n; c++) {
				cin >> menu[r][c];
			}
		}

		dfs(0, n / 2,0);
		cout << "#" << t+1 << " " << answer << endl;

	}
	return 0;
}
