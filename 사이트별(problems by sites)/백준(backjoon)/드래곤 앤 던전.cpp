#include <iostream>
#include <math.h>
#include <algorithm>

using namespace std;

int n;
int w_atk;

struct dun_no
{
	int t;
	int at;
	int hp;
};

dun_no dun_info [124000];
long long min_hp;
bool dun_ok;

long long max_w_hp = 1e18;

void dun_count(int a, int w_at, long long w_hp)
{
	if (a > n - 1)
	{
		dun_ok = true;
		return;
	}

	long long to_hp;
	int to_at;
	int m_atk, m_hp, plus_at, plus_hp;

	if (dun_info[a].t == 1)
	{
		m_atk = dun_info[a].at;
		m_hp = dun_info[a].hp;
		to_hp = w_hp - (ceil(m_hp / w_at) - 1) * m_atk;

		if (to_hp > 0)
		{
			dun_count(a + 1, w_at, to_hp);
		}
	}
	else
	{
		plus_at = dun_info[a].at;
		plus_hp = dun_info[a].hp;

		dun_count(a + 1, min(1000000, w_at + plus_at), min(max_w_hp, w_hp + plus_hp));
	}
}

int main()
{
	cin >> n >> w_atk;
	int in_t, in_a, in_h;
	for (int s = 0; s < n; s++)
	{
		cin >> in_t >> in_a >> in_h;
		dun_info[s] = { in_t, in_a, in_h};
	}

	long long min_v = 1;
	long long max_v = 1e18;
	long long mid_hp = 0;

	while (min_v < max_v)
	{
		mid_hp = (min_v + max_v) / 2;
		dun_ok = false;
		max_w_hp = mid_hp;
		dun_count(0, w_atk, mid_hp);

		if (dun_ok == true)
		{
			min_hp = mid_hp;
			max_v = mid_hp - 1;
			//cout << min_hp << endl;
		}
		else
		{
			min_v = mid_hp + 1;
		}
	}

	cout << min_hp << endl;
	return 0;
}