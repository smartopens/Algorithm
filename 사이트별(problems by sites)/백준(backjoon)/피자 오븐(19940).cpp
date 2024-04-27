#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int t;
int n;

vector<int> b_type;

int min_pn;
vector<vector<int>> b_case;

bool b_cmp(vector<int> a, vector<int>b)
{
	if (a[0] < b[0])
	{
		return true;
	}
	if (a[0] > b[0])
	{
		return false;
	}

	if (a[1] < b[1])
	{
		return true;
	}
	if (a[1] > b[1])
	{
		return false;
	}

	if (a[2] < b[2])
	{
		return true;
	}
	if (a[2] > b[2])
	{
		return false;
	}

	if (a[3] < b[3])
	{
		return true;
	}
	if (a[3] > b[3])
	{
		return false;
	}

	if (a[4] < b[4])
	{
		return true;
	}
	if (a[4] > b[4])
	{
		return false;
	}
	return false;
}

void bake_pizza(int a, int pn, int tm)
{
	if (a > 2)
	{
		if (min_pn > pn)
		{
			b_case.clear();
			b_case.push_back(b_type);
			min_pn = pn;
		}
		else if (min_pn == pn)
		{
			b_case.push_back(b_type);
		}
		return;
	}

	int now_p = 0;
	int now_tm;
	vector<int> ori_b_type = b_type;
	if (a == 0)
	{
		now_tm = tm;
		now_p = 0;
		while (now_tm < n)
		{
			now_tm += 60;
			now_p += 1;
		}
		b_type[0] += now_p;
		bake_pizza(a + 1, pn + now_p, now_tm);
		
		b_type[0] -= 1;
		bake_pizza(a + 1, pn + now_p-1, now_tm-60);
		b_type = ori_b_type;
	}
	else if (a == 1)
	{
		now_tm = tm;
		now_p = 0;
		if (n > now_tm)
		{
			// >> 20, 24, 30
			while (now_tm < n)
			{
				now_tm += 10;
				now_p += 1;
			}
			b_type[1] += now_p;
			bake_pizza(a + 1, pn + now_p, now_tm);

			b_type[1] -= 1;
			bake_pizza(a + 1, pn + now_p-1, now_tm-10);
			b_type = ori_b_type;
		}
		else
		{
			// 20, 24, 30 <<
			while (now_tm > n)
			{
				now_tm -= 10;
				now_p += 1;
			}

			b_type[2] += now_p;
			bake_pizza(a + 1, pn + now_p, now_tm);

			b_type[2] -= 1;
			bake_pizza(a + 1, pn + now_p-1, now_tm+10);
			b_type = ori_b_type;
		}
	}
	else if (a == 2)
	{
		now_tm = tm;
		now_p = 0;
		if (n > now_tm)
		{
			// >> 20, 24, 30
			while (now_tm < n)
			{
				now_tm += 1;
				now_p += 1;
			}
			b_type[3] += now_p;
			bake_pizza(a + 1, pn + now_p, now_tm);
			b_type = ori_b_type;
		}
		else
		{
			// 20, 24, 30 <<
			while (now_tm > n)
			{
				now_tm -= 1;
				now_p += 1;
			}

			b_type[4] += now_p;
			bake_pizza(a + 1, pn + now_p, now_tm);
			b_type = ori_b_type;
		}
	}

}

int main()
{
	cin >> t;
	for (int tc = 0; tc < t; tc++)
	{
		cin >> n;
		b_type = { 0,0,0,0,0 };
		min_pn = 21e8;
		b_case.clear();
		bake_pizza(0, 0,0);

		sort(b_case.begin(), b_case.end(), b_cmp);
		for (int s = 0; s < 5; s++)
		{
			cout << b_case[0][s] << " ";
		}
	}

	return 0;
}