#include <iostream>
#include <string>

using namespace std;

int n, k;
int t_map[10][10];
int vi[10];

int min_ts;

// 전체 순회 완성하기
void c_count(int a, string now_c)
{
	// 특정 순회에서 최적 경로 적용하기 
	if (a > n - 1)
	{
		int now_ts = 0;
		if ((int)(now_c[0]-'0') == k)
		{
			for (int s = 0; s < now_c.length()-1; s++)
			{
				now_ts += t_map[(now_c[s] - '0')][(now_c[s + 1] - '0')];
			}

			if (now_ts < min_ts)
			{
				min_ts = now_ts;
			}
		}
		return;
	}

	int to_v;
	string to_c;
	for (int i = 0; i < n; i++)
	{
		to_v = i;
		if (vi[to_v] != 0) continue;
		vi[to_v] = 1;

		to_c = now_c + (char)(to_v + '0');
		c_count(a + 1, to_c);
		vi[to_v] = 0;
	}
}
 
int main()
{
	cin >> n >> k;
	for (int r = 0; r < n; r++)
	{
		for (int c = 0; c < n; c++)
		{
			cin >> t_map[r][c];
		}
	}

	for (int k = 0; k < n; k++)
	{
		for (int sv = 0; sv < n; sv++)
		{
			for (int ev = 0; ev < n; ev++)
			{
				if (t_map[sv][k] != 0 && t_map[k][ev] != 0)
				{
					t_map[sv][ev] = min(t_map[sv][ev], t_map[sv][k] + t_map[k][ev]);
				}
			}
		}
	}

	min_ts = 21e8;
	c_count(0, "");

	cout << min_ts << endl;
	return 0;
}