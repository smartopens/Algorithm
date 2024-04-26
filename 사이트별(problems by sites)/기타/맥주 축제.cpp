#include <iostream>
#include <math.h>
#include <vector>
#include <algorithm>

using namespace std;

typedef long long ll;

ll n, m, k;

struct d_no
{
	ll w;
	ll co;
};

d_no d_info[200002];

ll min_d;

bool d_count(ll m_v)
{
	vector<int> c_bears = {};
	for (int s = 0; s < k; s++)
	{
		if (d_info[s].co <= m_v)
		{
			c_bears.push_back(d_info[s].w);
		}
	}

	if (c_bears.size() < n)
	{
		return false;
	}

	sort(c_bears.begin(), c_bears.end(), greater<ll>());
	int now_m = 0;
	for (int s = 0; s < n; s++)
	{
		now_m += c_bears[s];
	}

	if (now_m >= m)
	{
		return true;
	}

	return false;

}

int main()
{
	cin >> n >> m >> k;
	ll in_w, in_co;
	for (int dv = 0; dv < k; dv++)
	{
		cin >> in_w >> in_co;
		d_info[dv] = { in_w, in_co };
	}

	ll l_d = 1;
	ll r_d = pow(2, 31)-1;
	ll m_d = 0;
	//cout << l_d << " " << r_d << endl;
	min_d = 21e8;
	while (l_d <= r_d)
	{
		m_d = (l_d + r_d) / 2;

		if (d_count(m_d) == true)
		{
			r_d = m_d -1;
			min_d = m_d;
		}
		else
		{
			l_d = m_d + 1;
		}

	}

	if (min_d == 21e8)
	{
		cout << -1 << endl;
	}
	else
	{
		cout << min_d << endl;
	}
	return 0;
}