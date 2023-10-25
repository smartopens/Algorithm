#include <iostream>
#include <algorithm>

using namespace std;

// 삭제기준 1) 추천수, 2) 시간 순
// <int,node<int,int>> students, s_size, <string,int> s_vi,

int n;
int m;

struct node {
	int sid;
	int s_w;
	int s_t;
};

node stds[102];
int s_vi[102];

int s_size;
int out_stds[102];

bool sno_cmp(node a, node b)
{
	if (a.s_w < b.s_w)
	{
		return true;
	}
	if (a.s_w > b.s_w)
	{
		return false;
	}
	if (a.s_t > b.s_t)
	{
		return true;
	}
	if (a.s_t < b.s_t)
	{
		return false;
	}
	return false;
}

bool out_cmp(int a, int b)
{
	if (a < b)
	{
		return true;
	}
	if (a > b)
	{
		return false;
	}
	return false;
}


int main()
{
	cin >> n;
	cin >> m;

	int s_n;
	for (int v = 1; v < 101; v++)
	{
		stds[v] = { v,1000,0 };
	}

	for (int i = 0; i < m; i++)
	{
		cin >> s_n;

		if (s_size >= n)
		{
			if (stds[s_n].s_w == 0 || stds[s_n].s_w == 1000)
			{
				int d_id = 0;
				int min_w = 1000;
				int max_t = 0;
				for (int v = 1; v < 101; v++)
				{
					if (stds[v].s_w == 0 || stds[v].s_w == 1000) continue;

					if (stds[v].s_w < min_w)
					{
						min_w = stds[v].s_w;
						d_id = v;
						max_t = stds[v].s_t;
					}
					else if (stds[v].s_w == min_w)
					{
						if (stds[v].s_t > max_t)
						{
							d_id = v;
							max_t = stds[v].s_t;
						}
					}
				}

				stds[d_id] = { d_id,0,0 };
				stds[s_n] = { s_n,1,0 };
			}
			else {
				stds[s_n].s_w = stds[s_n].s_w + 1;
			}

			for (int v = 1; v < 101; v++)
			{
				if (stds[v].s_w == 0 || stds[v].s_w == 1000) continue;
				stds[v].s_t = stds[v].s_t + 1;
			}

			continue;
		}

		if(stds[s_n].s_w == 1000)
		{
			stds[s_n] = { s_n,1, 0};
			s_size += 1;
		}
		else
		{
			stds[s_n].s_w = stds[s_n].s_w + 1;
		}

		for (int v = 1; v < 101; v++)
		{
			if (stds[v].s_w == 0 || stds[v].s_w == 1000) continue;
			stds[v].s_t = stds[v].s_t + 1;
		}
	}

	for (int v = 1; v < 101; v++)
	{
		if (stds[v].s_w == 0 || stds[v].s_w == 1000) continue;
		cout << v << " ";
	}
	return 0;
}
